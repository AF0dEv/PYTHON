import sqlite3

# CRIAR BASE DE DADOS
bd = sqlite3.connect('primeiro_db.db') # tenta conectar, se nao houver, cria
# Este Comando cria uma Conexão com a BD SQLite chamado primeiro_db.db
# Cria a BD se ela não existir
# A Variavel 'bd' torna-se um Objeto de Conexão para ser Utilizado na Interação com a BD 

cursor = bd.cursor()

# CRIAR A TABELA
cursor.execute('CREATE TABLE IF NOT EXISTS Pessoa (nome TEXT, idade INTEGER, email TEXT)') # (nome de coluna + tipo de dados)
# Este Comando cria um Objeto associado a Conexão BD, o cursor é Utilizado para Executar Comandos SQL 

# INSERIR DADOS NA TABELA
cursor.execute('INSERT INTO Pessoa VALUES("Maria", 40, "maria@gmail.com")') # ATENÇÃO AS ASPAS

# FAZER UM COMMIT AOS DADOS PORQUE ESTAMOS A ESCREVER
bd.commit()

# LER OS DADOS
# o FetchAll é porque estamos a Ler
cursor.execute('SELECT * FROM Pessoa;')
print(cursor.fetchall())
