import os
import sqlite3

def conectar_bd():
    # Caminho da pasta onde o banco será salvo
    pasta_bd = os.path.join(os.path.dirname(__file__), "bancodados")

    if not os.path.exists(pasta_bd):
        os.makedirs(pasta_bd)

    caminho_db = os.path.join(pasta_bd, "acai_loja.db")

    return sqlite3.connect(caminho_db)


def criar_database():
    conector = conectar_bd()
    cursor = conector.cursor()

    # Tabela de produtos gerais
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT, 

            estoque_balcao REAL DEFAULT 0.0,
            unidade_balcao TEXT DEFAULT '',

            estoque_aberto REAL DEFAULT 0.0,
            unidade_aberto TEXT DEFAULT '',

            estoque_lacrado REAL DEFAULT 0.0,
            unidade_lacrado TEXT DEFAULT ''
        )
    ''')

    # Tabela específica para açaí
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS acai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,

            estoque_balcao REAL DEFAULT 0.0,
            unidade_balcao TEXT DEFAULT 'kg',

            estoque_freezer REAL DEFAULT 0.0,
            unidade_freezer TEXT DEFAULT 'kg'
        )
    ''')

    conector.commit()
    conector.close()

if __name__ == "__main__":
    criar_database()
    print("Banco de dados criado com sucesso!")