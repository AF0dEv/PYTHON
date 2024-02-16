import tkinter as tk
import sqlite3

janela = tk.Tk()
janela.title('AGENDA')

# Conectar com BD
conn = sqlite3.connect('agenda_db.db')

# Criar ENTRADAS
nome_entry = tk.Entry(janela)
idade_entry = tk.Entry(janela)
email_entry = tk.Entry(janela)
lista = tk.Listbox(janela)
id_entry = tk.Entry(janela)

# Criar RÓTULOS
nome_label = tk.Label(janela, text='Nome')
idade_label = tk.Label(janela, text='Idade')
email_label = tk.Label(janela, text='Email')
id_label = tk.Label(janela, text='ID')

# Criar Tabela
conn.execute('''CREATE TABLE IF NOT EXISTS Pessoa (nome TEXT, idade INTEGER, email TEXT)''')

def limpar_lista():
    try:
        lista.delete(0, tk.END)       
    except: 
        print('Problemas a Apagar Lista')



def adicionar_registo():
    nome = nome_entry.get()
    idade = idade_entry.get()
    email = email_entry.get()
    
    # INSERIR DADOS NA TABELA
    conn.execute('INSERT INTO Pessoa (nome, idade, email) VALUES(?, ?, ?)', (nome, idade, email)) # ATENÇÃO AS ASPAS

    # FAZER UM COMMIT AOS DADOS PORQUE ESTAMOS A ESCREVER
    conn.commit()
   
    
def exibir_registos():
    cursor = conn.execute('SELECT rowid, nome, idade, email FROM Pessoa')
    resultados = cursor.fetchall()
    limpar_lista()
    for resultado in resultados:
        id = resultado[0]
        nome = resultado[1]
        idade = resultado[2]
        email = resultado[3]
        lista.insert(tk.END, f'{id} ,{nome}, {idade}, {email}')


def atualizar_txt():
    id = id_entry.get()
    cursor = conn.execute('SELECT * FROM Pessoa WHERE rowid LIKE (' + id + ')')
    registos = cursor.fetchall()
    for registo in registos:
        nome = registo[0]
        idade = registo[1]
        email = registo[2]
        nome_entry.delete(0,tk.END)
        nome_entry.insert(0, nome)
        idade_entry.delete(0,tk.END)
        idade_entry.insert(0,idade)
        email_entry.delete(0,tk.END)
        email_entry.insert(0,email)


def atualizar_lista():
    nome = nome_entry.get()
    idade = idade_entry.get()
    email = email_entry.get()
    id = id_entry.get()    
    conn.execute('UPDATE Pessoa SET nome = ?, idade = ?, email = ? WHERE rowid = ?', (nome, idade, email, id))
    conn.commit()


def excluir_registo():
    try:
        linha = lista.get(lista.curselection())
        id = linha[0:linha.index(',')]
        print(id)
        conn.execute('DELETE FROM Pessoa WHERE rowid LIKE (' + id + ')')
        conn.commit()
    except:
        print('Erro de Remoção')
        
           
    
# Criar BOTÕES
adicionar_btn = tk.Button(janela, text='Adicionar', command=adicionar_registo, cursor="pirate")
exibir_btn = tk.Button(janela, text='Exibir Registos', command=exibir_registos, cursor="spider")
atualizar_btn = tk.Button(janela, text='Atualizar Lista', command=atualizar_lista, cursor="heart")
excluir_btn = tk.Button(janela, text='Excluir', command=excluir_registo, cursor="man")
limpar_btn = tk.Button(janela, text='Limpar Lista', command=limpar_lista, cursor="star")


# Adicionar RÓTULOS e ENTRADAS nas Janelas
nome_label.pack()
nome_entry.pack()
idade_label.pack()
idade_entry.pack()
email_label.pack()
email_entry.pack()
lista.pack()


# Adicionar BOTÕES à Janela
adicionar_btn.pack()
atualizar_btn.pack()
excluir_btn.pack()
exibir_btn.pack()
limpar_btn.pack()


id_label.pack()
id_entry.bind("<Return>", lambda event: atualizar_txt())
id_entry.pack()







# CORRER PROGRAMA
janela.mainloop()