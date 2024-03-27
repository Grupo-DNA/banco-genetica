from pymongo import MongoClient

# ===== RETORNA UM PONTEIRO AO BANCO DE CARACTERISTICAS
def conecta_banco():

    try:
        client = MongoClient("localhost", 27017)
    except:
        return 'Erro ao conectar com o banco!'

    database = client['banco-estatisticas']

    return database

# ===== CONSULTA CONTAGEM DE UM SNP
def consulta_snp(snp):
    banco = conecta_banco()

    try:
        tabela = banco['frequencias']
        return tabela.find_one({'_id': snp})

    except:
        print('Não foi possivel consultar frequência !')

# ===== INSERE CONTAGEM DE UM SNP
def insere_contagem_snp(contagem):
    banco = conecta_banco()

    try:
        tabela = banco['frequencias']
        tabela.insert_one(contagem)

        print('Contagem inserida com sucesso!')

    except:
        print('Falha na inserção da contagem!')

    banco.client.close()