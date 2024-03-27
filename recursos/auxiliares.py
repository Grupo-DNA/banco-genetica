from collections import defaultdict
import re
import json

# ===== RECEBE STRING E LE ATE CARACTERE NAO NUMERICO OU ALFABETICO
def le_string_alphanumerica(string: str):
    match = re.match(r'^[a-zA-Z0-9]*', string)
    return match.group(0)

# ===== ORGANIZA UMA STRING EM ORDEM CRESCENTE
def ordena_string(str:str) :
    str = ''.join(sorted(str))
    return str

# ===== CONTABILIZA ALELOS E GENOTIPOS
def conta_genotipos(snp, listaDadosSnp):

    contabilizacao = {
        '_id': snp,
        'totalPessoas': 0,
        'totalGenesLidos': 0,
        'totalGenesVazios': 0,
        'totalGenes': defaultdict(int),
        'totalAlelos': defaultdict(int)
    }

    # Total de pessoas
    contabilizacao['totalPessoas'] = len(listaDadosSnp)

    # Contabilizando genes
    for listaAlelos in listaDadosSnp:

        if len(listaAlelos) > 0:
            contabilizacao['totalGenesLidos'] += 1
            contabilizacao['totalGenes'][f'{ordena_string(listaAlelos[0])}'] += 1

        else:
            contabilizacao['totalGenesVazios'] += 1

    # Contabilizando alelos
    strAlelos = ''
    for gene in contabilizacao['totalGenes'].keys():
        strAlelos += gene
    listaAlelos = list(set(strAlelos))

    for alelo in listaAlelos:
        for gene in contabilizacao['totalGenes'].keys():
            contabilizacao['totalAlelos'][f'{alelo}'] += gene.count(alelo) * contabilizacao['totalGenes'][gene]

    return contabilizacao

# ===== CALCULA FREQUENCIA GENOTIPICA E ALELICA
def calcula_frequencias(contabilizacao: dict):

    frequencias = {
        'snp': contabilizacao['_id'],
        'frequenciaGene': defaultdict(float),
        'frequenciaAlelo': defaultdict(float)
    }

    #print(json.dumps(contabilizacao))
    #print(f'Snp: {contabilizacao['nomeSnp']}')

    # Frequencia Genica
    for gene in list(contabilizacao['totalGenes'].keys()):
        frequencia = contabilizacao['totalGenes'][f'{gene}'] / contabilizacao['totalGenesLidos']
        frequencias['frequenciaGene'][gene] = round(frequencia * 100, 2)

    # Cabeçalho freq. Alelica
    for alelo in list(contabilizacao['totalAlelos'].keys()):
        frequencia = contabilizacao['totalAlelos'][f'{alelo}'] / (contabilizacao['totalGenesLidos'] * 2)
        frequencias['frequenciaAlelo'][alelo] = round(frequencia * 100, 2)

    return json.dumps(frequencias)
