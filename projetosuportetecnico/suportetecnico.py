
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import datetime

class Cadastro_de_chamados:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Help!")
        self.janela.geometry("1200x700")

        # NOVO CHAMADO
        self.frame = tk.Frame(self.janela, width=400, height=300, bg="white")
        self.frame.place(x=140, y=180)

        self.canvas = tk.Canvas(self.frame, width=400, height=30, bg="#174B78", highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(200, 15, text="Novo Chamado", fill="white", font=("Arial", 11, "bold"), anchor="center")

        self.nome_solicitante = tk.Label(self.frame, background="#FFFFFF", text="Nome Completo do Solicitante:")
        self.nome_solicitante.place(x=0, y=40)
        self.entrada_nome = tk.Entry(self.frame, width=23)
        self.entrada_nome.place(x=180, y=40)

        self.departamento = tk.Label(self.frame, background="#FFFFFF", text="Departamento:")
        self.departamento.place(x=0, y=65)
        self.entrada_departamento = ttk.Combobox(self.frame, values=("Administrativo", "Financeiro", "Recursos Humanos", "Comercial", "Marketing", "TI", "Operacional", "Jurídico", "Outros"), state="readonly", width=20)
        self.entrada_departamento.place(x=120, y=65)

        self.categoria = tk.Label(self.frame, background="#FFFFFF", text="Categoria:")
        self.categoria.place(x=0, y=90)
        self.entrada_categoria = ttk.Combobox(self.frame, values=("Hardware", "Software", "Rede/Internet", "Acesso e Permissões", "Impressoras e Periféricos", "Telefonia", "Outros"), state="readonly")
        self.entrada_categoria.place(x=120, y=90)

        self.prioridade = tk.Label(self.frame, background="#FFFFFF", text="Prioridade:")
        self.prioridade.place(x=0, y=115)
        self.prioridade_teste = tk.BooleanVar()
        self.checkbox_prioridade = tk.Checkbutton(self.frame, text="Alta prioridade", variable=self.prioridade_teste, width=16)
        self.checkbox_prioridade.place(x=120, y=115)

        self.descricao_problema = tk.Label(self.frame, background="#FFFFFF", text="Descrição do Problema:")
        self.descricao_problema.place(x=0, y=140)
        self.entrada_descricao = tk.Text(self.frame, width=48, height=3, wrap="word")
        self.entrada_descricao.place(x=0, y=160)

        self.botao_cadastrar = tk.Button(self.frame, text="Cadastrar Chamado", background="#56CFEB", command=self.informacoes)
        self.botao_cadastrar.place(x=130, y=250)

        self.botao_limpar = tk.Button(self.frame, text="Limpar", background="#CD4444", command=self.apagar)
        self.botao_limpar.place(x=265, y=250)

        # CABEÇALHO
        self.cabecalho = tk.Frame(self.janela, width=1200, height=130, bg="#174B78")
        self.cabecalho.place(x=0, y=0)

        self.titulo = tk.Label(self.cabecalho, text="Help!", font=("Arial", 30, "bold"), fg="white", bg="#174B78")
        self.titulo.place(x=50, y=20)

        self.subtitulo = tk.Label(self.cabecalho, text="Suporte Técnico | Sistema de Gerenciamento de Chamados", font=("Arial", 12), fg="white", bg="#174B78")
        self.subtitulo.place(x=52, y=75)

        # VISUALIZAÇÃO E PESQUISA DE DADOS
        self.frame_chamados = tk.Frame(self.janela, width=400, height=300, bg="white")
        self.frame_chamados.place(x=600, y=180)

        self.canvas_chamados = tk.Canvas(self.frame_chamados, width=400, height=30, bg="#174B78", highlightthickness=0)
        self.canvas_chamados.place(x=0, y=0)
        self.canvas_chamados.create_text(200, 15, text="Pesquisar Chamados Recentes", fill="white", font=("Arial", 11, "bold"), anchor="center")

        self.nome_solicitante_chamados = tk.Label(self.frame_chamados, background="#FFFFFF", text="Nome Completo do Solicitante:")
        self.nome_solicitante_chamados.place(x=0, y=40)

        self.entrada_nome_chamados = tk.Entry(self.frame_chamados, width=17)
        self.entrada_nome_chamados.place(x=180, y=40)

        self.botao_pesquisar = tk.Button(self.frame_chamados, text="Pesquisar", background="#FFFFFF", foreground="#050404", width=10, command=self.realizar_pesquisa)
        self.botao_pesquisar.place(x=295, y=40)

        # RODAPÉ
        self.rodape = tk.Frame(self.janela, width=1200, height=42, bg="#174B78")
        self.rodape.place(x=0, y=658)

        self.versao = tk.Label(self.rodape, text="Help! | Versão 1.0", font=("Arial", 9), fg="white", bg="#174B78")
        self.versao.place(x=25, y=12)

        self.estatisticas = tk.Label(self.rodape, text="Estatísticas: Em desenvolvimento", font=("Arial", 9), fg="white", bg="#174B78")
        self.estatisticas.place(x=220, y=12)

        self.data_hora = tk.Label(self.rodape, text="", font=("Arial", 9), fg="white", bg="#174B78")
        self.data_hora.place(x=500, y=12)

        try:
            conexao = sqlite3.connect("sistemasp.db")
            conexao.close()
            status_banco = "Banco de dados: Conectado"
            cor_status = "#66DB68"
        except sqlite3.Error:
            status_banco = "Banco de dados: Desconectado"
            cor_status = "#FF5555"

        self.status_banco = tk.Label(self.rodape, text=status_banco, font=("Arial", 9, "bold"), fg=cor_status, bg="#174B78")
        self.status_banco.place(x=900, y=12)

        def atualizar_horario():
            horario_atual = datetime.datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
            self.data_hora.config(text=horario_atual)
            self.janela.after(1000, atualizar_horario)

        atualizar_horario()

    def informacoes(self):
        nome = self.entrada_nome.get()
        departamento = self.entrada_departamento.get()
        categoria = self.entrada_categoria.get()
        prioridade = self.prioridade_teste.get()
        descricao = self.entrada_descricao.get("1.0", "end-1c")

        conexao = sqlite3.connect("sistemasp.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chamados(
                nome TEXT,
                departamento TEXT,
                categoria TEXT,
                prioridade INTEGER,
                descricao TEXT
            )
        """)

        cursor.execute("""
            INSERT INTO chamados(nome, departamento, categoria, prioridade, descricao)
            VALUES(?,?,?,?,?)
        """, (nome, departamento, categoria, prioridade, descricao))

        conexao.commit()
        messagebox.showinfo("Conclusão", "Chamado Cadastrado com Sucesso!")

        self.entrada_nome.delete(0, tk.END)
        self.entrada_departamento.set("")
        self.entrada_categoria.set("")
        self.prioridade_teste.set(False)
        self.entrada_descricao.delete("1.0", tk.END)

        conexao.close()

    def apagar(self):
        self.entrada_nome.delete(0, tk.END)
        self.entrada_departamento.set("")
        self.entrada_categoria.set("")
        self.prioridade_teste.set(False)
        self.entrada_descricao.delete("1.0", tk.END)

    def realizar_pesquisa(self):
        nome_a_procurar = self.entrada_nome_chamados.get()

        conexao = sqlite3.connect("sistemasp.db")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT *
            FROM chamados
            WHERE nome = ?
        """, [nome_a_procurar])

        dados = cursor.fetchall()

        if not dados:
            print("Nenhum chamado encontrado!")

            self.aviso = tk.Label(self.frame_chamados, background="#FF0707", text="Usuário Não Encontrado!")
            self.aviso.place(x=125, y=120)

        else:
            for dado in dados:
                nome = dado[0]
                departamento = dado[1]
                categoria = dado[2]
                prioridade = dado[3]
                observacao = dado[4]

            try:
                self.aviso.destroy()
                del self.aviso

                self.entrada_nome_chamados.destroy()
                self.botao_pesquisar.destroy()

                self.nome = tk.Label(self.frame_chamados, background="#66DB68", text=nome)
                self.nome.place(x=200, y=40)

                self.departamento_entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Departamento:")
                self.departamento_entrada.place(x=0, y=65)

                self.departamento_resposta = tk.Label(self.frame_chamados, background="#66DB68", text=departamento)
                self.departamento_resposta.place(x=200, y=65)

                self.categoria_Entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Categoria:")
                self.categoria_Entrada.place(x=0, y=90)

                self.categoria_Resposta = tk.Label(self.frame_chamados, background="#66DB68", text=categoria)
                self.categoria_Resposta.place(x=200, y=90)

                self.prioridade_entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Prioridade:")
                self.prioridade_entrada.place(x=0, y=115)

                if prioridade == 1:
                    self.prioridade_Resposta = tk.Label(self.frame_chamados, background="#66DB68", text="Alta")
                else:
                    self.prioridade_Resposta = tk.Label(self.frame_chamados, background="#66DB68", text="Baixa")

                self.prioridade_Resposta.place(x=200, y=115)

                self.observacao_entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Observação:")
                self.observacao_entrada.place(x=0, y=140)

                self.observacao_resposta = tk.Label(self.frame_chamados, background="#FFFFFF", text=observacao, wraplength=380, justify="left", anchor="nw")
                self.observacao_resposta.place(x=0, y=165, width=390)

                self.botao_nova_pesquisa = tk.Button(self.frame_chamados, text="Pesquisar outro usuário", background="#56CFEB", command=self.nova_pesquisa)
                self.botao_nova_pesquisa.place(x=120, y=265)

            except AttributeError:
                self.entrada_nome_chamados.destroy()
                self.botao_pesquisar.destroy()

                self.nome = tk.Label(self.frame_chamados, background="#66DB68", text=nome)
                self.nome.place(x=200, y=40)

                self.departamento_entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Departamento:")
                self.departamento_entrada.place(x=0, y=65)

                self.departamento_resposta = tk.Label(self.frame_chamados, background="#66DB68", text=departamento)
                self.departamento_resposta.place(x=200, y=65)

                self.categoria_Entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Categoria:")
                self.categoria_Entrada.place(x=0, y=90)

                self.categoria_Resposta = tk.Label(self.frame_chamados, background="#66DB68", text=categoria)
                self.categoria_Resposta.place(x=200, y=90)

                self.prioridade_entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Prioridade:")
                self.prioridade_entrada.place(x=0, y=115)

                if prioridade == 1:
                    self.prioridade_Resposta = tk.Label(self.frame_chamados, background="#66DB68", text="Alta")
                else:
                    self.prioridade_Resposta = tk.Label(self.frame_chamados, background="#66DB68", text="Baixa")

                self.prioridade_Resposta.place(x=200, y=115)

                self.observacao_entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Observação:")
                self.observacao_entrada.place(x=0, y=140)

                self.observacao_resposta = tk.Label(self.frame_chamados, background="#FFFFFF", text=observacao, wraplength=380, justify="left", anchor="nw")
                self.observacao_resposta.place(x=0, y=165, width=390)

                self.botao_nova_pesquisa = tk.Button(self.frame_chamados, text="Pesquisar outro usuário", background="#56CFEB", command=self.nova_pesquisa)
                self.botao_nova_pesquisa.place(x=120, y=265)

        conexao.close()

    def nova_pesquisa(self):
        self.nome.destroy()
        self.departamento_entrada.destroy()
        self.departamento_resposta.destroy()
        self.categoria_Entrada.destroy()
        self.categoria_Resposta.destroy()
        self.prioridade_entrada.destroy()
        self.prioridade_Resposta.destroy()
        self.observacao_entrada.destroy()
        self.observacao_resposta.destroy()

        self.botao_nova_pesquisa.destroy()

        self.entrada_nome_chamados = tk.Entry(self.frame_chamados, width=17)
        self.entrada_nome_chamados.place(x=180, y=40)

        self.botao_pesquisar = tk.Button(self.frame_chamados, text="Pesquisar", background="#FFFFFF", foreground="#050404", width=10, command=self.realizar_pesquisa)
        self.botao_pesquisar.place(x=295, y=40)

        self.entrada_nome_chamados.focus()


teste = Cadastro_de_chamados()
teste.janela.mainloop()
