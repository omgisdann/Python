from sistemadecontrolefinanceiro import *


def main():
    movimentacao = Movimentacao('Boleto', 'Moradia', -1000, 'despesa', '01/01/2001')
    movimentacao2 = Movimentacao('Pagamento','Moradia', 1000, 'receita', '01/01/2001')
    movimentacao3 = Movimentacao('Comissão','Moradia', 2000, 'receita', '01/01/2001')
    movimentacao4 = Movimentacao('Comissão','Moradia', 8000, 'receita', '01/01/2001')


    registro = ControleFinanceiro()
    registro.controle_movimentacoes(movimentacao)
    registro.controle_movimentacoes(movimentacao2)
    registro.controle_movimentacoes(movimentacao3)
    registro.controle_movimentacoes(movimentacao4)


    registro.receitas_calculo()
    registro.despesas_calculo()
    registro.saldo_calculo()

    print(registro.lista_controle)
if __name__ == "__main__":
    main()