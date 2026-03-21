print("Gerador de histórias aleatórias")

def criacao (nome,genero,caracteristicas):
    personagem={}
    personagem['nome']=nome
    personagem['genero']=genero
    personagem['caracteristicas']=caracteristicas
    return personagem


def castelo(personagem):
    contador=0
    print("você entrou no castelo, tente fugir antes que o dragão te devore!")
    import random
    numero_sorteado=random.randint(0,10)
    while contador <3:
        usuario = int ( input (" digite um numero  "))
        contador+=1
        if usuario == numero_sorteado:
            print(f"parabéns {personagem['nome']} , você acertou!")
            break
        elif usuario != numero_sorteado and contador != 3:
            print("tente novamente!")
        else:
            print("tempo esgotado!")
        

def natureza (personagem):
    print(f"olá {personagem['nome']}")
    usuario = input("para qual caminho você gostaria de seguir? " ).lower()
    if usuario == 'direita':
        print("você chegou na casa da senhorinha adelaide!")
        if personagem['caracteristicas'] == 'alto' or personagem['caracteristicas'] == 'forte':
            npc=input("Olá meu amigo, me chamo adelaide, você gostaria de pegar esse pote para mim? ").lower()
            if npc == 'sim':
                print("obrigado , como recompensa te guiarei até o fim da floresta")
            else:
                print("sem problemas, caro viajante.")
        else:
            print("porém, você não possui as condições para ajudar a adelaide")
    elif usuario == 'meio':
        print(f"{personagem['nome']} chegou no Óasis, apenas relaxe e espere o helicóptero chegar")
    else:
        print("CORRA! O LEÃO ESTÁ VINDO!!!")



while True:
    print("bem vindo ao gerador de histórias aleátorias!")
    inicio = input ("gostaria de criar seu personagem? " ).lower()

    if inicio == 'sim' :
        nome_personagem=input("digite o nome ")
        genero_personagem=input("digite o gênero ")
        caracteristica_personagem=input("digite as características ")
        criacao_de_personagem = criacao (nome_personagem,genero_personagem,caracteristica_personagem)

        caminho = input ('qual caminho você gostaria de seguir? ').lower()
        if caminho == 'castelo':
            castelo(criacao_de_personagem)
        elif caminho == 'natureza':
            natureza(criacao_de_personagem)
    else:
        print("encerrando programa..")
        break


    

    




