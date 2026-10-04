import tkinter as tk


class Tarefa():
    tarefas_salvas = []
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("To-Do-List")
        self.janela.geometry("1000x500")
        self.texto_titulo = tk.Label(self.janela, text='TO DO LIST', background="#A5A4EE").place(x=450, y=0) #x movimenta pro lado, Y para baixo
        ####################################################### INICIO #################################


        ############################################ ADICIONAR #########################################
        self.texto_addtrf = tk.Label(self.janela, text='Adicionar Tarefa').place(x=0, y=50) #x movimenta pro lado, Y para baixo
        self.caixa_addtrf = tk.Entry(self.janela, width=25)
        self.caixa_addtrf.place(x=0, y=70)
        self.botao_addtrf = tk.Button(self.janela, text= 'Confirmar', command=self.adicionando_tarefa).place(x=160, y=65)
        #################################################################################################


        ##########################################REMOVER TAREFA#########################################
        self.texto_rmtrf = tk.Label(self.janela, text='Remover Tarefa').place(x=0, y=100)
        self.caixa_rmtrf = tk.Entry(self.janela, width=25)
        self.caixa_rmtrf.place(x=0, y=120)
        self.botao_rmtrf = tk.Button(self.janela, text= 'Confirmar', command=self.remover_tarefa).place(x=160, y=115)
        ##################################################################################################



        ##########################################VISUALIZAR TAREFA#########################################
        self.texto_vsl = tk.Label(self.janela, text='Visualizar Tarefa').place(x=0, y=150)
        self.botao_vsl = tk.Button(self.janela, text= 'Confirmar', command=self.visualizar_tarefas).place(x=5, y=180)

        self.janela.mainloop()

    def adicionando_tarefa(self):
        registrador = 0
        global aviso_add
        if Tarefa.tarefas_salvas != []:
            for lista in Tarefa.tarefas_salvas:
                if lista == self.caixa_addtrf.get():
                    aviso_add.config(text='Tarefa já registrada')
                    registrador = 1
                    break
            if registrador == 0:
                Tarefa.tarefas_salvas.append(self.caixa_addtrf.get())
                aviso_add.config(text='Tarefa nova registrada')
        else:
            Tarefa.tarefas_salvas.append(self.caixa_addtrf.get())
            aviso_add = tk.Label(self.janela, text='Tarefa nova registrada')
            aviso_add.place(x=240, y=65)




    def remover_tarefa(self):
        for nome_individual in Tarefa.tarefas_salvas:
            if nome_individual == self.caixa_rmtrf.get():
                Tarefa.tarefas_salvas.remove(nome_individual)
                aviso_add = tk.Label(self.janela, text='Tarefa removida!').place(x=240, y=119)
                break
        else:
            aviso_add = tk.Label(self.janela, text='A tarefa não foi encontrada!').place(x=240, y=119)

                
        
    def visualizar_tarefas(self):
        print(Tarefa.tarefas_salvas)

    

teste = Tarefa()
teste.adicionando_tarefa()
teste.remover_tarefa()
