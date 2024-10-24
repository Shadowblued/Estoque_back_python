from conection import connecting
from modelProdutos import Produtos

class DAOprodutos:

    def insert_into_table(self, novo_produto:Produtos):
        try:
            conn = connecting()
            cursor = conn.cursor()
            comand = f'INSERT INTO produtos (item, quantidade) VALUES (%s, %s)'
            values = (novo_produto.nome, novo_produto.quantidade)
            cursor.execute(comand, values)
            conn.commit()
            cursor.close()
        except :
            return None
        

    def edit_into_table(self, produto_atualizado:Produtos):
        try:
            conn = connecting()
            cursor = conn.cursor()
            comand = f'UPDATE produtos SET quantidade = %s WHERE id = %s'
            values = (produto_atualizado.quantidade, produto_atualizado.id)
            cursor.execute(comand, values)
            conn.commit()
            cursor.close()
        except:
            return None
        
        
    def select_table(self):
        try:
            conn = connecting()
            cursor = conn.cursor()
            comand = 'SELECT * FROM produtos'
            cursor.execute(comand)
            produtos = cursor.fetchall()
            for linha in produtos:
                print(linha)
            cursor.close()
        except :
            return None