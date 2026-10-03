import tkinter as tk
import time
from tkinter import ttk



class Conversor:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("600x320")
        self.mensagem_inicial = tk.Label(self.janela, text="BEM VINDO AO CONVERSOR DE MOEDAS!").place(x=180, y=10)
        self.mensagem_origem = tk.Label(self.janela, text="Moeda Origem:").place(x=10, y=70) #o y faz descer o x faz ir pro lado
        self.caixa_origem = ttk.Combobox(self.janela, values=("BRL", "USD")).place(x=8, y=95)
        self.mensagem_destino = tk.Label(self.janela, text="Moeda Destino:").place(x=30, y=70)
        self.janela.mainloop()



teste = Conversor()