from recursos import funcoes

if __name__ == '__main__':

    #funcoes.consulta_frequencia_snp(['rs3918290'])
    #funcoes.consulta_frequencia_snp(['rs11246602'])
    #funcoes.consulta_frequencia_snp('rs11246602')
    #funcoes.insere_dados()

    snps = [
        'rs11246602',
        'rs4848306',
        'rs1143634',
        'rs28497577',
        'rs917997',
        'rs13098911',
        'rs653178',
        'rs11221332',
        'rs4819388',
        'rs4675374',
        'rs1738074',
        'rs12203592',
        'rs41380347',
        'rs4994',
        'rs3803357',
        'rs1800012',
        'rs33972313',
        'rs2400707',
        'rs4333882'
    ]

    funcoes.consulta_frequencia_snp(snps)