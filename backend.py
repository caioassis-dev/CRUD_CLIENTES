import sqlite3 as sql
import pdb
conn = sql.connect('clientes.db')
cursor = conn.cursor()


def inserir_dados_backend(listaDados):

    # capturando apenas o valor do CPF
    cpf = listaDados[-1]
        
    try:
        # Verifica se o CPF já existe na tabela
        cursor.execute("SELECT 1 FROM clientes WHERE cpf = ?", (cpf,))
        if cursor.fetchone():
            cpf_existe = "CPF já existe na tabela"
            return False, cpf_existe

        # Insere o novo cliente
        consulta = """
            INSERT INTO clientes (nome, sobrenome, email, cpf)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(consulta,listaDados)
        conn.commit()
        
        return True, listaDados

    except Exception as e:
        return False, str(e)
    
def buscar_pelo_cpf_backend(cpf):
    cpf_selecionado = []
    
    string_cpf = cpf[0]
    
    try:
        consulta = f""" 
            SELECT * FROM clientes WHERE cpf = {string_cpf}
        """
        cursor.execute(consulta)
        
        for row in cursor.fetchall():

            cpf_selecionado.append(row)
        if len(cpf_selecionado) == 0:
            return False,None
        else: 
            return True,cpf_selecionado
    
    except Exception as e:
        
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
    
def deletar_dados_pelo_cpf_backend(cpf_numero):
    
    cpf_numero = cpf_numero[0]
    
    cpf_selecionado = []
    try:
        consulta = f""" 
            DELETE FROM clientes WHERE cpf = {cpf_numero};
        """
        cursor.execute(consulta)
        conn.commit()
        
        for row in cursor.fetchall():

            cpf_selecionado.append(row)
        if len(cpf_selecionado) == 0:
            return False,None
        else: 
            return True,cpf_selecionado
        
    except Exception as e:
        
        return str(e)