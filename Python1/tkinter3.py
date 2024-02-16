import tkinter as tk
from tkinter import messagebox

# Estrutura
root = tk.Tk()
root.geometry('400x300')
root.title('Agenda de Contatos')

# Widgets

nome_label = tk.Label(root, text='Nome')
nome_label.pack() # .pack -> Agrupa Conteudo como lista

nome_entry = tk.Entry(root)
nome_entry.pack()

endereco = tk.Label(root, text='Endereço')
endereco.pack() # .pack -> Agrupa Conteudo como lista

endereco_entry = tk.Entry(root)
endereco_entry.pack()

codigopostal = tk.Label(root, text='Código Postal')
codigopostal.pack() # .pack -> Agrupa Conteudo como lista

codigopostal_entry = tk.Entry(root)
codigopostal_entry.pack()

telefone = tk.Label(root, text='Telefone')
telefone.pack() # .pack -> Agrupa Conteudo como lista

telefone_entry = tk.Entry(root)
telefone_entry.pack()

def guardar_contato():
    # .get() <-- busca os valores 
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    codigopostal = codigopostal_entry.get()
    telefone= telefone_entry.get()
    with open('pessoas.txt', 'a') as ficheiro:
        ficheiro.write(f'{nome}, {endereco}, {codigopostal}, {telefone}\n')
    messagebox.showinfo('Sucesso','Guardado')
    
def exibir_contatos():
    with open('pessoas.txt') as ficheiro:
        conteudo = ficheiro.read()
        print(conteudo)
    
    

btn_ok = tk.Button(root, text='Guardar', command=guardar_contato)
btn_ok.pack()

btn_ver = tk.Button(root, text='Ver Contatos', command=exibir_contatos)
btn_ver.pack()
















root.mainloop()