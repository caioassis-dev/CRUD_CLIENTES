import sqlite3 as sql
import pdb
conn = sql.connect('clientes.db')
cursor = conn.cursor()


def inserir_dados_backend(listaDados):

    listaDadosInseridos = []
    try:
        consulta = """
            INSERT INTO clientes (nome, sobrenome, email, cpf)
            VALUES (?, ?, ?, ?)
        """
        # Lendo os dados
        cursor.execute(consulta, listaDados)

        conn.commit()
        return True,listaDados
    
    except Exception as e:
        print(e)
        return str(e)

def buscar_todos_dados_backend():
    
    listaCadastros = []
    try:
        
        cursor.execute("SELECT * FROM clientes")
        
        for row in cursor.fetchall():
            listaCadastros.append(row)
        
        return True,listaCadastros
        
    except Exception as e:
        return str(e)
    
