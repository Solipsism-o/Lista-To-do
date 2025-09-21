import os
import lista_func as L
from sys import exit

def limpar_tela():
    os.system('clear')

def inserir_a_fazer():
    afazer=str(input("Digite o a fazer: \n"))
    return afazer

def Mostrar_menu():
    limpar_tela()
    print("=========   LISTA DE AFAZERES   =========\n")
    Lista1.mostrar_lista()

Lista1=L.Lista()
Lista1.carregar_lista()

def menu():
    erro_menu = ""
    while True:
        Mostrar_menu()
        if erro_menu:
            print(f"\n{erro_menu}")
        operacao = input("\nDigite a operação desejada:\n1 - Adicionar a fazer\n2 - Remover a fazer\n3 - Editar\n4 - Sair\n")
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
            item = inserir_a_fazer()
            Lista1.adicionar_item(item)
            L.deletar_lista("lista.txt")
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
                    L.deletar_lista("lista.txt")
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
                    novo_item = input("Digite o novo a fazer:\n")
                    Lista1.editar_item(item_editar, novo_item)
                    L.deletar_lista("lista.txt")
                    Lista1.salvar_lista()
                    break
                except IndexError:
                    erro_editar = "Item inválido! Escolha um número que está na lista."
                except ValueError:
                    erro_editar = "Digite um número válido"
        case 4:
            L.deletar_lista("lista.txt")
            Lista1.salvar_lista()
            exit()

while True:
    menu()
