import pandas as pd
from .interface import pergunta_diretorio
from .drive import conectar_normscore_novo, conectar_normscore_antigo, lista_caracteristicas, consulta_caracteristica_normscore
from .bancos import bdEstatisticas, bdDados
from .parser import identifica_tipo_arquivo, trata_arquivo
from .auxiliares import conta_genotipos, le_string_alphanumerica, calcula_frequencias, trata_caracteristica_normscore, auxiliar_calcula_prs
from os import listdir
import json

from time import sleep

# ===== LE E INSERE DADOS BRUTOS DE UM PATH ESPECIFICO
def insere_dados():

    path = pergunta_diretorio()
    listaArquivos = listdir(path)

    # Estabelece uma conexão com banco
    banco = bdDados.conecta_banco()

    # Para cada dado bruto
    progresso = 0
    maximo = len(listaArquivos)

    for arquivo in listaArquivos:
        tipoDoArquivo = identifica_tipo_arquivo(f'{path}\\{arquivo}')
        dados = trata_arquivo(f'{path}\\{arquivo}', tipoDoArquivo)

        nomePessoa = le_string_alphanumerica(arquivo)
        bdDados.insere_dado_bruto(nomePessoa, dados, banco)
        bdDados.cria_um_index(nomePessoa, banco)

        progresso += 1
        print(f'<<<{progresso}/{maximo}>>>')

    banco.client.close()

# ===== FAZ CONTAGEM DE ALELOS DE UM SNP
def conta_alelos_snp(snp):

    # Consulta
    resposta = []
    banco = bdDados.conecta_banco()
    listaPessoas = banco.list_collection_names()

    # Trata pessoas com mais de uma variação de alelos
    for pessoa in listaPessoas:
        alelos = bdDados.consulta_snp(snp, banco, pessoa)
        if len(alelos) > 1:
            print('\n\n<<< AVISO >>>\n'
                  f'Cliente: {pessoa} foi desconsiderado por inconsistencia de informação!\n'
                  f'Para o snp: {snp}. Foram observadas as variações: {alelos}\n'
                  '<<< FIM DO AVISO >>>\n\n')

        else:
            resposta.append(alelos)

    banco.client.close()

    return conta_genotipos(snp, resposta)

# ===== CONSULTA FREQUENCIA DE UM SNP
def consulta_frequencia_snp(listaSnps):
    #outputTotal = []
    #outputFreq = []

    for snp in listaSnps:

        resposta_banco = bdEstatisticas.consulta_snp(snp)
        if resposta_banco != None:
            #outputTotal.append(resposta_banco) ### ---
            #outputFreq.append(dict(calcula_frequencias(resposta_banco))) ### ---

            print(json.dumps(resposta_banco)+',')
            print(json.dumps(calcula_frequencias(resposta_banco))+',') #DEBUG

        else:
            contagem = conta_alelos_snp(snp)
            bdEstatisticas.insere_contagem_snp(contagem)

            #outputTotal.append(contagem) ### ---
            #outputFreq.append(json.dumps(calcula_frequencias(contagem))) ### ---

            print(json.dumps(contagem))
            print(calcula_frequencias(contagem)) #DEBUG

    #dfTT = pd.DataFrame(outputTotal) ###
    #dfFR = pd.DataFrame(outputFreq) ###

    #dfTT.to_csv('total.xlsx', index=False) ###
    #dfFR.to_csv('freq.xlsx', index=False) ###

# ===== CONSULTA SNPS DE UMA PESSOA EM UMA DETERMINADA CARACTERISTICA
def consulta_snps_caracteristica(client_id, snpsCaracteristica):

    banco = bdDados.conecta_banco()
    snpsPessoa = {}

    for each in snpsCaracteristica:
        alelo = bdDados.consulta_snp(each['snp'], banco, client_id)
        if len(alelo) == 1:
            snpsPessoa[f'{each['snp']}'] = alelo[0]

        else:
            snpsPessoa[f'{each['snp']}'] = ''

    banco.client.close()
    return snpsPessoa

# ===== CALCULA E INSERE PRS DE UMA PESSOA PARA TODAS AS CARACTERISTICAS
def calcula_prs_pessoa(client_id):

    sleep(2)

    prsPessoa = {
        '_id': client_id
    }

    antigo = conectar_normscore_antigo()
    #novo = conectar_normscore_novo()

    for caracteristica in lista_caracteristicas(antigo):
        consulta = consulta_caracteristica_normscore(caracteristica, antigo)

        dicNormscore = trata_caracteristica_normscore(consulta)
        dicPessoa = consulta_snps_caracteristica(client_id, dicNormscore['snps'])

        prsCaracteristica = auxiliar_calcula_prs(dicNormscore, dicPessoa)
        prsPessoa[caracteristica] = prsCaracteristica

        print(prsPessoa)

# ===== CALCULA E INSERE PRS DE UMA CARACTERISTICA PARA TODAS AS PESSOAS
def calcula_prs_caracteristica(caracteristica):

    #normscore = conectar_normscore_antigo()
    normscore = conectar_normscore_novo()

    consulta = consulta_caracteristica_normscore(caracteristica, normscore)
    dicNormscore = trata_caracteristica_normscore(consulta)

    bancoPrs = bdEstatisticas.conecta_banco()
    bancoPessoas = bdDados.conecta_banco()
    for pessoa in bancoPessoas.list_collection_names():
        dicPessoa = consulta_snps_caracteristica(pessoa, dicNormscore['snps'])

        prsCaracteristica = auxiliar_calcula_prs(dicNormscore, dicPessoa)
        bancoPrs['caracteristicas-novo'].update_one({'_id': pessoa}, {'$set':{caracteristica: prsCaracteristica}}, upsert=True)

    bancoPrs.client.close()
    bancoPessoas.client.close()



# ===================== <<< TEMP >>> ========================
def temp_calcula_tudo():

    #antigo = conectar_normscore_antigo()
    novo = conectar_normscore_novo()
    listaCaracteristicas = lista_caracteristicas(novo)

    contador = 0

    for caracteristica in listaCaracteristicas:
        sleep(10)

        print(f'<<< {contador}/{len(listaCaracteristicas)} >>>')
        calcula_prs_caracteristica(caracteristica)

        contador += 1


#testa compatibilidade do banco
def compatibilidade():

    banco = bdEstatisticas.conecta_banco()
    tabela = banco['caracteristicas-novo']

    for caracteristica in lista_caracteristicas(conectar_normscore_novo()):

        pipeline = [
            {
                '$match': {
                    caracteristica: {
                        '$ne': None
                    }
                }
            },
            {
                '$count': caracteristica
            }
        ]

        try:
            print(tabela.aggregate(pipeline).next())
        except:
            print('{'+caracteristica+': NENHUM}')