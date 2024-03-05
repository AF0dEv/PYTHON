import tkinter as tk
from tkinter import messagebox

# Estrutura

# Janela
root = tk.Tk()

# Tamanho da Janela 
root.geometry('500x470')

# Titulo da Janela
root.title('Agenda de Contatos')

# Widgets

# Label -> Nome
nome_label = tk.Label(root, text='Nome')
nome_label.pack() # .pack -> Agrupa Conteudo como lista

# Entry -> Campo de Texto Nome
nome_entry = tk.Entry(root)
nome_entry.pack()

# Label -> Endereço
endereco = tk.Label(root, text='Endereço')
endereco.pack() # .pack -> Agrupa Conteudo como lista

# Entry -> Campo de Texto Endereço
endereco_entry = tk.Entry(root)
endereco_entry.pack()

# Label -> Código Postal
codigopostal = tk.Label(root, text='Código Postal')
codigopostal.pack() # .pack -> Agrupa Conteudo como lista

# Entry -> Campo de Texto Código Postal
codigopostal_entry = tk.Entry(root)
codigopostal_entry.pack()

# Label -> Telefone
telefone = tk.Label(root, text='Telefone')
telefone.pack() # .pack -> Agrupa Conteudo como lista

# Entry -> Campo de Texto Telefone
telefone_entry = tk.Entry(root)
telefone_entry.pack()


# Funções

# Função para Guardar Contato no Ficheiro de Texto
def guardar_contato():
    # .get() <-- busca os valores 
    nome = nome_entry.get() 
    endereco = endereco_entry.get()
    codigopostal = codigopostal_entry.get()
    telefone= telefone_entry.get()
    with open('pessoas.txt', 'a') as ficheiro: # 'a' <-- abre o ficheiro para escrita, mas não apaga o conteúdo
        ficheiro.write(f'{nome}, {endereco}, {codigopostal}, {telefone}\n') # .write <-- escreve no ficheiro, neste caso, os valores das variáveis
    messagebox.showinfo('Sucesso','Guardado') # .showinfo <-- mostra uma mensagem de informação


# Função para Exibir Contatos do Ficheiro de Texto na Área de Texto
def exibir_contatos():
    with open('pessoas.txt') as ficheiro:
        conteudo = ficheiro.read() # .read() <-- lê o conteúdo do ficheiro
        contactos_textArea.delete(1.0, tk.END) # .delete(1.0, tk.END) <-- apaga o conteúdo da área de texto 
        contactos_textArea.insert(tk.END, conteudo) # .insert(tk.END, conteudo) <-- insere o conteúdo na área de texto


# Função para Apagar Todos os Contatos do Ficheiro de Texto na Área de Texto e no Ficheiro
def apagar_contatos():
    with open('pessoas.txt', 'w') as ficheiro: # 'w' <-- abre o ficheiro para escrita
        ficheiro.write('') # .write <-- escreve no ficheiro, neste caso, nada
    messagebox.showinfo('Sucesso','Apagado')


# Função para Editar Contato no Ficheiro de Texto na Área de Texto e no Ficheiro
def editar_contato():
    novo_conteudo = contactos_textArea.get(1.0, tk.END) # .get(1.0, tk.END) <-- busca os valores 
    with open('pessoas.txt', 'w') as ficheiro: # 'w' <-- abre o ficheiro para escrita
        ficheiro.write(novo_conteudo) # .write <-- escreve no ficheiro
    messagebox.showinfo('Sucesso', 'Contato editado com sucesso') # .showinfo <-- mostra uma mensagem de informação
    

# Botões
    
# Botão para Guardar Contato
btn_ok = tk.Button(root, text='Guardar', command=guardar_contato)
btn_ok.pack()

# Botão para Exibir Contatos
btn_ver = tk.Button(root, text='Ver Contatos', command=exibir_contatos)
btn_ver.pack()

# Label -> Explicação
explicacao_label = tk.Label(root, text='Estes botões editam todo o arquivo, portanto a área de texto representa o arquivo de texto')
explicacao_label.pack()

# Botão para Editar Contatos
btn_editar = tk.Button(root, text='Editar Contatos', command=editar_contato)
btn_editar.pack()

# Botão para Apagar Todos os Contatos
btn_apagar = tk.Button(root, text='Apagar Todos Contatos', command=apagar_contatos)
btn_apagar.pack()

# Área de Texto para Exibir Contatos, Editar File e Apagar Contatos
contactos_textArea = tk.Text(root, width=40, height=10)
contactos_textArea.pack()


# Loop da Janela

root.mainloop()