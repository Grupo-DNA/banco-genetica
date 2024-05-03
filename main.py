from recursos import funcoes

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

if __name__ == '__main__':

    funcoes.insere_dados()

    snps = []

    #funcoes.consulta_frequencia_snp(snps)
    #funcoes.calcula_prs_pessoa('CLUB002606')
    #funcoes.calcula_prs_caracteristica('acne')
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