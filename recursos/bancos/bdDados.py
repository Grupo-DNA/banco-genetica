from pymongo import MongoClient

# ===== RETORNA UM PONTEIRO AO BANCO DE GENETICO
def conecta_banco():

    try:
        client = MongoClient("localhost", 27017)

    except:

        return 'Erro ao conectar com o banco!'

    database = client['banco-snps']

    return database

# ===== INSERE UM DADO BRUTO DE UMA PESSOA
def insere_dado_bruto(idPessoa, dadoBruto, banco):

    try:
        colecao = banco[idPessoa]
        colecao.insert_many(dadoBruto)

        print(f'Sucesso na inserção! {idPessoa}')

    except:
        print('Não foi possivel inserir no banco!')

# ===== CRIA UM INDEX PARA UMA COLLECTION COM BASE NO SNP
def cria_um_index(idPessoa, banco):

    try:
        colecao = banco[idPessoa]
        colecao.create_index('snp')

        print(f'Index criado com sucesso ! {idPessoa}')

    except:
        print('Falha ao criar index !')

    print('======================================')

# ===== CONSULTA UM SNP DE UMA PESSOA
def consulta_snp(snp, banco, pessoa):

    try:
        tabela = banco[f'{pessoa}']
        return tabela.distinct('alelos', {'snp': f'{snp}'})

    except:
        print(f'Não foi possivel consultar a collection: {pessoa}')