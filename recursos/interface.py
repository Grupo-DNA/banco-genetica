import tkinter as tk
from tkinter import filedialog

# ===== PERGUNTA PATH DIRETORIO
def pergunta_diretorio():
    path = filedialog.askdirectory()
    return path

# ===== CRIA JANELA BASE
def cria_janela(resolucao: str):
    # Cria uma janela nova
    janela = tk.Tk()
    # Da um titulo para a janela
    janela.title("Janela TESTE")
    # Define a resolução da janela
    janela.geometry(resolucao)
    # Fixa a resolução da janela
    janela.resizable(False, False)

    return janela

# ===== CONFIGURA A JANELA DE PROGRESSBAR
def barra_de_progresso(janela: tk):

    # Cria label
    label = tk.Label(janela, text='0/0')
    label.pack()

    # Cria barra de progresso
    progress_bar = ttk.Progressbar(janela, orient="horizontal", length=500, mode="determinate")
    progress_bar.pack()
    progress_bar["value"] = 0
