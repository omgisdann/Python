import tkinter as tk
import webbrowser

#cada botao de determinado assunto que a pessoa clica abre uma aba com links que a pessoa pode estar acessando para estudar aquele assunto
class Programa:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("LETSTUDYT")
        self.janela.geometry("1000x700")

    def cabecalho(self):
        self.frame_cabecalho = tk.Frame(self.janela)
        self.frame_cabecalho.place(x=0, y=0, width=1000, height=100)
        canvas = tk.Canvas(self.frame_cabecalho,width=1000, height=100, bg="powder blue")
        canvas.pack()
        canvas.create_text(500, 50, text="LET STUDY TOGETHER", font=("Arial", 40))

        
    def corpo(self):
        self.frame_corpo = tk.Frame(self.janela, bg="white")
        self.frame_corpo.place(x=0, y=100, width=1000, height=600)
        self.botao_python = tk.Button(self.frame_corpo, text= 'Aprender Python', command=self.funcionalidade_py)
        self.botao_python.place(x=0, y=5)


    def funcionalidade_py(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Python")
        nova.geometry("300x500")
        tk.Label(nova, text="Esta é uma nova janela").pack()


    



teste = Programa()
teste.cabecalho()
teste.corpo()
teste.janela.mainloop()
        