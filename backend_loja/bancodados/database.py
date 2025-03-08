import sqlite3

def criar_database():
    conector = sqlite3.connect("bancodados/acai_loja.db")
    cursor = conector.cursor()

    #produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT, 

            disponibilidade_balcao REAL DEFAULT 0.0,
            unidade_balcao TEXT DEFAULT '',

            disponibilidade_aberto REAL DEFAULT 0.0,
            unidade_aberto TEXT DEFAULT '',

            disponibilidade_lacrado REAL DEFAULT 0.0,
            unidade_lacrado TEXT DEFAULT ''
        )
    ''')

    