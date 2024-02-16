import mysql.connector

conexao = mysql.connector.connect(
    host = '62.28.39.135',
    user = 'Raquel',
    password = 'Silva1234',
    database = 'dbafonsomysqlpy'
)

cursor = conexao.cursor()

#CRUD

# CREATE
def create():
    strSQL = "INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)"

    values = ("Chocolate", 4)

    cursor.execute(strSQL, values)

    conexao.commit() # Editar BD


# READ
def read():
    strSQL = 'SELECT * FROM vendas'
    cursor.execute(strSQL)
    registos = cursor.fetchall()
    # resolver saber o que registos da return para condicionar atribuiçao de valores
    if  registos :
        for registo in registos:
            id = registo[0]
            nome_produto = registo[1]
            valor = registo[2]
    print(f'{id} ,{nome_produto}, {valor}')


# UPDATE
def update():
    read()
    id = input('Introduza o ID do Produto a Atualizar: ')
    nome_produto = input('Introduza o novo nome do Produto: ')
    valor = input('Introduza o Valor do novo Produto: ')
    strSQL = f'UPDATE vendas SET nome_produto = "{nome_produto}", valor = "{valor}" WHERE idvendas = {id};' 
    cursor.execute(strSQL)
    conexao.commit() # Editar BD


# DELETE
def delete():
    read()
    id = input('Introduza o ID do Produto a Remover: ')
    strSQL = f'DELETE FROM vendas WHERE idvendas = "{id}"'
    cursor.execute(strSQL)
    conexao.commit()
    read()
 
 
 
 # EXECUTAR   
update()   
delete()    
cursor.close()
conexao.close()