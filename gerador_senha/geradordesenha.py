import tkinter as tk
import hashlib
import random
import string
import sqlite3
import getpass
from tkinter import messagebox


janela = tk.Tk()
janela.title("Gerenciador de senhas")
janela.geometry("1200x500")

texto1 = tk.Label(janela, text='Usuário')
texto1.grid(row=0, column=0, sticky='e')

entrada1 = tk.Entry(janela, width=20)
entrada1.grid(row=0, column=1, padx=5, pady=5)

texto2 = tk.Label(janela, text='E-mail')
texto2.grid(row=1, column=0, sticky='e')

entrada2 = tk.Entry(janela, width=20)
entrada2.grid(row=1, column=1, padx=5, pady=5)

texto3 = tk.Label(janela, text='Senha')
texto3.grid(row=2, column=0, sticky='e')

entrada3 = tk.Entry(janela, width=20, show='*')
entrada3.grid(row=2, column=1, padx=5, pady=5)
global password
password = entrada3.get()


texto4 = tk.Label(janela, text='Procurar Usuário Específico')
texto4.grid(row=3, column=0, sticky='e')

entrada4 = tk.Entry(janela, width=20)
entrada4.grid(row=3, column=1, padx=5, pady=5)


texto_parte_exclusao = tk.Label(janela, text='Excluir Usuário')
texto_parte_exclusao.grid(row=4, column=0, sticky='e')

entrada_parte_exclusao = tk.Entry(janela, width=20)
entrada_parte_exclusao.grid(row=4, column=1, sticky='e', padx=5, pady=5)


texto_parte_visualizacao = tk.Label(janela, text= 'Visualizar todas as informações')
texto_parte_visualizacao.grid(row=9, column=0, sticky='e')

alteracao_cadastral = tk.Label(janela, text= 'Usuário para alterar senha')
alteracao_cadastral.grid(row=7, column=0, sticky='e')

entrada_alteracao = tk.Entry(janela, width=20)
entrada_alteracao.grid(row=7, column=1, sticky='e', padx=5, pady=5)

nova_senha = tk.Label(janela, text= 'Nova Senha')
nova_senha.grid(row=7, column=3, sticky='e')

entrada_senha = tk.Entry(janela, width=20)
entrada_senha.grid(row=7, column=4, sticky='e', padx=5, pady=5)


alteracao_cadastralemail = tk.Label(janela, text= 'Usuário para alterar email')
alteracao_cadastralemail.grid(row=8, column=0, sticky='e', padx=5, pady=5)

entrada_email = tk.Entry(janela, width=20)
entrada_email.grid(row=8, column=1, sticky='e', padx=5, pady=5)

novo_email = tk.Label(janela, text= 'Digite o novo email')
novo_email.grid(row=8, column=3, sticky='e', padx=5, pady=5)

novo_email_entrada = tk.Entry(janela, width=20)
novo_email_entrada.grid(row=8, column=4, sticky='e', padx=5, pady=5)

