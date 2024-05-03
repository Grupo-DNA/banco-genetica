import pandas as pd

# ===== RETORNA UM DICIONARIO REFERENTE AO ARQUIVO DE DADOS
def trata_arquivo(path, tipo:int):

    # Tratando arquivo de tipo 1
    if tipo == 1:
        dados = pd.read_csv(path, delimiter='\t', dtype={
            "RsID": "string",
            "Sample ID": "string",
            "SNP Name": "string",
            "Allele1 - Plus": "string",
            "Allele2 - Plus": "string",
            "Chr": "string"
        })
        dados = dados.rename(columns={
            "RsID": "snp",
            "Sample ID": "id_club",
            "SNP Name": "posicao",
            "Allele1 - Plus": "alelo_1",
            "Allele2 - Plus": "alelo_2",
            "Chr": "cromossomo"
        })
        dados = dados[dados['snp'].str.contains(r'^rs\d+')]
        dados['alelos'] = dados['alelo_1'] + dados['alelo_2']
        dados = dados.drop(columns='id_club')
        dados = dados.drop(columns='alelo_1')
        dados = dados.drop(columns='alelo_2')
        dados['snp'] = dados['snp'].str.split(',')
        dados = dados.explode('snp')

        dicionarios = dados.to_dict(orient='records')

        for dicionario in dicionarios:
            if dicionario['alelos'] == '--':
                dicionario.pop('alelos', None)

        return dicionarios

    # Tratando arquivo de tipo 2
    elif tipo == 2:
        dados = pd.read_csv(path, delimiter='\t', dtype={
            "RSID": "string",
            "POSITION": "string",
            "RESULT": "string",
            "CHROMOSOME": "string"
        })
        dados = dados.rename(columns={
            "RSID": "snp",
            "POSITION": "posicao",
            "RESULT": "alelos",
            "CHROMOSOME": "cromossomo"
        })
        dados = dados[dados['snp'].str.contains(r'^rs\d+')]
        dados['snp'] = dados['snp'].str.split(',')
        dados = dados.explode('snp')

        dicionarios = dados.to_dict(orient='records')

        for dicionario in dicionarios:
            if dicionario['alelos'] == '--':
                dicionario.pop('alelos', None)

        return dicionarios

    # Tratando arquivo de tipo 3
    elif tipo == 3:
        dados = pd.read_csv(path, delimiter=',', dtype={
            "RSID": "string",
            "POSITION": "string",
            "RESULT": "string",
            "CHROMOSOME": "string"
        })
        dados = dados.rename(columns={
            "RSID": "snp",
            "POSITION": "posicao",
            "RESULT": "alelos",
            "CHROMOSOME": "cromossomo"
        })
        dados = dados[dados['snp'].str.contains(r'^rs\d+')]
        dados['snp'] = dados['snp'].str.split(',')
        dados = dados.explode('snp')
        dados['snp'] = dados['snp'].str.extract(r'(rs\d+)')

        dicionarios = dados.to_dict(orient='records')

        for dicionario in dicionarios:
            if dicionario['alelos'] == '--':
                dicionario.pop('alelos', None)

        return dicionarios

    # Tratando arquivo de tipo 4
    elif tipo == 4:
        dados = pd.read_csv(path, delimiter=',', skiprows=12, dtype={
            "RSID": "string",
            "POSITION": "string",
            "RESULT": "string",
            "CHROMOSOME": "string"
        })
        dados = dados.rename(columns={
            "RSID": "snp",
            "POSITION": "posicao",
            "RESULT": "alelos",
            "CHROMOSOME": "cromossomo"
        })
        dados = dados[dados['snp'].str.contains(r'^rs\d+')]
        dados['snp'] = dados['snp'].str.split(',')
        dados = dados.explode('snp')
        dados['snp'] = dados['snp'].str.extract(r'(rs\d+)')

        dicionarios = dados.to_dict(orient='records')

        for dicionario in dicionarios:
            if dicionario['alelos'] == '--':
                dicionario.pop('alelos', None)

        return dicionarios

    # Tratando arquivo de tipo 5
    elif tipo == 5:
        dados = pd.read_csv(path, delimiter=',', header=None, names=['snp', 'cromossomo', 'posicao', 'alelos'], dtype={
            "snp": "string",
            "cromossomo": "string",
            "posicao": "string",
            "alelos": "string"
        })
        dados = dados[dados['snp'].str.contains(r'^rs\d+')]
        dados['snp'] = dados['snp'].str.split(',')
        dados = dados.explode('snp')
        dados['snp'] = dados['snp'].str.extract(r'(rs\d+)')

        dicionarios = dados.to_dict(orient='records')

        for dicionario in dicionarios:
            if dicionario['alelos'] == '--':
                dicionario.pop('alelos', None)

        return dicionarios

    # Tratando arquivo de tipo 6
    elif tipo == 6:
        dados = pd.read_csv(path, delimiter='\t', skiprows=10, dtype={
            "RsID": "string",
            "Sample ID": "string",
            "SNP Name": "string",
            "Allele1 - Plus": "string",
            "Allele2 - Plus": "string",
            "Chr": "string"
        })
        dados = dados.rename(columns={
            "RsID": "snp",
            "Sample ID": "id_club",
            "SNP Name": "posicao",
            "Allele1 - Plus": "alelo_1",
            "Allele2 - Plus": "alelo_2",
            "Chr": "cromossomo"
        })

        dados = dados[dados['snp'].str.contains(r'^rs\d+')]
        dados['alelos'] = dados['alelo_1'] + dados['alelo_2']
        dados = dados.drop(columns='id_club')
        dados = dados.drop(columns='alelo_1')
        dados = dados.drop(columns='alelo_2')
        dados['snp'] = dados['snp'].str.split(',')
        dados = dados.explode('snp')

        dicionarios = dados.to_dict(orient='records')

        for dicionario in dicionarios:
            if dicionario['alelos'] == '--':
                dicionario.pop('alelos', None)

        return dicionarios

    # Tratando arquivo de tipo 7
    elif tipo == 7:
        dados = pd.read_csv(path, delimiter='\t', dtype={
            "rsid": "string",
            "Sample ID": "string",
            "SNP Name": "string",
            "Allele1 - Plus": "string",
            "Allele2 - Plus": "string",
            "Chr": "string"
        })
        dados = dados.rename(columns={
            "rsid": "snp",
            "Sample ID": "id_club",
            "SNP Name": "posicao",
            "Allele1 - Plus": "alelo_1",
            "Allele2 - Plus": "alelo_2",
            "Chr": "cromossomo"
        })
        dados = dados[dados['snp'].str.contains(r'^rs\d+')]
        dados['alelos'] = dados['alelo_1'] + dados['alelo_2']
        dados = dados.drop(columns='id_club')
        dados = dados.drop(columns='alelo_1')
        dados = dados.drop(columns='alelo_2')
        dados['snp'] = dados['snp'].str.split(',')
        dados = dados.explode('snp')

        dicionarios = dados.to_dict(orient='records')

        for dicionario in dicionarios:
            if dicionario['alelos'] == '--':
                dicionario.pop('alelos', None)

        return dicionarios

    # Tratando arquivo de tipo 8
    elif tipo == 8:
        dados = pd.read_csv(path, delimiter=';', dtype={
            "rsid": "string",
            "Sample ID": "string",
            "SNP Name": "string",
            "Allele1 - Plus": "string",
            "Allele2 - Plus": "string",
            "Chr": "string"
        })
        dados = dados.rename(columns={
            "rsid": "snp",
            "Sample ID": "id_club",
            "SNP Name": "posicao",
            "Allele1 - Plus": "alelo_1",
            "Allele2 - Plus": "alelo_2",
            "Chr": "cromossomo"
        })
        dados = dados[dados['snp'].str.contains(r'^rs\d+')]
        dados['alelos'] = dados['alelo_1'] + dados['alelo_2']
        dados = dados.drop(columns='id_club')
        dados = dados.drop(columns='alelo_1')
        dados = dados.drop(columns='alelo_2')
        dados['snp'] = dados['snp'].str.split(',')
        dados = dados.explode('snp')

        dicionarios = dados.to_dict(orient='records')

        for dicionario in dicionarios:
            if dicionario['alelos'] == '--':
                dicionario.pop('alelos', None)

        return dicionarios

    else:
        print("Não é possivel ler esse formato!")

