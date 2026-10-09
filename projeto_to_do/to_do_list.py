import tkinter as tk
import random

class Tarefa():
    tarefas_salvas = []
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("To-Do-List")
        self.janela.geometry("1000x500")
        self.texto_titulo = tk.Label(self.janela, text='TO DO LIST', foreground="#1B1BB9").place(x=460, y=0) #x movimenta pro lado, Y para baixo
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
        ####################################################################################################



        ##########################################VISUALIZAR TAREFA#########################################
        self.texto_vsl = tk.Label(self.janela, text='Visualizar todas Tarefas').place(x=0, y=155)
        self.botao_vsl = tk.Button(self.janela, text= 'Visualizar', command=self.visualizar_tarefas).place(x=5, y=180)

        #########################################RANDOM TO DO ##############################################
        self.texto_rdm = tk.Label(self.janela, text='Gerador de tarefa aleatória').place(x=0, y=210)
        self.botao_rdm = tk.Button(self.janela, text= 'Gerar Tarefa Aleatória', command=self.gerar_tarefa_aleatoria).place(x=5, y=237)

        #########################################CONTAR OS TO DO'S #########################################
        self.texto_rdm = tk.Label(self.janela, text='Quantidade de tarefas').place(x=0, y=270)
        self.botao_rdm = tk.Button(self.janela, text= 'Visualizar', command=self.quantidade_tarefas).place(x=5, y=294)

        ##########################################MARCAR COMO CONCLUIDA#####################################

        self.texto_tc = tk.Label(self.janela, text='Marcar Tarefa como concluida').place(x=0, y=330)
        self.caixa_tc = tk.Entry(self.janela, width=25)
        self.caixa_tc.place(x=170, y=330)
        self.botao_tc = tk.Button(self.janela, text= 'Confirmar', command=self.marcar_como_concluida).place(x=330, y=327)

        self.janela.mainloop()

    def adicionando_tarefa(self):
        registrador = 0
        global aviso_add
        if Tarefa.tarefas_salvas != []:
            for lista in Tarefa.tarefas_salvas:
                if lista == self.caixa_addtrf.get():
                    aviso_add.config(text='Tarefa já registrada!', fg='red')
                    registrador = 1
                    break
            if registrador == 0:
                Tarefa.tarefas_salvas.append(self.caixa_addtrf.get())
                aviso_add.config(text='Tarefa nova registrada!', fg='green')
        else:
            Tarefa.tarefas_salvas.append(self.caixa_addtrf.get())
            aviso_add = tk.Label(self.janela, text='Tarefa nova registrada!', fg='green')
            aviso_add.place(x=240, y=65)




    def remover_tarefa(self):
        '''caso alguma tarefa tenha sido publicada errada, essa função servirá para apagar'''
        for nome_individual in Tarefa.tarefas_salvas:
            if nome_individual == self.caixa_rmtrf.get():
                Tarefa.tarefas_salvas.remove(nome_individual)
                aviso_add = tk.Label(self.janela, text='Tarefa removida!', fg='green').place(x=240, y=119)
                break
        else:
            aviso_add = tk.Label(self.janela, text='A tarefa não foi encontrada!', fg='red').place(x=240, y=119)

                
        
    def visualizar_tarefas(self):
        if Tarefa.tarefas_salvas != []:
            nova = tk.Toplevel(self.janela)
            nova.title("Visualizar Tarefas")
            nova.geometry("1000x500")
            tk.Label(nova, text=f"Tarefas disponiveis: {Tarefa.tarefas_salvas}").place(x=0, y=0)
        else:
            tk.Label(self.janela, text=f"Nenhuma tarefa a visualizar!", fg='red').place(x=80, y=180)

           
            

    def gerar_tarefa_aleatoria(self):
        if Tarefa.tarefas_salvas != []:
            Tarefa.tarefas_salvas = random.choice(Tarefa.tarefas_salvas)
            nova = tk.Toplevel(self.janela)
            nova.title("Tarefa Aleatória")
            nova.geometry("300x200")
            tk.Label(nova, text=f"A tarefa escolhida foi: {self.tarefa_escolhida}").pack()
        else:
            self.mensagem = tk.Label(self.janela, text='Não há tarefas!', fg='red').place(x=90, y=240)


    def quantidade_tarefas(self):
        if Tarefa.tarefas_salvas != []:
            quantidade = len(Tarefa.tarefas_salvas)
            self_mensagem = tk.Label(self.janela, text=f'{quantidade} tarefas')
            self_mensagem.place(x=70, y=295)
        else:
            self_mensagem = tk.Label(self.janela, text='Não há tarefas para visualizar!', fg='red')
            self_mensagem.place(x=70, y=295)
            self_mensagem.config(self.janela, text='Não há tarefas para visualizar!', fg='red').place(x=70, y=295)



    def marcar_como_concluida(self):
        resposta = self.caixa_tc.get()
        registrador = 0
        if Tarefa.tarefas_salvas != []:
            for tarefa in Tarefa.tarefas_salvas:
                if tarefa == resposta:
                    Tarefa.tarefas_salvas.remove(tarefa)
                    try:
                        self.texto_tc.config(text='Tarefa concluída!', fg='green')
                    except:
                        self.texto_tc = tk.Label(self.janela, text='Tarefa concluída!', fg='green')
                        self.texto_tc.place(x=410, y=330)
                    registrador +=1
                    break
            if registrador == 0:
                try:
                    self.texto_tc.config(text='Tarefa não encontrada!', fg='red')
                except:
                    self.texto_tc = tk.Label(self.janela, text='Tarefa não encontrada!', fg='red')
                    self.texto_tc.place(x=410, y=330)
        else:
            try:
                self.texto_tc.config(text='Não há tarefas!', fg='red')
            except:
                try:
                    self.texto_tc.config(text='Não há tarefas!', fg='red')
                except AttributeError:
                    self.texto_tc = tk.Label(self.janela, text='Não há tarefas!', fg='red')
                    self.texto_tc.place(x=410, y=330)




teste = Tarefa()
teste.adicionando_tarefa()