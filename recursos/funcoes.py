from .bancos import bdEstatisticas, bdDados
from .parser import identifica_tipo_arquivo, trata_arquivo
from .auxiliares import conta_genotipos, le_string_alphanumerica
from os import listdir
import json

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

    for snp in listaSnps:

        resposta_banco = bdEstatisticas.consulta_snp(snp)
        if resposta_banco != None:
            print(resposta_banco)

        else:
            contagem = conta_alelos_snp(snp)
            bdEstatisticas.insere_contagem_snp(contagem)
            print(json.dumps(contagem))