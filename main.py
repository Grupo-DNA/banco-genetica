from recursos import funcoes

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

if __name__ == '__main__':

    #funcoes.insere_dados()

    snps = [
        "rs11206510",
        "rs17114036",
        "rs17465637",
        "rs599839",
        "rs4845625",
        "rs6544713",
        "rs6725887",
        "rs515135",
        "rs2252641",
        "rs1561198",
        "rs2306374",
        "rs7692387",
        "rs17087335",
        "rs273909",
        "rs17609940",
        "rs3798220",
        "rs10947789",
        "rs4252120",
        "rs10953541",
        "rs11556924",
        "rs2023938",
        "rs3918226",
        "rs2954029",
        "rs264",
        "rs4977574",
        "rs579459",
        "rs111245230",
        "rs2505083",
        "rs1746048",
        "rs1412444",
        "rs12413409",
        "rs974819",
        "rs964184",
        "rs3184504",
        "rs11830157",
        "rs4773144",
        "rs9319428",
        "rs2895811",
        "rs3825807",
        "rs17514846",
        "rs56062135",
        "rs216172",
        "rs12936587",
        "rs46522",
        "rs116843064",
        "rs1122608",
        "rs2075650",
        "rs9982601"
    ]

    funcoes.consulta_frequencia_snp(snps)
    #funcoes.calcula_prs_pessoa('CLUB002606')
    #funcoes.calcula_prs_caracteristica('insonia')
    #funcoes.temp_calcula_tudo()
    #funcoes.compatibilidade()

    def plota_grafico(media, desvio_padrao, prs_x):

        x = np.arange(0, 100, 0.1)
        y = norm.pdf(x, media, desvio_padrao)
        prs_y = norm.pdf(prs_x, media, desvio_padrao)

        ax = plt.subplot(111)
        ax.plot(x, y)
        ax.set_title('Curva normal de Demência')
        ax.set_xlabel('PRS')

        ax.axvline(x=media, color='black', linestyle = '--', label = 'Média')
        ax.set_yticks([])
        ax.spines[['right', 'left', 'top']].set_visible(False)

        ax.scatter(prs_x, prs_y, color = 'r', zorder = 3)
        ax.fill_between(x, y, where=(x <= prs_x), color='lightblue', alpha=0.3)
        plt.show()

    #plota_grafico(5.88, 9.12, 18.3)