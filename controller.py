from dao import DAOprodutos
from modelProdutos import Produtos


class Controller_Produtos:
    def __init__(self):
        self.dao = DAOprodutos()

    def adicionar_produto(self, nome, quantidade):
        novo_produto = Produtos(None, nome, quantidade)
        self.dao.insert_into_table(novo_produto)

    def listar_produtos(self):
        self.dao.select_table()
    
    def atualizar_quantidade(self, id, quantidade):
        produto_atualizado = Produtos(id, None, quantidade)
        self.dao.edit_into_table(produto_atualizado)

    