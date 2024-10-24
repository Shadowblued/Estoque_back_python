from conection import connecting
from controller import Controller_Produtos
import platform
import os


def menu():
    while True:
        print("""---------- Menu do estoque ----------
    1 - Cadastrar Produto
    2 - Atualizar Quantidade
    3 - Vizualizar todo o Estoque
    4 - Limpar Tela
    5 - Fechar programa""")
        
        op = input("Digite a operação que deseja realizar: ")
        if op == "1":
            adicionar_produto()
            
        elif op == "2":
            atualizar_produto()

        elif op == "3":
            vizualizar_estoque()

        elif op == "4":
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')
        elif op == "5":
            print("Fechando o Programa...")
            break
        else:
            print ("""Ops!!! 
Você não digitou uma operação Válida, tente novamente. """)
            
def adicionar_produto():

    print("---------- Cadastrar Produto ----------")
    print("Para cancelar a operação digite \"CANCELAR\"")
    nome = validar_nome("Digite o nome do produto: ")
    if nome == None:
        return
    quantidade = validar_quantidade("Digite a quantidade que está sendo adicionado ao estoque: ")
    if quantidade == None:
        return

    controller.adicionar_produto(nome, quantidade) #Função do controller

def atualizar_produto():
    
    print("--------- Atualizar quantidade ----------")
    print("Para cancelar a operação Digite \"CANCELAR\"")

    # Adicionar a visualização dos ultimos itens adicionados

    id = validar_quantidade("Digite o ID do produto que você deseja atualizar: ")
    if id == None:
        return
    quantidade = validar_quantidade("Digite o valor atual do produto no estoque: ")
    if quantidade == None:
        return
    
    controller.atualizar_quantidade(id, quantidade) #Função do controller
    print("Alteração bem Sucedida!!")

def vizualizar_estoque():
    print("---------- Vizualizar Estoque ----------")

    controller.listar_produtos()

def validar_nome(mensagem, tipo=str):
    while True:
        entrada = input(mensagem).strip()
        if entrada.lower() == "cancelar":
            print("Cancelando operação...")
            return None
        try: 
            return tipo(entrada)
        except ValueError:
            print(f"Entrada inválida. Por favor digite um valor do tipo {tipo.__name__}")

def validar_quantidade(mensagem, tipo=int):
    while True:
        entrada = (input(mensagem).strip())
        if entrada == "cancelar":
            print("Cancelando operação...")
            return None
        try: 
            entrada = int(entrada)
            return tipo(entrada)
        except ValueError:
            print(f"Entrada inválida. Por favor digite um valor do tipo {tipo.__name__}")

if __name__ == "__main__":
    controller = Controller_Produtos()

    conn = connecting()
    print("Iniciando o Estoque...")
    menu()


if conn:
    conn.close()

