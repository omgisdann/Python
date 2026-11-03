import tkinter as tk
from tkinter import ttk
import sqlite3
import datetime

class Cadastro_de_chamados:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Help!")
        self.janela.geometry("1200x700")


        self.frame = tk.Frame(self.janela, width=400, height=300, bg="white")
        self.frame.place(x=195, y=286)

        self.canvas = tk.Canvas(self.frame,width=400,height=30,bg="#174B78",highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(200, 15, text="Novo Chamado", fill="white", font=("Arial", 11, "bold"), anchor="center")

        self.nome_solicitante = tk.Label(self.frame,background="#FFFFFF" ,text= 'Nome do Solicitante:')
        self.nome_solicitante.place(x=0, y=40)
        self.entrada_nome = tk.Entry(self.frame, width=23)
        self.entrada_nome.place(x=120, y=40)

        self.departamento = tk.Label(self.frame,background="#FFFFFF" ,text= 'Departamento:')
        self.departamento.place(x=0, y=65)
        self.entrada_departamento = ttk.Combobox(self.frame, values=("Administrativo", "Financeiro", "Recursos Humanos", "Comercial", "Marketing", "TI", "Operacional", "Jurídico", "Outros"), state="readonly", width=20)
        self.entrada_departamento.place(x=120, y=65)

        self.categoria = tk.Label(self.frame,background="#FFFFFF" ,text= 'Categoria:')
        self.categoria.place(x=0, y=90)
        self.entrada_categoria = ttk.Combobox(self.frame, values=("Hardware", "Software", "Rede/Internet", "Acesso e Permissões", "Impressoras e Periféricos", "Telefonia", "Outros"), state="readonly")
        self.entrada_categoria.place(x=120, y=90)


        self.prioridade = tk.Label(self.frame,background="#FFFFFF" ,text= 'Prioridade:')
        self.prioridade.place(x=0, y=115)
        self.prioridade_teste = tk.BooleanVar()
        self.checkbox_prioridade = tk.Checkbutton(self.frame, text="Alta prioridade", variable=self.prioridade_teste, width=16)
        self.checkbox_prioridade.place(x=120, y=115)


        self.descricao_problema = tk.Label(self.frame,background="#FFFFFF" ,text= 'Descrição do Problema:')
        self.descricao_problema.place(x=0, y=140)
        self.entrada_descricao = tk.Text(self.frame, width=48, height=3,wrap="word")
        self.entrada_descricao.place(x=0, y=160)


        self.botao_cadastrar = tk.Button(self.frame, text="Cadastrar Chamado", background="#56CFEB", command=self.informacoes)
        self.botao_cadastrar.place(x=100, y=250)

        self.botao_limpar = tk.Button(self.frame, text="Limpar", background="#CD4444")
        self.botao_limpar.place(x=230, y=250)   


    def informacoes(self):
        nome = self.entrada_nome.get()
        departamento = self.entrada_departamento.get()
        categoria = self.entrada_categoria.get()
        prioridade = self.prioridade_teste.get()
        descricao = self.entrada_descricao.get("1.0", "end-1c")
        #INSERIR ESSAS INFORMAÇÕES EM UM BANCO DE DADOS SQL

        
    

teste = Cadastro_de_chamados()
teste.janela.mainloop()
teste.informacoes()