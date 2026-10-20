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

        self.botao_java = tk.Button(self.frame_corpo, text='Aprender Java', command=self.funcionalidade_java)
        self.botao_java.place(x=0, y=35)

        self.botao_js = tk.Button(self.frame_corpo, text='Aprender JavaScript')
        self.botao_js.place(x=0, y=65)

    def funcionalidade_py(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Python")
        nova.geometry("600x400")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        link_guanabara = tk.Button(nova, background="#5BE36F",text="Professor Guanabara", command=lambda: webbrowser.open('https://www.youtube.com/@cursoemvideo'))
        link_guanabara.place(x=0, y=20)

        link_hashtag = tk.Button(nova, background="#5BE36F",text="HashTag Treinamentos", command=lambda: webbrowser.open('https://www.youtube.com/c/HashtagTreinamentos/videos'))
        link_hashtag.place(x=0, y=50)

        link_dunossauro = tk.Button(nova, background="#5BE36F",text="Dunossauro", command=lambda: webbrowser.open('https://www.youtube.com/@Dunossauro'))
        link_dunossauro.place(x=0, y=80)

        link_otavio = tk.Button(nova, background="#5BE36F",text="Otávio Miranda", command=lambda: webbrowser.open('https://www.youtube.com/@OtavioMiranda'))
        link_otavio.place(x=0, y=110)

        link_boson = tk.Button(nova, background="#5BE36F",text="Boson Treinamentos", command=lambda: webbrowser.open('https://www.youtube.com/@bosontreinamentos'))
        link_boson.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#657CD6",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        link_exercism = tk.Button(nova, background="#657CD6",text="Exercism", command=lambda: webbrowser.open('https://exercism.org/pt-BR'))
        link_exercism.place(x=542, y=50)

        link_codeacademy = tk.Button(nova, background="#657CD6",text="Code Academy", command=lambda: webbrowser.open('https://www.codecademy.com/learn/welcome-to-codecademy'))
        link_codeacademy.place(x=507, y=80)

        linkLearnPython = tk.Button(nova, background="#657CD6",text="Learn Python.org", command=lambda: webbrowser.open('https://learnpython.org/'))
        linkLearnPython.place(x=497, y=110)
        
        link_freecodecamp = tk.Button(nova, background="#657CD6",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=140)

        mensagem_traducao = tk.Label(nova, background="#FB0202", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=370)
        print("Olá mundo")
    
    def funcionalidade_java(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Java")
        nova.geometry("600x400")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        link_guanabara = tk.Button(nova, background="#5BE36F",text="Professor Guanabara", command=lambda: webbrowser.open('https://www.youtube.com/@cursoemvideo'))
        link_guanabara.place(x=0, y=20)
        
        link_loiane= tk.Button(nova, background="#5BE36F",text="Loiane Groner", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=LnORjqZUMIQ&t=1s'))
        link_loiane.place(x=0, y=50)
        
        link_dev_dojo = tk.Button(nova, background="#5BE36F",text="Dev Dojo", command=lambda: webbrowser.open('https://www.youtube.com/@DevDojoBrasil'))
        link_dev_dojo.place(x=0, y=80)
        
        link_FernandaKipper = tk.Button(nova, background="#5BE36F",text="Fernanda Kipper", command=lambda: webbrowser.open('https://www.youtube.com/@kipperdev'))
        link_FernandaKipper.place(x=0, y=110)
        
        link_academiadosdev = tk.Button(nova, background="#5BE36F",text="Academia dos Dev", command=lambda: webbrowser.open('https://www.youtube.com/@AcademiadosDevs'))
        link_academiadosdev.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)
    
        link_udemy = tk.Button(nova, background="#657CD6",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)
    
        link_programiz = tk.Button(nova, background="#657CD6",text="Programiz", command=lambda: webbrowser.open('https://www.programiz.com/'))
        link_programiz.place(x=535, y=50)
    
        link_devjava = tk.Button(nova, background="#657CD6",text="Dev Java", command=lambda: webbrowser.open('https://dev.java/'))
        link_devjava.place(x=543, y=80)
    
        linkw3school = tk.Button(nova, background="#657CD6",text="W3 Schools", command=lambda: webbrowser.open('https://www.w3schools.com/'))
        linkw3school.place(x=527, y=110)
            
        link_freecodecamp = tk.Button(nova, background="#657CD6",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=140)

        mensagem_traducao = tk.Label(nova, background="#FB0202", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=370)

teste = Programa()
teste.cabecalho()
teste.corpo()
teste.janela.mainloop()
        