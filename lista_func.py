import os

def deletar_lista(lista:str):
        os.remove(lista)

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
