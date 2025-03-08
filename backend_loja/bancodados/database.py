import sqlite3

def criar_database():
    conector = sqlite3.connect("bancodados/acai_loja.db")
    cursor = conector.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco
        )
    ''')