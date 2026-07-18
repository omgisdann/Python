class Filme:
    def __init__(self, codigo, nome, genero):
        self.codigo = codigo
        self.nome = nome
        self.genero = genero
        self.disponivel = True


class Locadora:
    def __init__(self):
        self.filmes = []

    def cadastrar_filme(self):
        codigo = int(input("Código: "))
        nome = input("Nome do filme: ")
        genero = input("Gênero: ")

        for filme in self.filmes:
            if filme.codigo == codigo:
                print("Código já cadastrado.")
                return

        novo_filme = Filme(codigo, nome, genero)
        self.filmes.append(novo_filme)
        print("Filme cadastrado com sucesso!")

    def listar_filmes(self):
        if len(self.filmes) == 0:
            print("Nenhum filme cadastrado.")
            return

        print("\n===== FILMES =====")

        for filme in self.filmes:
            if filme.disponivel:
                status = "Disponível"
            else:
                status = "Alugado"

            print(f"Código: {filme.codigo}")
            print(f"Nome: {filme.nome}")
            print(f"Gênero: {filme.genero}")
            print(f"Status: {status}")
            print("-" * 25)

    def alugar_filme(self):
        codigo = int(input("Código do filme: "))

        for filme in self.filmes:
            if filme.codigo == codigo:
                if filme.disponivel:
                    filme.disponivel = False
                    print("Filme alugado.")
                else:
                    print("Filme já está alugado.")
                return

        print("Filme não encontrado.")

    def devolver_filme(self):
        codigo = int(input("Código do filme: "))

        for filme in self.filmes:
            if filme.codigo == codigo:
                if not filme.disponivel:
                    filme.disponivel = True
                    print("Filme devolvido.")
                else:
                    print("Esse filme já está disponível.")
                return

        print("Filme não encontrado.")


locadora = Locadora()

while True:
    print("""
========== LOCADORA ==========
1 - Cadastrar filme
2 - Listar filmes
3 - Alugar filme
4 - Devolver filme
0 - Sair
==============================
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        locadora.cadastrar_filme()

    elif opcao == "2":
        locadora.listar_filmes()

    elif opcao == "3":
        locadora.alugar_filme()

    elif opcao == "4":
        locadora.devolver_filme()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")