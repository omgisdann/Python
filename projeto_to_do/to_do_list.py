import tkinter as tk


class Tarefa():
    tarefas_salvas = []
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("To-Do-List")
        self.janela.geometry("1000x500")
        self.texto_titulo = tk.Label(self.janela, text='TO DO LIST', background="#A5A4EE").place(x=450, y=0) #x movimenta pro lado, Y para baixo
        ####################################################### INICIO ######################################


        ############################################ ADICIONAR #############################################
        self.texto_addtrf = tk.Label(self.janela, text='Adicionar Tarefa').place(x=0, y=50) #x movimenta pro lado, Y para baixo
        self.caixa_addtrf = tk.Entry(self.janela, width=25)
        self.caixa_addtrf.place(x=0, y=70)
        self.botao_addtrf = tk.Button(self.janela, text= 'Confirmar', command=self.adicionando_tarefa).place(x=160, y=65)
        ####################################################################################################

        ##########################################Remover TAREFA#########################################
        self.texto_rmtrf = tk.Label(self.janela, text='Remover Tarefa').place(x=0, y=100)
        self.caixa_rmtrf = tk.Entry(self.janela, width=25)
        self.caixa_rmtrf.place(x=0, y=120)
        self.janela.mainloop()

    def adicionando_tarefa(self):
        Tarefa.tarefas_salvas.extend([[self.caixa_addtrf.get()]])

        
        

    

teste = Tarefa()
teste.adicionando_tarefa()
