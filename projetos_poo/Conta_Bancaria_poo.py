from hashlib import sha256
import pwinput

class ContaBancaria:
    def __init__(self, id, titular, saldo):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        self.__hash = sha256(self.__pedir_senha().encode('UTF-8')).hexdigest()
        self.__historico = []
        self.__tentativas = 0
        

    def __validar_senha(self, chave):
        '''A senha passada pelo usuário será validada para ver se bate com a mesma quando houve a criação da conta.'''
        '''Toda vez quando houver uma ação rígida, será necessário passar/validar a senha.'''
        chave_usuario = sha256(chave.encode("UTF-8")).hexdigest()    
        if chave_usuario == self.__hash:
            return True
        else:
            return False
        

    def __pedir_senha(self):
        chave = pwinput.pwinput('Senha: ')
        return chave


    def sacar(self, valor_saque):
        '''Aqui, o usuário realiza o saque de acordo com as condições propostas.'''
        self.__tentativas = 0
        while self.__tentativas <3:
            if valor_saque > 0:
                if self.__validar_senha(self.__pedir_senha()) == True:
                        if valor_saque <= self.__saldo:
                            self.__saldo -= valor_saque   
                            print(f'Um saque de {valor_saque}R$ foi realizado de sua conta.')
                            self.__historico.extend([f'Saque de {valor_saque}R$'])
                            break
                        else:
                            print("Saldo Insuficiente!")
                            break
                else:
                    print("Senha Incorreta!")
                    self.__tentativas+=1
            else:
                print('O valor precisa ser maior que 0!')
                break
        else:
            print('3º Tentativa, Conta Bloqueada.')


    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.__saldo += valor_deposito
            print(f'Um valor de {valor_deposito}R$ foi depositado na sua conta')
            self.__historico.extend([f'Depósito de {valor_deposito}R$'])
        else:
            print('Não foi possível depositar esse valor.')
        

    def transferencia(self, valor, outra_Conta):
        '''É realizado uma transferência de uma conta para outra.'''
        self.__tentativas = 0
        while self.__tentativas <3:
            if valor > 0:
                if self.__validar_senha(self.__pedir_senha()) == True:
                    if valor <= self.__saldo:
                        self.__saldo -= valor
                        outra_Conta.depositar(valor)
                        print(f'Foi depositado na conta com ID de {outra_Conta._id} o valor de {valor}R$')
                        self.__historico.extend([f'Transferência para a conta {outra_Conta._id} no valor de {valor}R$'])
                        break
                    else:
                        print('Não é possível realizar uma transferência de um valor maior do que o saldo.')
                        break
                else:
                    print('Senha Incorreta!')
                    self.__tentativas+=1
            else:
                print('Para realizar uma transferência, o valor precisa ser maior que ZERO!')
                break
        else:
            print('3º Tentativa, Conta Bloqueada.')


    def mostrar_saldo(self):
        self.__tentativas = 0
        while self.__tentativas <3:
            if self.__validar_senha(self.__pedir_senha()) == True:
                print(f'Seu Saldo Atual é de {self.__saldo}R$')
                break
            else:
                print(f'Sua Senha está incorreta!')
                self.__tentativas+=1
        else:
            print('3º Tentativa, Conta Bloqueada.')
  

    

    @property
    def nome(self):
        return self._titular
    

    @nome.setter
    def nome(self, novo_nome):
        '''Se caso o usuário optar por trocar o nome, é totalmente possível visando que o mesmo tenha a senha.'''
        self.__tentativas = 0
        while self.__tentativas <3:
            if self.__validar_senha(self.__pedir_senha()) == True:
                self._titular = novo_nome
                print('O nome do titular foi alterado')
                break
            else:
                print("Sua Senha está incorreta!")
                self.__tentativas+=1
        else:
            print('3º Tentativa, Conta Bloqueada.')
  



    @property
    def historico_transacoes(self):
        self.__tentativas = 0
        while self.__tentativas <3:
            if self.__validar_senha(self.__pedir_senha()) == True:
                print(self.__historico)
                break
            else:
                print(f'Sua Senha está incorreta!')
                self.__tentativas+=1
        else:
            print('3º Tentativa, Conta Bloqueada.')

