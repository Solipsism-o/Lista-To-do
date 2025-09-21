import os

def deletar_lista(lista:str):
    try:
        os.remove(lista)
    except FileNotFoundError:
        print(f"Arquivo '{lista}' não encontrado.")

def limpar_tela():
    os.system('clear')

def inserir_afazer():
    afazer=str(input("Digite o afazer: \n"))
    return afazer

class Lista:
    def __init__(self):
        self.itens = []

    def salvar_lista(self):
        with open('lista.txt', 'w') as l:
            for item in self.itens:
                l.write(f"{item}\n")

    def carregar_lista(self):
        try:
            with open('lista.txt', 'r') as f:
                 linhas = [linha.strip() for linha in f]
                 for x in linhas:
                     self.itens.append(x)
        except FileNotFoundError:
            pass

    def adicionar_item(self, item:str):
        self.itens.append(item)

    def editar_item(self,num_lista:int,novo_item:str):
        num_lista-=1
        self.itens[num_lista]=novo_item

    def remover_item(self, item:int):
        item=item-1
        self.itens.remove(self.itens[item])

    def mostrar_lista(self):
        for x in range(len(self.itens)):
            print(f"{x+1} - {self.itens[x]}")

def Mostrar_menu():
    limpar_tela()
    print("=========   LISTA DE AFAZERES   =========\n")
    Lista1.mostrar_lista()

Lista1=Lista()
Lista1.carregar_lista()

def menu():
    erro_menu = ""
    while True:
        Mostrar_menu()
        if erro_menu:
            print(f"\n{erro_menu}")
        operacao = input("\nDigite a operação desejada:\n1 - Adicionar afazer\n2 - Remover afazer\n3 - Editar\n4 - Sair\n")
        try:
            operacao = int(operacao)
            if operacao in [1, 2, 3, 4]:
                break
            else:
                erro_menu = "Digite um número entre 1 e 4."
        except ValueError:
            erro_menu = "Digite um número válido."

    match operacao:
        case 1:
            item = inserir_afazer()
            Lista1.adicionar_item(item)
            deletar_lista("lista.txt")
            Lista1.salvar_lista()
        case 2:
            erro_remover = ""
            while True:
                Mostrar_menu()
                if erro_remover:
                    print(f"\n{erro_remover}")
                try:
                    item_remover = input("qual item você deseja remover?\n\nDigite X para cancelar a operação\n\n")
                    if item_remover == "X":
                        break
                    item_remover = int(item_remover)
                    Lista1.remover_item(item_remover)
                    deletar_lista("lista.txt")
                    Lista1.salvar_lista()
                    break
                except IndexError:
                    erro_remover = "Item inválido! Escolha um número que está na lista."
                except ValueError:
                    erro_remover = "Digite um número válido"
        case 3:
            erro_editar = ""
            while True:
                Mostrar_menu()
                if erro_editar:
                    print(f"\n{erro_editar}")
                try:
                    item_editar = input("qual item você deseja editar?\n\nDigite X para cancelar a operação\n")
                    if item_editar == "X":
                        break
                    item_editar = int(item_editar)
                    novo_item = input("Digite o novo afazer:\n")
                    Lista1.editar_item(item_editar, novo_item)
                    deletar_lista("lista.txt")
                    Lista1.salvar_lista()
                    break
                except IndexError:
                    erro_editar = "Item inválido! Escolha um número que está na lista."
                except ValueError:
                    erro_editar = "Digite um número válido"
        case 4:
            deletar_lista("lista.txt")
            Lista1.salvar_lista()
            exit()

while True:
    menu()
