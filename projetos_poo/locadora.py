class Veiculo:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.disponivel = True
        '''essa classe serve APENAS para, depois de criada, ser passada para locadora.
        lá onde faremos as transações reais, mas jamais aqui!'''

    def exibir_dados (self):
        print(f'MODELO DO VEICULO {self.modelo}')
        print(f'MARCA DO VEICULO {self.marca}')
        print(f'ANO DO VEÍCULO {self.ano}')
        print(f'SITUAÇÃO DO VEÍCULO {self.disponivel}')


class Locadora:
    def __init__(self):
        self.lista_veiculos = []
        self.lista_clientes = []


    def listar_veiculo (self, veiculo):
        if veiculo.modelo:
            self.lista_veiculos.extend([[veiculo.modelo, veiculo.marca, veiculo.ano, veiculo.disponivel]])
        else:
            print('não foi possivel adicionar o carro a nossa locadora')


    def listar_cliente (self, cliente):
        if cliente.nome:
            self.lista_clientes.extend([[cliente.nome, cliente.idade, cliente.veiculos_alugados_cliente]])
        else:
            print('não foi possivel adicionar o cliente a nossa loja.')


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.veiculos_alugados_cliente = []


    '''o cliente alugará um veículo da locadora!!! NÃO da própria CLASSE veiculo!'''
    def alugar_veiculo (self, nome_do_veículo_a_alugar, locadora):
        for e in locadora.lista_veiculos:
            for j in e:
                if j == nome_do_veículo_a_alugar:
                    e[3] = False
                    self.veiculos_alugados_cliente.extend([e])
                    locadora.lista_veiculos.remove(e)
                    break
                else:
                    print('não possuimos nenhum veículo com este nome!')
                    break
    


    def devolver_veiculo (self, nome_do_veículo_a_devolver, locadora):
        for e in self.veiculos_alugados_cliente:
            for j in e:
                if j == nome_do_veículo_a_devolver:
                    e[3] = True
                    locadora.lista_veiculos.extend([e])
                    self.veiculos_alugados_cliente.remove(e)
                    break
                else:
                    print('não possuimos nenhum veículo com este nome!')
                    break


print('BEM VINDO A NOSSA LOCADORA!') 
carros_alugados = 0
pessoa_criada = 0
veiculo_criado = 0
while True:
    print("\n===== LOCADORA DE VEÍCULOS =====")
    print("1 - Cadastrar veículo")
    print("2 - Listar veículo")
    print("3 - Cadastrar cliente")
    print("4 - Listar cliente")
    print("5 - Alugar veículo")
    print("6 - Devolver veículo")
    print("7 - Mostrar veículo alugado de um cliente")
    print("8 - Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("digite uma opção válida! ")


    if opcao == 1:
        if veiculo_criado == 0:
            print ('CADASTRAMENTO DE VEÍCULOS')

            modelo = input ('digite o modelo do carro ').lower()
            marca = input ('digite a marca do carro ').lower()

            '''aqui, só criaremos um veículo caso o ano informado seja correto, caso contrário, perguntaremos até obter a resposta correta.'''
            while True:
                try:
                    ano = int(input ('digite o ano do carro '))
                    veiculo_criado +=1
                    break
                except ValueError:
                    print('digite uma data válida! ')
                


            veiculo_liberado = False
            veiculo_cadastrado = Veiculo (modelo, marca, ano) # O veículo só será cadastrado se todas as informações acima estiverem corretas, caso contrário pedirá a data infinitamente!
            veiculo_liberado = True             





    elif opcao == 2:
        print ('Listagem de veículos')


        try:
            '''essa variável nos ajuda a ter mais controle, fazendo que, só seja possível listar um veículo, caso o MESMO tiver sido criado'''
            if veiculo_liberado == True:
                try:
                    localiza.listar_veiculo(veiculo_cadastrado)
                except:
                    localiza = Locadora ()
                    localiza.listar_veiculo(veiculo_cadastrado)
        except NameError:
            print('O veículo não foi criado! sendo assim, impossível realizar a listagem.')
        
       
        
        
    elif opcao == 3 and pessoa_criada == 0:
        print ('Cadastramento de cliente')

        nome = input ("digite o nome do cliente a ser cadastrado ").lower()
        while True:
            try:
                idade = int(input ('digite a idade do cliente '))
                pessoa_criada +=1
                break
            except ValueError:
                print('digite uma idade válida! ')

        
        cliente_liberado = False
        cliente_cadastrado = Cliente (nome, idade) # O cliente só será cadastrado se todas as informações acima estiverem corretas, caso contrário pedirá a idade infinitamente!
        cliente_liberado = True             


        



    elif opcao == 4:
        print ('Listagem de cliente')

        try:
            '''essa variável nos ajuda a ter mais controle, fazendo que, só seja possível listar um cliente, caso o MESMO tiver sido criado'''
            if cliente_liberado == True:
                try:
                    localiza.listar_cliente(cliente_cadastrado)
                except:
                    localiza = Locadora ()
                    localiza.listar_cliente(cliente_cadastrado)
        except NameError:
            print('O cliente não foi criado! sendo assim, impossível realizar a listagem.')
        



    elif opcao == 5:
        print('Alugamento de veículo')
        
        if carros_alugados == 0:
            nome_pessoal = input ("digite o seu nome, iremos procurar na nossa lista para realizar o empréstimo. ").lower()
            modelo_veiculo = input ("digite o nome do veículo que você irá querer o empréstimo. ").lower()
            try:
                for e in localiza.lista_clientes:
                    for j in e:
                        if j == nome_pessoal:
                            for h in localiza.lista_veiculos:
                                for i in h:
                                    if i == modelo_veiculo:
                                        h[3] = False
                                        carro = h
                                        e[2] = carro
                                        localiza.lista_veiculos.remove(h)
                                        carros_alugados+=1
                                        break
                                    else:
                                        print("veiculo não encontrado!")
                                        break
                            break
                        else:
                            print('Não temos esse usuário cadastrado na nossa locadora')
            except NameError:
                print("Para alugar um carro, primeiro é necessário se cadastrar em nossa locadora!")

    


    elif opcao == 6:
        print ('Devolução de veículo')

        nome_pessoal = input ("digite o seu nome, iremos procurar na nossa lista para realizar a devolução. ").lower()
        modelo_veiculo = input ("digite o nome do veículo que você irá devolver. ").lower()


        try:
            for lista_individual_de_clientes in localiza.lista_clientes:
                for elemento in lista_individual_de_clientes:
                    if elemento == nome_pessoal:
                        print('achamos o seu nome no nosso cadastro')
                        if modelo_veiculo == lista_individual_de_clientes[2][0]:
                            lista_individual_de_clientes[2][3] = True
                            localiza.lista_veiculos.append(lista_individual_de_clientes[2])
                            lista_individual_de_clientes[2].clear()
                            break
                        else:
                            print('não encontramos o carro!')
                    else:
                        print('não achamos seu nome no nosso cadastro!')
        except NameError: 
            print("Para alugar um carro, primeiro é necessário se cadastrar em nossa locadora!")
            '''se caso um cliente nao for cadastrado na locadora, esse erro vai explodir'''


    
    elif opcao == 7:
        print("Veículo Alugado")
        nome = input ("digite o seu nome ")
        try:
            for lista_individual_de_clientes in localiza.lista_clientes:
                if elemento == nome_pessoal:
                    print(lista_individual_de_clientes[2])
        except:
            print("é necessário se cadastrar na nossa plataforma!")


    elif opcao == 8:
        print('Até logo')
        break