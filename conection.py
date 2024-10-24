import mysql.connector
from mysql.connector import Error

def connecting():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='projeto_inter_3'
        )
        if connection.is_connected():
            print("Conexão bem-sucedida!")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None