# ===== RETORNA O TIPO DO ARQUIVO DE DADOS
def identifica_tipo_arquivo(path):
    with open(path, 'r') as arquivo:
        # Le as 5 primeiras linhas do arquivo
        linhas = [next(arquivo) for _ in range(5)]

    # Checando modelos
    if ('rsid' in linhas[0] and 'Sample ID' in linhas[0] and 'SNP Name' in linhas[0] and 'Allele1 - Plus' in linhas[0]
            and 'Allele2 - Plus' in linhas[0] and 'Chr' in linhas[0] and ';' in linhas[0]):
        return 8

    if ('RsID' in linhas[0] and 'Sample ID' in linhas[0] and 'SNP Name' in linhas[0] and 'Allele1 - Plus' in linhas[0]
            and 'Allele2 - Plus' in linhas[0] and 'Chr' in linhas[0]):
        return 1

    if 'RSID' in linhas[0] and 'CHROMOSOME' in linhas[0] and 'POSITION' in linhas[0] and 'RESULT' in linhas[0] and ',' in linhas[0]:
        return 3

    if 'RSID' in linhas[0] and 'CHROMOSOME' in linhas[0] and 'POSITION' in linhas[0] and 'RESULT' in linhas[0]:
        return 2

    if '##fileformat=MyHeritage' in linhas[0]:
        return 4

    if '[Header]' in linhas[0]:
        return 6

    if 'rs' in linhas[0] and ',' in linhas[0]:
        return 5

    if ('rsid' in linhas[0] and 'Sample ID' in linhas[0]):
        return 7

    else:
        return 0
