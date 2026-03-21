print("=== JOGO DE ADIVINHAÇÃO ===")
import random
flag=True
contador=0
numero=random.randint(1,100)
while flag:
    usuario = int(input("digite um numero de 1 a 100 "))

    if usuario < numero:
        print('maior')
        contador+=1
    elif usuario > numero:
        print('menor')
        contador+=1
    else:
        contador+=1
        print(f"acertou! depois de {contador} tentativas.")
        flag=False