informacoes = []
def declaracao():
    global dados
    dados = {}
    try:
        conexao = sqlite3.connect("SQL.db")
        cursor = conexao.cursor()
        cursor.execute("""
        SELECT *
        FROM informacoesDOusuario
        WHERE usuario = ?
        """, [entrada1.get()])
        resultadousuario = cursor.fetchall()

        cursor.execute("""
        SELECT *
        FROM informacoesDOusuario
        WHERE email = ?
        """, [entrada2.get()])
        resultadoemail = cursor.fetchall()
        if resultadousuario == []:
            if resultadoemail == []:
                if entrada1.get():
                    dados['usuario'] = entrada1.get()
                    possibilidade = tk.Label(janela, text='USUÁRIO VÁLIDO!', fg='green')
                    possibilidade.grid(row=0, column=3, sticky='e')
                else:
                    possibilidade = tk.Label(janela, text='USUÁRIO inválido!', fg='red')
                    possibilidade.grid(row=0, column=3, sticky='e')
                    dados['usuario'] = '?'
                if entrada2.get():
                    dados['E-mail'] = entrada2.get()
                    possibilidade = tk.Label(janela, text='E-MAIL VÁLIDO!', fg='green')
                    possibilidade.grid(row=1, column=3, sticky='e')
                else:
                    possibilidade = tk.Label(janela, text='E-mail inválido!', fg='red')
                    possibilidade.grid(row=1, column=3, sticky='e')
                    dados['E-mail'] = '?'
                if entrada3.get():
                    dados['Senha'] = entrada3.get()
                    possibilidade = tk.Label(janela, text='SENHA VÁLIDA!', fg='green')
                    possibilidade.grid(row=2, column=5, sticky='e')
                else:
                    dados['Senha'] = password
                    possibilidade = tk.Label(janela, text='SENHA VÁLIDA GERADA AUTOMATICAMENTE!', fg='green')
                    possibilidade.grid(row=2, column=5, sticky='e')
                    if not password:
                        possibilidade = tk.Label(janela, text='Senha inválida!', fg='red')
                        possibilidade.grid(row=2, column=5, sticky='e')
                        dados['Senha'] = '?'


                try:
                    conexao = sqlite3.connect("SQL.db")
                    cursor = conexao.cursor()
                    cursor.execute("""
                    INSERT INTO informacoesDOusuario(usuario, email, senha)
                    VALUES(?,?,?)
                    """, (
                        dados['usuario'],
                        dados['E-mail'],
                        dados['Senha']
                        ))
                    conexao.commit()
                except:
                    conexao = sqlite3.connect("SQL.db")
                    cursor = conexao.cursor()
                    cursor.execute("""CREATE TABLE informacoesDOusuario(
                    id INTEGER PRIMARY KEY,
                    usuario TEXT,
                    email TEXT,
                    senha TEXT)
                    """)
                    
                    cursor.execute("""
                    INSERT INTO informacoesDOusuario(usuario, email, senha)
                    VALUES(?,?,?)
                    """, (
                    dados['usuario'],
                    dados['E-mail'],
                    dados['Senha']
                    ))
                    conexao.commit()
            else: 
                possibilidade = tk.Label(janela, text='Não é possível usar um email já existente!', fg='red')
                possibilidade.grid(row=1, column=3, sticky='e')
        else:
            possibilidade = tk.Label(janela, text='Não é possível cadastrar um usuario já existente!', fg='red')
            possibilidade.grid(row=0, column=3, sticky='e')
    except:
        if entrada1.get():
            dados['usuario'] = entrada1.get()
            possibilidade = tk.Label(janela, text='USUÁRIO VÁLIDO!', fg='green')
            possibilidade.grid(row=0, column=3, sticky='e')
        else:
            possibilidade = tk.Label(janela, text='USUÁRIO inválido!', fg='red')
            possibilidade.grid(row=0, column=3, sticky='e')
            dados['usuario'] = '?'
        if entrada2.get():
            dados['E-mail'] = entrada2.get()
            possibilidade = tk.Label(janela, text='E-MAIL VÁLIDO!', fg='green')
            possibilidade.grid(row=1, column=3, sticky='e')
        else:
            possibilidade = tk.Label(janela, text='E-MAIL inválido!', fg='red')
            possibilidade.grid(row=1, column=3, sticky='e')
            dados['E-mail'] = '?'
        if entrada3.get():
            dados['Senha'] = entrada3.get()
            possibilidade = tk.Label(janela, text='SENHA VÁLIDA!', fg='green')
            possibilidade.grid(row=2, column=5, sticky='e')
        else:
            dados['Senha'] = password
            possibilidade = tk.Label(janela, text='SENHA VÁLIDA GERADA AUTOMATICAMENTE!', fg='green')
            possibilidade.grid(row=2, column=5, sticky='e')
            if not password:
                possibilidade = tk.Label(janela, text='Senha inválida!', fg='red')
                possibilidade.grid(row=2, column=5, sticky='e')
                dados['Senha'] = '?'
            try:
                conexao = sqlite3.connect("SQL.db")
                cursor = conexao.cursor()
                cursor.execute("""
                INSERT INTO informacoesDOusuario(usuario, email, senha)
                VALUES(?,?,?)
                """, (
                dados['usuario'],
                dados['E-mail'],
                dados['Senha']
                ))
                conexao.commit()
            except:
                conexao = sqlite3.connect("SQL.db")
                cursor = conexao.cursor()
                cursor.execute("""CREATE TABLE informacoesDOusuario(
                id INTEGER PRIMARY KEY,
                usuario TEXT,
                email TEXT,
                senha TEXT)
                """)
                            
                cursor.execute("""
                INSERT INTO informacoesDOusuario(usuario, email, senha)
                VALUES(?,?,?)
                """, (
                dados['usuario'],
                dados['E-mail'],
                dados['Senha']
                ))
                conexao.commit()

def gerar_senha():
    '''irá gerar uma senha segura para substituir a senha criada pelo usuário'''
    global password
    caracteres = string.ascii_letters + string.digits + string.punctuation
    nova_senha = ''.join(random.choice(caracteres) for i in range(10))
    password = nova_senha
    
def copiar_senha():  
    janela.clipboard_clear()
    try:
        janela.clipboard_append(dados['Senha'])
        messagebox.showinfo("Success", f"Copied to clipboard: {dados['Senha']}")
    except NameError, KeyError:
        messagebox.showerror("ERRO", "Não foi criado nenhum cadastro E/OU o cadastro não foi confirmado!")

