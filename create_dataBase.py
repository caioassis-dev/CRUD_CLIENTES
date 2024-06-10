import sqlite3 as sql

conn = sql.connect('clientes.db')
cursor = conn.cursor()

cursor.execute(""" 
    CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        email TEXT NOT NULL,
        cpf VARCHAR(11) NOT NULL
    );
""")

print("Tabela criada com sucesso")

conn.close()

