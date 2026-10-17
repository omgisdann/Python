import tkinter as tk
from tkinter import messagebox

class Perguntas:
    acertos = 0
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Quiz")
        self.janela.geometry("800x500")
        self.botao = tk.Button(self.janela, text='Confirmar', background="#E01919", command=self.submit, font=("Arial", 15, "bold"))
        self.botao.place(x=330, y=330)


    def Questao(self):
        self.var_opcao1 = tk.StringVar(value="")  
        self.question1 = tk.Label(self.janela, text='Qual a capital do Brasil?', foreground="#0A1FBB", font=("Arial", 30, "bold"))
        self.question1.place(x=160, y=0)
        self.first_q_rbottom  = tk.Radiobutton(self.janela, text='Rio de Janeiro', variable=self.var_opcao1, value= 'rio', font=("Arial", 10, "bold"))
        self.first_q_rbottom.place(x=0, y=80)
        self.second_q_rbottom = tk.Radiobutton(self.janela, text='Brasília', variable=self.var_opcao1, value='brasilia', font=("Arial", 10, "bold"))
        self.second_q_rbottom.place(x=0, y=110)
        self.third_q_rbottom  = tk.Radiobutton(self.janela, text='São Paulo', variable=self.var_opcao1, value='sao paulo', font=("Arial", 10, "bold"))
        self.third_q_rbottom.place(x=0, y=140)
        self.fourth_q_rbottom = tk.Radiobutton(self.janela, text='Ceará', variable=self.var_opcao1, value='ceara', font=("Arial", 10, "bold"))
        self.fourth_q_rbottom.place(x=0, y=170)
        

    def submit(self):
        if self.var_opcao1.get() == 'brasilia':
            Perguntas.acertos +=1
            self.msg = tk.Label(self.janela, text='Você acertou!', foreground="#09A70F", font=("Arial", 8 , "bold"))
            self.msg.place(x=345, y=300)
            self.var_opcao2 = tk.StringVar(value="")
            self.question1.config(text= "Qual o maior deserto do mundo?")
            self.botao.config(text= 'Confirmar', command=self.submit2)
            self.question1.place(x=110, y=0)
            self.first_q_rbottom.config(text='Saara',  value='saara',variable=self.var_opcao2)
            self.second_q_rbottom.config(text='Kalahari', value='kalahari', variable=self.var_opcao2)
            self.third_q_rbottom.config(text='Danakil', value='danakil', variable=self.var_opcao2)
            self.fourth_q_rbottom.config(text='Chalbi', value='chalbi', variable=self.var_opcao2)
        else:
            messagebox.showinfo('Quantidade de acertos', f"Quantidade de acertos:{Perguntas.acertos}")
            self.janela.destroy()
            


    def submit2(self):
        if self.var_opcao2.get() == 'saara':
            Perguntas.acertos+=1
            self.msg.config(text='Você acertou!', foreground="#09A70F", font=("Arial", 8 , "bold"))
            self.msg.place(x=345, y=300)
        else:
            messagebox.showinfo('Quantidade de acertos', f"Quantidade de acertos:{Perguntas.acertos}")
            self.janela.destroy()




teste = Perguntas()
teste.Questao()
teste.janela.mainloop()