def procurar_usuario():
    '''Devolve um usuário específico'''
    lista = []
    dicionario = {}
    conexao = sqlite3.connect("SQL.db")
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT *
    FROM informacoesDOusuario
    WHERE usuario = ?
    """, [entrada4.get()])
    info = cursor.fetchall()
    nova = tk.Toplevel(janela)
    nova.title("Sites encontrados")
    nova.geometry("300x200")
    for informacao in info:
        dicionario['Id'] = informacao[0]
        dicionario['usuario'] = informacao[1]
        dicionario['Email'] = informacao[2]
        dicionario['Senha'] = informacao[3]
        lista.append(dicionario.copy())
    texto5 = tk.Label(nova, text=lista)
    texto5.grid(row=3, column=1, padx=5, pady=5)


 
def excluir_conta():
    '''irá remover a que tiver o mesmo nome do site'''
    conexao = sqlite3.connect("SQL.db")
    cursor = conexao.cursor()
    caso = tk.messagebox.askyesno('Confirmação', 'Deseja realizar a exclusão?')
    if caso == True:
        cursor.execute("""
        DELETE FROM informacoesDOusuario
        WHERE usuario = ?
        """, [entrada_parte_exclusao.get()])  
        textoaviso = tk.Label(janela, text='Usuário excluido!', fg='green')     
        textoaviso.grid(row=4, column=3, padx=5, pady=5) 
        conexao.commit()
    else:
        messagebox.showinfo('Confirmação', 'Nenhum cadastro foi excluido.')


def visualizar_informacoes():
    '''visualiza todas as contas'''
    dicionario = {}
    lista = []
    conexao = sqlite3.connect("SQL.db")
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT *
    FROM informacoesDOusuario
    """)
    info = cursor.fetchall()
    nova = tk.Toplevel(janela)
    nova.title("Todos os sites")
    nova.geometry("300x200")
    for informacao in info:
        dicionario['Id'] = informacao[0]
        dicionario['usuario'] = informacao[1]
        dicionario['Email'] = informacao[2]
        dicionario['Senha'] = informacao[3]
        lista.append(dicionario.copy())
    visualizar_tudo = tk.Label(nova, text=lista)
    visualizar_tudo.grid(row=3, column=1, padx=5, pady=5)


def cancelar():
    entrada1 = tk.Entry(janela, width=20)
    entrada1.grid(row=0, column=1, padx=5, pady=5)

    entrada2 = tk.Entry(janela, width=20)
    entrada2.grid(row=1, column=1, padx=5, pady=5)


    entrada3 = tk.Entry(janela, width=20)
    entrada3.grid(row=2, column=1, padx=5, pady=5)


def trocar_senha():
    '''Para realizar a troca, é necessário primeiro confirmar o nome de usuário,
    logo depois, inserir a nova senha e confirma-lá, antes de REALIZAR A TROCA.'''
    try:
        conexao = sqlite3.connect("SQL.db")
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE informacoesDOusuario
        SET senha = ?
        WHERE usuario = ?
        """, [senha, nome])
        conexao.commit()
    except:
        print("Confirme primeiro o nome do usuário, logo após, confirme também a nova senha.")


def confirmar_senha():
    global senha 
    senha = entrada_senha.get()



def confirmar_usuario():
    global nome 
    nome = entrada_alteracao.get()


def confirmar_email():
    global nome_email
    nome_email = entrada_email.get()


def confirmar_novo_email():
    global novo_email
    novo_email = novo_email_entrada.get()


def alterar_email():
    try:
        conexao = sqlite3.connect("SQL.db")
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE informacoesDOusuario
        SET email = ?
        WHERE usuario = ?
        """, [novo_email, nome_email])
        conexao.commit()
    except:
        print("Confirme primeiro o nome do usuário, logo após, confirme também a nova senha.")

inicio = tk.Button(janela, text= 'Confirmar', command=declaracao).grid(row=2, column=2, padx=5, pady=5)
copiarsenha = tk.Button(janela, text= 'Copiar senha', command=copiar_senha).grid(row=2, column=3, padx=5, pady=5)
senha_aleatoria = tk.Button(janela, text= 'Gerar senha', command=gerar_senha).grid(row=2, column=4, padx = 5, pady = 5)
procurar_usuari0 = tk.Button(janela, text= 'Procurar', command=procurar_usuario).grid(row=3, column=2, padx=5, pady=5) 
excluir = tk.Button(janela, text= 'Excluir', command=excluir_conta).grid(row=4, column=2, padx=5, pady=5) 
visualizar = tk.Button(janela, text= 'Conferir', command=visualizar_informacoes).grid(row=9, column=1, padx=5, pady=5) 
cancelar_cadastro = tk.Button(janela, text= 'Apagar', command=cancelar).grid(row=2, column=5, padx=5, pady=5) 
botao_senha = tk.Button(janela, text= 'Confirmar', command=confirmar_senha).grid(row=7, column=5, sticky='e', padx=5, pady=5) 
botao_usuario =  tk.Button(janela, text= 'Confirmar', command=confirmar_usuario).grid(row=7, column=2, sticky='e', padx=5, pady=5) 
realizar_troca =  tk.Button(janela, text= 'Realizar troca Senha', command=trocar_senha).grid(row=7, column=6,padx=5, pady=5, sticky='e') 
botao_email = tk.Button(janela, text= 'Confirmar', command=confirmar_email).grid(row=8, column=2,padx=5, pady=5, sticky='e') 
confirmar_novo_email = tk.Button(janela, text= 'Confirmar', command=confirmar_novo_email).grid(row=8, column=5,padx=5, pady=5, sticky='e') 
trocar_email = tk.Button(janela, text= 'Realizar Troca Email', command=alterar_email).grid(row=8, column=6, padx=5, pady=5, sticky='e') 
janela.mainloop()


