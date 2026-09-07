from datetime import datetime
import sqlite3

class Movimentacao:
    id = 1
    categorias = [
    "alimentação",
    "transporte",
    "moradia",
    "lazer",
    "educação",
    "saúde",
    "academia",
    "games",
    "assinaturas",
    "viagem",
    "presente"]
    def __init__(self, descricao, categoria, valor, tipo, data):



        descricao = descricao.lower()
        if descricao != '':
            self._descricao = descricao
        else:
            raise Exception('É necessário ter uma DESCRIÇÃO!')


        
        categoria = categoria.lower()
        if categoria in Movimentacao.categorias:
            self._categoria = categoria
        else:
            raise Exception('A categoria não está inclusa.')



        if isinstance(valor, int):
            self._valor = valor
        else:
            raise TypeError("O VALOR precisa ser um número inteiro")



        tipo = tipo.lower()
        if tipo == 'despesa' or tipo == 'receita':
            self._tipo = tipo
        else:
            raise Exception('O tipo da movimentação só pode ser RECEITA ou DESPESA!')

        

        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            self._data = data
        except:
            raise Exception("Formato de data inválido")

        Movimentacao.id +=1

while True:
    print('CONTROLE FINANCEIRO')
    print("1 - Registrar movimentação" ,
          "2 - Listar movimentação",
          "3 - Ver receitas",
          "4 - Ver despesas",
          "5 - Ver saldo",
          "6 - Remover movimentação ",
          "7 - Alterar movimentação",
          "8 - Busca de movimentação específica por ID", 
          "9 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("=====MENU PARA REGISTRAR MOVIMENTAÇÃO=====")
        descricao = input ("digite a descrição da sua movimentação ")
        categoria = input ("digite a categoria da sua movimentação ")
        valor = int(input("digite o valor da sua movimentação "))
        tipo = input("digite o tipo da sua movimentação ")
        data = input("digite a data da sua movimentação ")

        movimentacao = Movimentacao(descricao, categoria, valor, tipo, data)
        try:
            cursor = conexao.cursor()

            cursor.execute("""                
                                    INSERT INTO movimentacoes(descricao, categoria, valor, tipo, data)  
                                    VALUES(?,?,?,?,?)
                                    """, ( 
                                    movimentacao._descricao, 
                                    movimentacao._categoria, 
                                    movimentacao._valor,           
                                    movimentacao._data
                                    ))

            conexao.commit()
        except NameError:
            conexao = sqlite3.connect("financeiro.db") ##É CRIADO O BANCO DE DADOS
            cursor = conexao.cursor()
            cursor.execute("""
                            CREATE TABLE movimentacoes(
                                id INTEGER PRIMARY KEY,
                                descricao TEXT,
                                categoria TEXT,          
                                valor INTEGER,
                                tipo TEXT,
                                data TEXT
                                )    
                            """)  ##É CRIADO AS TABELAS E COLUNAS (VAZIAS)
            
                        
            cursor.execute("""                
                        INSERT INTO movimentacoes(descricao, categoria, valor, tipo, data)  
                        VALUES(?,?,?,?,?)
                        """, ( 
                        movimentacao._descricao, 
                        movimentacao._categoria, 
                        movimentacao._valor,            #fala de onde vai vim os valores que preencherá as colunas
                        movimentacao._tipo, 
                        movimentacao._data
                        ))
            
            conexao.commit()

    elif opcao == 2:
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * 
            FROM movimentacoes
            """)
    
        dados = cursor.fetchall()
        print(dados)
        

    elif opcao == 3:
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * 
            FROM movimentacoes
            """)
        dados = cursor.fetchall()        
        receita = 0
        for dado in dados:
            if dado[4] == 'receita':
                receita += dado[3]
            print(f'receita de {receita} R$')
          


    elif opcao == 4:
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * 
            FROM movimentacoes
            """)
        dados = cursor.fetchall()   
        despesa = 0
        for dado in dados:
            if dado[4] == 'despesa':
                despesa += dado[3]
            print(f'despesa de -{despesa} R$')
          

    elif opcao == 5:
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * 
            FROM movimentacoes
            """)
        dados = cursor.fetchall()   
        saldo = 0
        for dado in dados:
            if dado[4] == 'receita':
                saldo+=dado[3]
            else:
                saldo-=dado[3]
        if saldo < 0:
            print(f'Déficit de {saldo} R$')
        elif saldo > 0:
            print(f'Superávit de {saldo} R$')
        else:
            print(f'saldo de {saldo} R$')

    elif opcao == 6:
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        id_da_movimentacao = input("Digite o ID da movimentação que você irá querer remover ")
        confirmacao = input("Deseja de fato remover a movimentação? ").lower()
        if confirmacao == 'sim':
            cursor.execute("""
            DELETE 
            FROM movimentacoes 
            where id = ?
            """, id_da_movimentacao)
            print(f'A remoção foi realizada com sucesso!')
            conexao.commit()
        else:
            print("Movimentação não removida")

    elif opcao == 7:
        id_da_movimentacao = input("Digite o ID da movimentação que você irá querer alterar ")
        categoria_a_modificar = input("digite o que modificar ")
        if categoria_a_modificar == 'valor':
            try:
                novo_valor = int(input("Digite o novo valor "))
            except ValueError:'O valor precisa ser um número inteiro'
        elif categoria_a_modificar == 'data':
            data_modificada = input("Digite o novo valor com %d/%m/%Y ")
            try:
                novo_valor = datetime.strptime(data_modificada, "%d/%m/%Y")
            except ValueError: 'O valor precisa ser uma data no formato %d/%m/%Y'
        else:
            novo_valor = input("Digite o novo valor ")
     


        if categoria_a_modificar == 'descricao':
            cursor.execute("""
            UPDATE movimentacoes
            SET descricao = ?
            WHERE id = ?
            """, (novo_valor, id_da_movimentacao))
            conexao.commit()

        elif categoria_a_modificar == 'categoria':
            cursor.execute("""
            UPDATE movimentacoes
            SET categoria = ?
            WHERE id = ?
            """, (novo_valor, id_da_movimentacao))
            conexao.commit()

        elif categoria_a_modificar == 'valor':
            cursor.execute("""
            UPDATE movimentacoes
            SET valor = ?
            WHERE id = ?
            """, (novo_valor, id_da_movimentacao))
            conexao.commit()

        elif categoria_a_modificar == 'tipo':
            cursor.execute("""
            UPDATE movimentacoes
            SET tipo = ?
            WHERE id = ?
            """, (novo_valor, id_da_movimentacao))
            conexao.commit()

        elif categoria_a_modificar == 'data':
            cursor.execute("""
            UPDATE movimentacoes
            SET data = ?
            WHERE id = ?
            """, (novo_valor, id_da_movimentacao))
            conexao.commit()

    elif opcao == 8:
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        id_procurar = input("digite o id da movimentação na qual você irá procurar ")
        cursor.execute("""
        SELECT *
        FROM movimentacoes
        WHERE id = ? """,(id_procurar))
        movimentacao_especifica = cursor.fetchall()
        print(movimentacao_especifica)


    elif opcao == 9:
        print("ATÉ LOGO!")
        break














