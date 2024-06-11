from tkinter import *
import tkinter as tk
import backend
from tkinter import messagebox

def obter_dados_input():
    pass

def buscar_todos_dados():
    pass

def buscar():
    pass

def inserir_dados():
    listaValores = []
    
    if nome.get():
        listaValores.append(nome.get())
    if sobrenome.get():
        listaValores.append(sobrenome.get())
    if email.get():
        listaValores.append(email.get())
    if cpf.get():
        listaValores.append(cpf.get())

    resposta = backend.inserir_dados_backend(listaValores)
    
    if resposta != True:
        tk.messagebox.showinfo("Erro", "Não foi possivel cadastrar, verifique os valores digitados")
    else:    
        tk.messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
        
    return resposta

def atualizar_dados():
    pass

def deletar_dados():
    pass

def fechar_app():
    pass

# criação da janela principal
janela = tk.Tk()
janela.title("Cadastro Clientes")
janela.geometry("290x300")
width_entry = 30

# legenda campo de entrada
label_nome = tk.Label(janela, text="Nome: ")
label_sobrenome = tk.Label(janela, text="Sobrenome: ")
label_email = tk.Label(janela, text="Email: ")
label_cpf = tk.Label(janela, text="CPF: ")


# criando campos de entrada
nome = tk.Entry(janela)
sobrenome = tk.Entry(janela)
email = tk.Entry(janela)
cpf = tk.Entry(janela)

# criando botoes
capturar_input = tk.Button(janela, text="Salvar dados", command=obter_dados_input)
ver_todos_registros = tk.Button(janela, text="Ver todos registros", command=buscar_todos_dados)
ver_busca = tk.Button(janela, text="Buscar", command=buscar)
ver_dados_inseridos = tk.Button(janela, text="Inserir", command=inserir_dados)
ver_dados_atualizados = tk.Button(janela, text="Atualizar", command=atualizar_dados)
ver_dados_deletados = tk.Button(janela, text="Deletar", command=deletar_dados)
fechar_aplicativo = tk.Button(janela, text="Fechar", command=fechar_app)


# orientacao dos campos na janela
label_nome.grid(row=0, column=0, sticky="w")
nome.grid(row=0, column=1)
label_sobrenome.grid(row=1, column=0, sticky="w")
sobrenome.grid(row=1, column=1)
label_email.grid(row=2, column=0, sticky="w")
email.grid(row=2, column=1)
label_cpf.grid(row=3, column=0, sticky="w")
cpf.grid(row=3, column=1)
ver_todos_registros.grid(row=5, column=0, columnspan=3)
ver_busca.grid(row=6, column=0, columnspan=3)
ver_dados_inseridos.grid(row=7, column=0, columnspan=3)
ver_dados_atualizados.grid(row=8, column=0, columnspan=3)
ver_dados_deletados.grid(row=8, column=0, columnspan=3)
capturar_input.grid(row=9, column=0, columnspan=3)
fechar_aplicativo.grid(row=10, column=0, columnspan=3)


janela.mainloop()