class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def criar_produto(self):
        return (self.nome, self.preco)


class Carrinho:
    def __init__(self):
        self.lista = []

    def adicionar_ao_carrinho(self, produto):
        self.lista.append(produto.criar_produto())

    def deletar_produto(self, produto_a_remover):
        for item in self.lista[:]:
            if item[0] == produto_a_remover:
                self.lista.remove(item)

    def mostrar_carrinho(self):
        print(self.lista)

    def calcular_total(self):
        total = 0
        for item in self.lista:
            total += item[1]
        print(f"Total dos produtos: R$ {total}")


# TESTES
teste = Produto('YPê', 8)
teste1 = Produto('Amaciante', 14)
teste2 = Produto('Sabão', 10)

car = Carrinho()

car.adicionar_ao_carrinho(teste)
car.adicionar_ao_carrinho(teste1)
car.adicionar_ao_carrinho(teste2)

car.mostrar_carrinho()
car.calcular_total()

car.deletar_produto('Amaciante')

car.mostrar_carrinho()
car.calcular_total()