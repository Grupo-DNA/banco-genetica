import gspread
from google.oauth2.service_account import Credentials

import time

# ===== CONECTA NO SHEETS DO NORMSCORE GLOBAL ANTIGO
def conectar_normscore_antigo():

    escopos = ['https://www.googleapis.com/auth/spreadsheets']
    credenciais = Credentials.from_service_account_file('recursos/credentials.json', scopes=escopos)
    client = gspread.authorize(credenciais)

    sheet_id = '108KQpjPqOkWeOwH8z_2HST8EeXWWKJe-FFo2IpktFSI'
    workbook = client.open_by_key(sheet_id)
    sheet = workbook.get_worksheet_by_id(1936220)

    return sheet

# ===== CONECTA NO SHEETS DO NORMSCORE GLOBAL NOVO
def conectar_normscore_novo():

    escopos = ['https://www.googleapis.com/auth/spreadsheets']
    credenciais = Credentials.from_service_account_file('recursos/credentials.json', scopes=escopos)
    client = gspread.authorize(credenciais)

    sheet_id = '108KQpjPqOkWeOwH8z_2HST8EeXWWKJe-FFo2IpktFSI'
    workbook = client.open_by_key(sheet_id)
    sheet = workbook.get_worksheet_by_id(968767897)

    return sheet

# ===== LISTA AS DIFERENTES CARACTERISTICAS DO NORMSCORE
def lista_caracteristicas(sheet):

    caracteristicas = list(set(sheet.col_values(2)[3:]))
    caracteristicas.sort()

    return caracteristicas

# ===== DADA UMA CARACTERISTICA, RETORNA OS DADOS REFERENTES DO NORMSCORE
def consulta_caracteristica_normscore(caracteristica, sheet):

    dadosCaracteristica = sheet.findall(caracteristica)
    posicoes = []

    for dado in dadosCaracteristica:
        posicoes.append(dado.row)

    rangeCelulas = f'B{min(posicoes)}:H{max(posicoes)}'
    return sheet.get(rangeCelulas)