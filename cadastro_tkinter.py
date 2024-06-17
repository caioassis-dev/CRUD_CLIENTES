from tkinter import *
import tkinter as tk
import backend
from tkinter import messagebox
import pdb


def buscar_pelo_cpf():
    lista_cpf = []
    
    if cpf.get():
        lista_cpf.append(cpf.get())
    
    resposta, row = backend.buscar_pelo_cpf_backend(lista_cpf)
    text_widget.delete("1.0","end")

    if row == None and resposta != True:
        tk.messagebox.showinfo("end","Esse cadastro não existe na base de dados!!")
    else:
        # adicionei essa linha abaixo para limpar a saida toda vez que for uma noa requisição
        text_widget.delete("1.0","end")
        for cpf_ in row:
            text_widget.insert("end",f"{cpf_}")    
        
    return resposta,row

def buscar_todos_dados():
    
    resposta,row = backend.buscar_todos_dados_backend()
    # adicionei essa linha abaixo para limpar a saida toda vez que for uma noa requisição
    text_widget.delete("1.0","end") 
    for cadastro in row:

        text_widget.insert("end",f"{cadastro}\n")
    
    return resposta


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
    
    resposta, row = backend.inserir_dados_backend(listaValores)
    
    if resposta != True and row == 'CPF já existe na tabela':
        tk.messagebox.showinfo("Erro", "CPF já existe no cadastro.")
    elif resposta != True:
        tk.messagebox.showinfo("Erro", "Não foi possivel cadastrar, verifique os valores digitados")
    else:
        # adicionei essa linha abaixo para limpar a saida toda vez que for uma noa requisição
        text_widget.delete("1.0","end")    
        text_widget.insert("end",f"Úlltimo cadastro: {row}\n")    
        tk.messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
        
    return resposta

def atualizar_dados():
    resposta,row = buscar_pelo_cpf()
    text_widget.delete("1.0","end")    
    text_widget.insert("end",f"Cadastro anterior: {row}\n")
    
    # criando dicionario para adicionar o valor para cada chave, para poder 
    # ver qual valor será feito a atualização. 
    valores = {}   
    
    valores['nome'] = nome.get() if nome.get() else None
    valores['sobrenome'] = sobrenome.get() if sobrenome.get() else None
    valores['email'] = email.get() if email.get() else None
    valores['cpf'] = cpf.get() if cpf.get() else None
    
    resposta, row = backend.atualizar_dados_backend(valores,row)

    text_widget.insert("end",f"Cadastro atualizado: {row}\n")
    return resposta


def deletar_dados_pelo_cpf():
    
    lista_cpf = []
    
    if cpf.get():
        lista_cpf.append(cpf.get())
        
    resposta, row = backend.buscar_pelo_cpf_backend(lista_cpf)
    resultado = tk.messagebox.askyesno("confirmação", f"Você deseja deletar esse cadastro? {row}")
    
    if resultado:
        resposta, cadastro_deletado = backend.deletar_dados_pelo_cpf_backend(lista_cpf)   
        tk.messagebox.showinfo("Sucesso", "Cadastro deletado!")    
    else:
        tk.messagebox.showinfo("erro", "Cadastro não foi deletado!")

    return resposta

def validar_qtd_cpf(P):
    # Verifica se o valor inserido tem no máximo 11 caracteres e se é um numero.
    if len(P) <= 11 and P.isdigit():
        return True
    else:
        return False

# criação da janela principal
janela = tk.Tk()
janela.title("Cadastro Clientes")
janela.geometry("585x310")
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
# adicionei verificacao para apenas 11 posicoes.
cpf = tk.Entry(janela, validate="key")
cpf['validatecommand'] = (cpf.register(validar_qtd_cpf), '%P')

# criando botoes
ver_todos_registros = tk.Button(janela, text="Ver todos registros", command=buscar_todos_dados)
ver_busca = tk.Button(janela, text="Buscar pelo cpf", command=buscar_pelo_cpf)
ver_dados_deletados = tk.Button(janela, text="Deletar pelo cpf", command=deletar_dados_pelo_cpf)
ver_dados_atualizados = tk.Button(janela, text="Atualizar contatos", command=atualizar_dados)
ver_dados_inseridos = tk.Button(janela, text="Inserir", command=inserir_dados)


# criando espaço texto vazio para inserir informações e um com scroolbar lateral "widget"
text_widget = tk.Text(janela, wrap="word", height=5)
scrollbar = tk.Scrollbar(janela, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)



# orientacao dos campos na janela
label_nome.grid(row=0, column=0, sticky="w", columnspan=2)
nome.grid(row=0, column=1, columnspan=2)
label_sobrenome.grid(row=1, column=0, sticky="w", columnspan=2)
sobrenome.grid(row=1, column=1, columnspan=2)
label_email.grid(row=2, column=0, sticky="w", columnspan=2)
email.grid(row=2, column=1, columnspan=2)
label_cpf.grid(row=3, column=0, sticky="w", columnspan=2)
cpf.grid(row=3, column=1, columnspan=2)
ver_todos_registros.grid(row=4, column=0, columnspan=3)
ver_busca.grid(row=5, column=0, columnspan=3)
ver_dados_deletados.grid(row=6, column=0, columnspan=3)
ver_dados_atualizados.grid(row=7, column=0, columnspan=3)
ver_dados_inseridos.grid(row=8, column=0, columnspan=3)
text_widget.grid(row=9, column=0, sticky="w", columnspan=2)
scrollbar.grid(row=9, column=2, sticky="w", columnspan=2)

janela.mainloop()