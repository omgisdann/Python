from pathlib import *
import sqlite3

class Arquivos:
    def __init__(self, endereco):
        if isinstance(endereco, str):
            self._endereco = endereco
        else:
            raise TypeError('O endereço passado deve ser uma STRING!')


    def acessar_conteudos_individuais(self):
        meu_arquivo = Path(self._endereco)
        if meu_arquivo.exists() == True:
            try:
                for arquivo_individual in meu_arquivo.iterdir():
                    if arquivo_individual.is_file():
                        print('Arquivo')
                        print("Nome:" , arquivo_individual.name)
                        print("Extensão:", arquivo_individual.suffix)
                        print(f"Tamanho: {arquivo_individual.stat().st_size}B")
                        print("Caminho:", arquivo_individual, '\n')

                    else:
                        print("Pasta")
                        print("Nome:" , arquivo_individual.name)
                        print(f"Tamanho: {arquivo_individual.stat().st_size}B")
                        print("Caminho:", arquivo_individual, '\n')
            except:
                print("Acessar conteúdos funciona apenas para pastas, não para arquivos!")
        else:
            print("O caminho de endereço passado não existe!")

    def resumo_pasta(self):
        quantidade_arquivos = 0
        quantidade_pastas = 0
        total_itens = 0
        tamanho_dos_arquivos = 0
        meu_arquivo = Path(self._endereco)
        if meu_arquivo.exists() == True:
            if meu_arquivo.iterdir():
                for arquivo_individual in meu_arquivo.iterdir():
                    if arquivo_individual.is_file():
                        quantidade_arquivos +=1
                        tamanho_dos_arquivos += arquivo_individual.stat().st_size
                    else:
                        quantidade_pastas +=1
                        tamanho_dos_arquivos += arquivo_individual.stat().st_size
                total_itens = quantidade_arquivos + quantidade_pastas
                print(f"Arquivos: {quantidade_arquivos}")
                print(f"Pastas: {quantidade_pastas}")
                print(f"Total de itens: {total_itens}")
                print(f"Tamanho dos arquivos: {tamanho_dos_arquivos}B")
            else:
                print("O caminho precisa estar relacionado a uma pasta")
        else:
            print("O caminho para o arquivo não existe!")
            


    def filtro_extensao(self, extensao):
        extensao = extensao.lower()
        meu_arquivo = Path(self._endereco)
        if meu_arquivo.exists() == True:
            try:
                for arquivo_individual in meu_arquivo.iterdir():
                    if arquivo_individual.suffix == extensao:
                        print(arquivo_individual.name)
            except NotADirectoryError:
                print("O caminho precisa estar relacionado a uma pasta!")
        else:
            print('O caminho não existe!')
            

    def filtro_nome(self, nome):
        meu_arquivo = Path(self._endereco)
        if meu_arquivo.exists() == True:
            try:
                for arquivo_individual in meu_arquivo.iterdir():
                    if arquivo_individual.is_file():
                        if arquivo_individual.name == nome:
                            print(arquivo_individual)
                            break
            except NotADirectoryError:
                print('O caminho precisa estar relacionado a uma pasta!')
        else:
            print("O caminho informado não existe!")




while True:
    print("\n===== GERENCIADOR DE ARQUIVOS =====")
    print("1 - Acessar conteúdos individuais")
    print("2 - Resumo da pasta")
    print("3 - Filtrar por extensão")
    print("4 - Filtrar por nome")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao !=5 and opcao <5:
        endereco = input(r"Digite o endereço da pasta ")
        meu_arquivo = Arquivos(endereco)
    
    if opcao == 1:
       meu_arquivo.acessar_conteudos_individuais()
    elif opcao == 2:
        meu_arquivo.resumo_pasta()
    elif opcao == 3:
        meu_arquivo.filtro_extensao('.png')
    elif opcao == 4:
        meu_arquivo.filtro_nome('primeira.png')
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")