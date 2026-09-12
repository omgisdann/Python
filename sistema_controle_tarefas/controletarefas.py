tarefas = []

class Tarefa:
    def __init__(self, descricao, prioridade):
        self._descricao = descricao
        self._prioridade = prioridade
        self._estado = False
        tarefas.extend([[self]])


    @property
    def descricao(self):
        return self._descricao

    @property
    def prioridade(self):
        return self._prioridade

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, novo_valor):
        self._estado = novo_valor

    def visualizar_tarefas(self):
        for lista in tarefas:
            for objeto in lista:
                print(objeto.descricao)
                print(objeto.prioridade)
                print(objeto.estado)


    def marcar_como_concluido(self, nome_tarefa):
        for lista in tarefas:
            for objeto in lista:
                if objeto.descricao == nome_tarefa:
                    objeto.estado = True
                    break

        



teste = Tarefa('Estudar', 'Alta')
teste.marcar_como_concluido('Estudar')
teste.visualizar_tarefas()




novo_teste = Tarefa('Ler', 'Baixa')
novo_teste.marcar_como_concluido('Ler')
novo_teste.visualizar_tarefas()
