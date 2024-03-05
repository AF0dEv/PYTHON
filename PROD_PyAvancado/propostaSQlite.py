import tkinter as tk
import sqlite3

conn = sqlite3.connect('marcos.db')
c = conn.cursor()

c.execute('''CREATE TABLE if not exists pessoas
             (nome TEXT, sexo TEXT, telefone TEXT, email TEXT)''')

def inserir_dados():
    print('Producao')

def exibir_dados():
    print('Producao')

def atualizar_dados():
    print('Producao')

def apagar_dados():
    print('Producao')

def limpar_campos():
    print('Producao')
    
janela = tk.Tk()
janela.title("Agenda")

nome_label = tk.Label(janela, text="Nome")
nome_entry = tk.Entry(janela)

sexo_label = tk.Label(janela, text="Sexo")
sexo_entry = tk.Entry(janela)

telefone_label = tk.Label(janela, text="Telefone")
telefone_entry = tk.Entry(janela)

email_label = tk.Label(janela, text="Email")
email_entry = tk.Entry(janela)

id_label = tk.Label(janela, text="Id")
id_entry = tk.Entry(janela)

inserir_button = tk.Button(janela, text="Inserir", command=inserir_dados)

exibir_button = tk.Button(janela, text="Exibir", command=exibir_dados)

atualizar_button = tk.Button(janela, text="Atualizar", command=atualizar_dados)

apagar_button = tk.Button(janela, text="Apagar", command=apagar_dados)

texto = tk.Text(janela, height=20, width=60)

nome_label.grid(row=0, column=0)
nome_entry.grid(row=0, column=1)

sexo_label.grid(row=1, column=0)
sexo_entry.grid(row=1, column=1)

telefone_label.grid(row=2, column=0)
telefone_entry.grid(row=2, column=1)

email_label.grid(row=3, column=0)
email_entry.grid(row=3, column=1)

id_label.grid(row=0, column=4)
id_entry.grid(row=1, column=4)

inserir_button.grid(row=2, column=3)
atualizar_button.grid(row=2, column=4)
apagar_button.grid(row=3, column=4)
exibir_button.grid(row=3, column=3)

texto.grid(row=5, columnspan=6, padx=20, pady=20)

janela.mainloop()

conn.close()
