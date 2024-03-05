import tkinter as tk
import sqlite3
from tkinter import messagebox


conn = sqlite3.connect('afonso.db')
c = conn.cursor()

c.execute('''CREATE TABLE if not exists pessoas
             (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sexo TEXT, telefone TEXT, email TEXT)''')

def inserir_dados():
    nome = nome_entry.get()
    sexo = sexo_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()
    c.execute("INSERT INTO pessoas (nome, sexo, telefone, email) VALUES (?, ?, ?, ?)", (nome, sexo, telefone, email))
    conn.commit()
    limpar_campos()
    c.execute("SELECT * FROM pessoas")
    rows = c.fetchall()
    for row in rows:
        id, nome, sexo, telefone, email = row
        texto.insert(tk.END, f"{id}: {nome}, {sexo}, {telefone}, {email}\n")
    messagebox.showinfo('Sucesso','Guardado') # .showinfo <-- mostra uma mensagem de informação


def exibir_dados():
    limpar_campos()
    c.execute("SELECT * FROM pessoas")
    rows = c.fetchall()
    for row in rows:
        id, nome, sexo, telefone, email = row
        texto.insert(tk.END, f"{id}: {nome}, {sexo}, {telefone}, {email}\n")


def atualizar_dados():
    try:
        id = id_entry.get()
        nome = nome_entry.get()
        sexo = sexo_entry.get()
        telefone = telefone_entry.get()
        email = email_entry.get()

        c.execute("UPDATE pessoas SET nome=?, sexo=?, telefone=?, email=? WHERE id=?", (nome, sexo, telefone, email, id))
        
        exibir_dados()
        
        conn.commit()
        messagebox.showinfo('Sucesso','Atualizado') # .showinfo <-- mostra uma mensagem de informação
    except:
        messagebox.showinfo('Erro','Ocorreu um erro ao atualizar os dados')
    finally:
        limpar_campos()
        id_entry.delete(0, tk.END)
        exibir_dados()
    
        
    
    
def apagar_dados():
    limpar_campos()
    try:
        id = id_entry.get()
        c.execute("DELETE FROM pessoas WHERE id=?", (id,))
        
        exibir_dados()

        messagebox.showinfo('Sucesso','Apagado') # .showinfo <-- mostra uma mensagem de informação

    finally:
        id_entry.delete(0, tk.END)
        


def limpar_campos():
    nome_entry.delete(0, tk.END)
    sexo_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    texto.delete(1.0, tk.END)
    
    
    
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