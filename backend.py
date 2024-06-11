import sqlite3 as sql
import pdb
conn = sql.connect('clientes.db')
cursor = conn.cursor()


def inserir_dados_backend(listaDados):
    
    try:
        consulta = """
            INSERT INTO clientes (nome, sobrenome, email, cpf)
            VALUES (?, ?, ?, ?)
        """
        # Lendo os dados
        cursor.execute(consulta, listaDados)

        conn.commit()
        return True
    
    except Exception as e:
        return str(e)


