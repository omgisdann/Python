print("PROJETO FUNCIONALIDADES!")
lista=[]
while True:

    dicionario={}

    print("\nMENU:")
    print("1 - Adicionar contato")
    print("2 - Contatos salvos")
    print("3 - Buscar contato")
    print("4 - Atualizar contato")
    print("5 - Remover contato")
    print("6 - Sair")
    usuario = int (input('digite a opção desejada ' ))


    if usuario == 1:
        print('adicionar contato!')
        nome = input ('digite o nome do contato ' )
        telefone = int (input("digite o telefone " ))
        email = input ('digite o email ' )

        dicionario['nome']=nome
        dicionario['telefone']=telefone
        dicionario['email']=email

        lista.append(dicionario.copy())

    elif usuario == 2:
        print(f"os dados salvos na lista são : ")

        for e in lista:
            print(e)

    

    elif usuario == 3:
        print("Busca Personalizada!")
        email_do_contato = input('digite o email do contato ')

        for e in lista:
            if email_do_contato == e['email']:
                print(e)
    


    elif usuario == 4:
        print("Atualizar contato")
        att = input("informe o contato a ser atualizado, nos informando o email " )
        option = input ('o que você gostaria de atualizar? ' ).lower()


        if option == 'telefone':
            new_number=int(input("qual será o novo telefone a adicionar? " ))

            for e in lista:
                if att == e['email']:
                    e['telefone']=new_number
                    print(e)
        

        elif option == 'email':
            new_email=input("qual será o novo email a adicionar? " )

            for e in lista:
                if att == e['email']:
                    e['email']=new_email
                    print(e)
        else:
            print("OPÇÃO INVÁLIDA!")

        
    elif usuario == 5:
        print("remoção de contato!")
        contato_a_remover = input ('digite o contato a remover, nos informando o email: ' )
        encontrado = False

        for e in lista:
            if contato_a_remover == e['email']:
                lista.remove(e)
                encontrado = True
                break

        if not encontrado:
            print("não foi encontrado")
        

    elif usuario == 6:
        print('ATÉ LOGO!')
        break