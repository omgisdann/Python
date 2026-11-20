
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import datetime


qt_chamados_ja_registrados = 0 
class Cadastro_de_chamados:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Help!")
        self.janela.geometry("1200x700")

        # NOVO CHAMADO
        self.frame = tk.Frame(self.janela, width=400, height=300, bg="white")
        self.frame.place(x=200, y=180)

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
        self.frame_chamados.place(x=660, y=180)

        self.canvas_chamados = tk.Canvas(self.frame_chamados, width=400, height=30, bg="#174B78", highlightthickness=0)
        self.canvas_chamados.place(x=0, y=0)
        self.canvas_chamados.create_text(200, 15, text="Pesquisar Chamados Recentes", fill="white", font=("Arial", 11, "bold"), anchor="center")

        self.id_chamado = tk.Label(self.frame_chamados, background="#FFFFFF", text="ID do Chamado:")
        self.id_chamado.place(x=0, y=40)

        self.entrada_id_chamado = tk.Entry(self.frame_chamados, width=17)
        self.entrada_id_chamado.place(x=180, y=40)

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

        # BARRA LATERAL
        self.barra_lateral = tk.Frame(self.janela, width=150, height=528, bg="#174B78")
        self.barra_lateral.place(x=0, y=130)

        self.botao_novo_chamado = tk.Button(self.barra_lateral, text='Criar Chamado', bg="#174B78", fg="#FFFFFF", width=20, relief="flat", bd=0, activebackground="#174B78", activeforeground="white", highlightthickness=0, font=("Arial", 9, "bold"), command=self.acessar_novo_chamado)
        self.botao_novo_chamado.place(x=0, y=15)

        self.botao_pesquisar_chamada = tk.Button(self.barra_lateral, text='Pesquisar Chamado', bg="#174B78", fg="#FFFFFF", width=20, relief="flat", bd=0, activebackground="#174B78", activeforeground="white", highlightthickness=0, font=("Arial", 9, "bold"), command=self.procurar_chamado)
        self.botao_pesquisar_chamada.place(x=0, y=60)

        self.botao_chamadosregistrados = tk.Button(self.barra_lateral, text='Quantidade de chamados', bg="#174B78", fg="#FFFFFF", width=20, relief="flat", bd=0, activebackground="#174B78", activeforeground="white", highlightthickness=0, font=("Arial", 9, "bold"), command=self.quantidade_chamados)
        self.botao_chamadosregistrados.place(x=3, y=105)

        self.central_de_consultas = tk.Button(self.barra_lateral, text='Central de Consultas', bg="#174B78", fg="#FFFFFF", width=20, relief="flat", bd=0, activebackground="#174B78", activeforeground="white", highlightthickness=0, font=("Arial", 9, "bold"), command=self.central_de_consultas)
        self.central_de_consultas.place(x=0, y=150)

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
                id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        global qt_chamados_ja_registrados
        qt_chamados_ja_registrados +=1

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
        id_a_procurar = self.entrada_id_chamado.get()

        conexao = sqlite3.connect("sistemasp.db")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT *
            FROM chamados
            WHERE id = ?
        """, [id_a_procurar])

        dados = cursor.fetchall()
        conexao.close()

        if not dados:
            print("Nenhum chamado encontrado!")

            if hasattr(self, "aviso"):
                self.aviso.destroy()

            self.aviso = tk.Label(self.frame_chamados, background="#FF0707", text="Chamado Não Encontrado!")
            self.aviso.place(x=125, y=120)

        else:
            for dado in dados:
                id_chamado = dado[0]
                nome = dado[1]
                departamento = dado[2]
                categoria = dado[3]
                prioridade = dado[4]
                observacao = dado[5]

            if hasattr(self, "aviso"):
                self.aviso.destroy()
                del self.aviso

            self.id_chamado.destroy()
            self.entrada_id_chamado.destroy()
            self.botao_pesquisar.destroy()

            # ID DO CHAMADO
            self.id_label = tk.Label(self.frame_chamados, background="#FFFFFF", text="ID:")
            self.id_label.place(x=0, y=40)

            self.id_resultado = tk.Label(self.frame_chamados, background="#66DB68", text=id_chamado)
            self.id_resultado.place(x=200, y=40)

            # NOME DO SOLICITANTE
            self.nome_label = tk.Label(self.frame_chamados, background="#FFFFFF", text="Nome Completo do Solicitante:")
            self.nome_label.place(x=0, y=65)

            self.nome = tk.Label(self.frame_chamados, background="#66DB68", text=nome)
            self.nome.place(x=200, y=65)

            # DEPARTAMENTO
            self.departamento_entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Departamento:")
            self.departamento_entrada.place(x=0, y=90)

            self.departamento_resposta = tk.Label(self.frame_chamados, background="#66DB68", text=departamento)
            self.departamento_resposta.place(x=200, y=90)

            # CATEGORIA
            self.categoria_Entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Categoria:")
            self.categoria_Entrada.place(x=0, y=115)

            self.categoria_Resposta = tk.Label(self.frame_chamados, background="#66DB68", text=categoria)
            self.categoria_Resposta.place(x=200, y=115)

            # PRIORIDADE
            self.prioridade_entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Prioridade:")
            self.prioridade_entrada.place(x=0, y=140)

            if prioridade == 1:
                self.prioridade_Resposta = tk.Label(self.frame_chamados, background="#66DB68", text="Alta")
            else:
                self.prioridade_Resposta = tk.Label(self.frame_chamados, background="#66DB68", text="Baixa")

            self.prioridade_Resposta.place(x=200, y=140)

            # OBSERVAÇÃO
            self.observacao_entrada = tk.Label(self.frame_chamados, background="#FFFFFF", text="Observação:")
            self.observacao_entrada.place(x=0, y=165)

            self.observacao_resposta = tk.Label(self.frame_chamados, background="#FFFFFF", text=observacao, wraplength=380, justify="left", anchor="nw")
            self.observacao_resposta.place(x=0, y=190, width=390)

            self.botao_nova_pesquisa = tk.Button(self.frame_chamados, text="Pesquisar outro chamado", background="#56CFEB", command=self.nova_pesquisa)
            self.botao_nova_pesquisa.place(x=120, y=265)

    def nova_pesquisa(self):
        self.id_label.destroy()
        self.id_resultado.destroy()
        self.nome_label.destroy()
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

        self.id_chamado = tk.Label(self.frame_chamados, background="#FFFFFF", text="ID do Chamado:")
        self.id_chamado.place(x=0, y=40)

        self.entrada_id_chamado = tk.Entry(self.frame_chamados, width=17)
        self.entrada_id_chamado.place(x=180, y=40)

        self.botao_pesquisar = tk.Button(self.frame_chamados, text="Pesquisar", background="#FFFFFF", foreground="#050404", width=10, command=self.realizar_pesquisa)
        self.botao_pesquisar.place(x=295, y=40)

        self.entrada_id_chamado.focus()
            
    def acessar_novo_chamado(self):
        self.frame.lift()
        self.entrada_nome.focus_set()


    def procurar_chamado(self):
        self.frame.lift()
        self.entrada_id_chamado.focus_set()


    def quantidade_chamados(self):
        nova = tk.Toplevel(self.janela)
        nova.geometry("300x150")
        primeiro = tk.Label(nova, text="Quantidade de chamados já registrados:")
        primeiro.place(x=0, y=0)
        segundo = tk.Label(nova, text=qt_chamados_ja_registrados, font=("Arial", 20))
        segundo.place(x=140, y=50)

        largura_janela = 300
        altura_janela = 150
        largura_tela = nova.winfo_screenwidth()
        altura_tela = nova.winfo_screenheight()
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        nova.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")


    def central_de_consultas(self):
        self.segunda_janela = tk.Toplevel(self.janela)
        self.segunda_janela.geometry("300x150")
        self.segunda_janela.title("Central de Consultas")
        botao_departamento = tk.Button(self.segunda_janela, text="Consultas por Departamentos", background="#FFFFFF", foreground="#050404", width=30, command=self.pg_inicial_departamentos)
        botao_departamento.place(x=40, y=0)

        botao_categoria = tk.Button(self.segunda_janela, text="Consultas por Categoria", background="#FFFFFF", foreground="#050404", width=30, command=self.pg_inicial_categorias)
        botao_categoria.place(x=40, y=45)

        largura_janela = 300
        altura_janela = 150
        largura_tela = self.segunda_janela.winfo_screenwidth()
        altura_tela = self.segunda_janela.winfo_screenheight()
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        self.segunda_janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")


    def pg_inicial_departamentos(self):
        self.janela_departamento = tk.Toplevel(self.segunda_janela)
        self.janela_departamento.title("Consulta Por Departamento")
        self.janela_departamento.geometry("800x700")
        label_departamento = tk.Label(self.janela_departamento, text='Digite o Nome do Departamento desejado:')
        label_departamento.place(x=400, y=90, anchor="center")
        self.nomedepartamento = tk.Entry(self.janela_departamento, width=40)
        self.nomedepartamento.place(x=400, y=140, anchor="center")
        botao_confirmar = tk.Button(self.janela_departamento, text="Consultar", command=self.select_departamentos)
        botao_confirmar.place(x=400, y=185, anchor="center")


    def pg_inicial_categorias(self):
        self.janela_categorias = tk.Toplevel(self.segunda_janela)
        self.janela_categorias.title("Consulta Por Categorias")
        self.janela_categorias.geometry("800x700")
        label_categoria = tk.Label(self.janela_categorias, text='Digite o Nome da Categoria desejada:')
        label_categoria.place(x=400, y=90, anchor="center")
        self.nomedacategoria = tk.Entry(self.janela_categorias, width=40)
        self.nomedacategoria.place(x=400, y=140, anchor="center")
        botao_confirmar = tk.Button(self.janela_categorias, text="Consultar", command=self.select_categoria)
        botao_confirmar.place(x=400, y=185, anchor="center")

    def select_departamentos(self):
        conexao = sqlite3.connect("sistemasp.db")   
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT *
        FROM chamados
        where departamento = ?
        """, [self.nomedepartamento.get()])



        dados = cursor.fetchall()
        conexao.close()

        if hasattr(self, "tabela_resultados"):
            self.tabela_resultados.destroy()

        self.tabela_resultados = ttk.Treeview(self.janela_departamento, columns=("ID", "Nome", "Departamento", "Categoria", "Prioridade", "Observação"), show="headings")

        self.tabela_resultados.heading("ID", text="ID")
        self.tabela_resultados.heading("Nome", text="Solicitante")
        self.tabela_resultados.heading("Departamento", text="Departamento")
        self.tabela_resultados.heading("Categoria", text="Categoria")
        self.tabela_resultados.heading("Prioridade", text="Prioridade")
        self.tabela_resultados.heading("Observação", text="Observação")

        self.tabela_resultados.column("ID", width=40, anchor="center")
        self.tabela_resultados.column("Nome", width=130)
        self.tabela_resultados.column("Departamento", width=110)
        self.tabela_resultados.column("Categoria", width=130)
        self.tabela_resultados.column("Prioridade", width=90, anchor="center")
        self.tabela_resultados.column("Observação", width=800)

        self.tabela_resultados.place(x=20, y=250, width=760, height=400)

        for dado in dados:
            prioridade = "Alta" if dado[4] == 1 else "Baixa"
            self.tabela_resultados.insert("", tk.END, values=(dado[0], dado[1], dado[2], dado[3], prioridade, dado[5]))
            
    def select_categoria(self):
        conexao = sqlite3.connect("sistemasp.db")   
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT *
        FROM chamados
        where categoria = ?
        """, [self.nomedacategoria.get()])



        dados = cursor.fetchall()
        conexao.close()

        if hasattr(self, "tabela_resultados"):
            self.tabela_resultados.destroy()

        self.tabela_resultados = ttk.Treeview(self.janela_categorias, columns=("ID", "Nome", "Departamento", "Categoria", "Prioridade", "Observação"), show="headings")

        self.tabela_resultados.heading("ID", text="ID")
        self.tabela_resultados.heading("Nome", text="Solicitante")
        self.tabela_resultados.heading("Departamento", text="Departamento")
        self.tabela_resultados.heading("Categoria", text="Categoria")
        self.tabela_resultados.heading("Prioridade", text="Prioridade")
        self.tabela_resultados.heading("Observação", text="Observação")

        self.tabela_resultados.column("ID", width=40, anchor="center")
        self.tabela_resultados.column("Nome", width=130)
        self.tabela_resultados.column("Departamento", width=110)
        self.tabela_resultados.column("Categoria", width=130)
        self.tabela_resultados.column("Prioridade", width=90, anchor="center")
        self.tabela_resultados.column("Observação", width=800)

        self.tabela_resultados.place(x=20, y=250, width=760, height=400)

        for dado in dados:
            prioridade = "Alta" if dado[4] == 1 else "Baixa"
            self.tabela_resultados.insert("", tk.END, values=(dado[0], dado[1], dado[2], dado[3], prioridade, dado[5]))
            

teste = Cadastro_de_chamados()
teste.janela.mainloop()
