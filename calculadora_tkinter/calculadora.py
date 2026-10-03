import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("315x440")


tela_resultado = tk.Frame(janela, width=315, height=75, bg="#4946E5")
tela_resultado.grid(row=0, column=0)

tela_numeros = tk.Frame(janela, width=315, height=440)
tela_numeros.grid(row=1, column=0)


botao_9 = tk.Button(janela, text= '9').place(x=10,y=75,width=70, height=60)
botao_8 = tk.Button(janela, text= '8').place(x=85,y=75,width=70, height=60)
botao_7 = tk.Button(janela, text= '7').place(x=160,y=75,width=70, height=60)
botao_C = tk.Button(janela, text= 'C').place(x=235,y=75,width=70, height=60)

botao_6 = tk.Button(janela, text= '6').place(x=10,y=150,width=70, height=60)
botao_5 = tk.Button(janela, text= '5').place(x=85,y=150,width=70, height=60)
botao_4 = tk.Button(janela, text= '4').place(x=160,y=150,width=70, height=60)
botao_slash = tk.Button(janela, text= '/').place(x=235,y=150,width=70, height=60)

botao_3 = tk.Button(janela, text= '3').place(x=10,y=225,width=70, height=60)
botao_2= tk.Button(janela, text= '2').place(x=85,y=225,width=70, height=60)
botao_1= tk.Button(janela, text= '1').place(x=160,y=225,width=70, height=60)
botao_asterisco= tk.Button(janela, text= '*').place(x=235,y=225,width=70, height=60)


botao_00 = tk.Button(janela, text= '00').place(x=10,y=300,width=70, height=60)
botao_0 = tk.Button(janela, text= '0').place(x=85,y=300,width=70, height=60)
botao_ponto = tk.Button(janela, text= '.').place(x=160,y=300,width=70, height=60)
botao_subtracao = tk.Button(janela, text= '-').place(x=235,y=300,width=70, height=60)

botao_porcentagem = tk.Button(janela, text= '%').place(x=10, y=375, width = 70, height = 60)
botao_del = tk.Button(janela, text= 'DEL').place(x=85, y= 375, width = 70, height = 60)
botao_igual = tk.Button(janela, text= '=').place(x=160, y= 375, width = 70, height = 60)
botao_mais = tk.Button(janela, text= '+').place(x=235, y= 375, width = 70, height = 60)

janela.mainloop()