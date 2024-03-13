from flask import Flask, request, session, render_template, redirect, url_for, flash
from mysql.connector import connect
from config import *


app = Flask(__name__) # Determinar Caminho Raiz Aplicação
app.config.from_pyfile('config.py') # Carregar Ficheiro de Configurações pelo ficheiro 'config.py'
app.secret_key = 'secret' # Definir chave secreta da Aplicação Flask -> Utilizado para Assinar Cookies

# previnir problemas com cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

def connect_to_database():
    return connect(
        user = mysql_database_user,
        password = mysql_database_password,
        host = mysql_database_host,
        database = mysql_database_db,
        # Caracteres Tugueses
        charset = 'utf8mb4',
        collation = 'utf8mb4_unicode_ci'
    )


@app.route('/')
def index():
    if 'user_id' in session and session['is_admin']:
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        return render_template('admin.html', users=users)
    elif 'user_id' in session:
        db = connect_to_database()
        cursor = db.cursor()
        user_id = session['user_id']
            
        cursor.execute('SELECT * FROM tarefas')
        tarefas = cursor.fetchall()
        return render_template('user.html', tarefas = tarefas)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s',(username, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['is_admin'] = user[4]
            return redirect(url_for('admin' if user[4] else 'user')) # se for admin vai para admin senao vai para user
        else:
            return render_template('login.html', error='Nome ou Palavra-Passe Incorreta!')    
    else:
        return render_template('login.html') # pagina de origem e sempre chamado de index
    
    

@app.route('/admin')
def admin():
    if 'user_id' in session and session['is_admin']:
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        return render_template('admin.html', users=users)
    else:
        return redirect(url_for('login'))


@app.route('/registo', methods = ['POST'])
def registo():
    if request.method == "POST":
        user = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        is_admin = request.form.get('is_admin')
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute('INSERT INTO users (username, password, email, is_admin) VALUES(%s, %s, %s, %s)', (user, password, email, is_admin))
        db.commit()
        return redirect(url_for('login'))
    else:
        return render_template('registo.html')


@app.route('/user', methods = ['GET', 'POST'])
def user():
    if 'user_id' in session and session['is_admin']:
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute('SELECT user_id, username FROM users WHERE is_admin = 0')
        users = cursor.fetchall()
        return render_template('adminTarefa.html', users = users)
        
        
    elif 'user_id' in session:
        db = connect_to_database()
        cursor = db.cursor()
        user = session['user_id']
        
        cursor.execute('SELECT tarefa_id, descricao, concluido FROM tarefas WHERE id_user = %s', (user,))
        tarefas = cursor.fetchall()
        return render_template('user.html', listaTarefas = tarefas)
    
    else:
        return redirect(url_for('login'))



@app.route('/userAdmin/<int:id_user>', methods = ['GET', 'POST'])
def userAdmin(id_user):
    if 'user_id' in session and session['is_admin']:
        db =  db = connect_to_database()
        cursor = db.cursor()
        user_id = id_user

        cursor.execute('SELECT tarefa_id, descricao, concluido, id_user FROM tarefas WHERE id_user = %s', (user_id,))
        tarefas = cursor.fetchall()
        return render_template('userAdmin.html', listaTarefas = tarefas)
    else:
        return redirect(url_for('user'))
    



@app.route('/adminTarefa/<int:id_user>', methods = ['GET', 'POST'])
def adminTarefa(id_user):
    if 'user_id' in session and session['is_admin']:
        db = connect_to_database()
        cursor = db.cursor()
        user = id_user
        cursor.execute('SELECT tarefa_id, descricao, concluido FROM tarefas WHERE id_user = %s', (user,))
        tarefas = cursor.fetchall()
        return render_template('userAdmin.html', tarefas = tarefas)

                          

@app.route('/updateUser/<int:id_user>',methods=['POST','GET'])
def updateUser(id_user):
    if 'user_id' in session and session['is_admin']:
        if request.method == 'POST':
            user_id = id_user
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            is_admin = request.form['is_admin']
            db = connect_to_database()
            cursor = db.cursor()
            cursor.execute("""
                   UPDATE users
                   SET username=%s, password=%s, email=%s, is_admin=%s
                   WHERE user_id=%s
                """, (username, password, email, is_admin, user_id))
            flash("Dados actualizados com sucesso!")
            db.commit()
            return redirect(url_for('admin'))


@app.route('/deleteUser/<int:user_id>', methods=['POST','GET'])
def deleteUser(user_id):
    if 'user_id' in session and session['is_admin']:
        if request.method == 'GET':
            id_user = user_id
            db = connect_to_database()
            cursor = db.cursor()
            try:
                cursor.execute("""
                    DELETE FROM users
                    WHERE user_id=%s
                """, (id_user,))
                flash("Dados actualizados com sucesso!")
                db.commit()
            except:
                flash("Erro ao Eliminar Utilizador! Utilizador tem tarefas associadas!")
            return redirect(url_for('admin'))
        return redirect(url_for('user'))
    


@app.route('/updateTarefa/<int:id>/<string:descricao>/<int:concluido>',methods=['POST','GET'])
def updateTarefa(id, descricao, concluido):
    if request.method == 'GET':
        id_tarefa = id
        desc = descricao
        conc = concluido
        if 'user_id' in session:
            db = connect_to_database()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE tarefas
                SET descricao=%s, concluido=%s
                WHERE tarefa_id=%s
             """, (desc, conc, id_tarefa,))
            flash("Dados actualizados com sucesso!")
            db.commit()
            return redirect(url_for('user'))
    return redirect(url_for('index'))



@app.route('/updateTarefaAdmin/<int:id>/<string:descricao>/<int:concluido>/<int:id_user>',methods=['POST','GET'])
def updateTarefaAdmin(id, descricao, concluido, id_user):
    if request.method == 'GET':
        id_tarefa = id
        desc = descricao
        conc = concluido
        user_id = id_user
        if 'user_id' in session:
            db = connect_to_database()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE tarefas
                SET descricao=%s, concluido=%s
                WHERE tarefa_id=%s
             """, (desc, conc, id_tarefa,))
            flash("Dados actualizados com sucesso!")
            db.commit()
            return redirect(url_for('userAdmin', id_user=user_id))
    return redirect(url_for('index'))


@app.route('/updateDesc',methods=['POST','GET'])
def updateDesc():
     if request.method == 'POST':
        id = request.form['id_tarefa']
        descricao = request.form['descricao']
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("""
            UPDATE tarefas
            SET descricao=%s
            WHERE tarefa_id=%s
         """, (descricao, id))
        flash("Dados actualizados com sucesso!")
        db.commit()
        return redirect(url_for('user'))
    
    
@app.route('/userAdmin/userAdminUpdateDescAdmin/<int:user_id>',methods=['POST','GET'])
def userAdminUpdateDescAdmin(user_id):
     if request.method == 'POST':
        id = request.form['id_tarefa']
        descricao = request.form['descricao']
        user = user_id
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("""
            UPDATE tarefas
            SET descricao=%s
            WHERE tarefa_id=%s
         """, (descricao, id))
        flash("Dados actualizados com sucesso!")
        db.commit()
        return redirect (url_for('userAdmin', id_user = user))   
    
    
@app.route('/deleteTaskUser/<int:tarefa_id>', methods=['POST','GET'])
def deleteTaskUser(tarefa_id):
    if 'user_id' in session:
            if request.method == 'GET':
                id_tarefa = int(tarefa_id)
                db = connect_to_database()
                cursor = db.cursor()
                cursor.execute("""
                    DELETE FROM tarefas
                    WHERE tarefa_id=%s
                 """, (int(id_tarefa),))
                flash("Dados actualizados com sucesso!")
                db.commit()
                return redirect(url_for('user'))
    return redirect(url_for('user'))


@app.route('/deleteTaskAdmin/<int:tarefa_id>/<int:user>', methods=['POST','GET'])
def deleteTaskAdmin(tarefa_id, user):
    if 'user_id' in session and session['is_admin']:
        if request.method == 'GET':
            id_tarefa = int(tarefa_id)
            user_id = user
            db = connect_to_database()
            cursor = db.cursor()
            cursor.execute("""
                DELETE FROM tarefas
                WHERE tarefa_id=%s
             """, (int(id_tarefa),))
            flash("Dados actualizados com sucesso!")
            db.commit()
            return redirect(url_for('userAdmin', id_user = user_id))
    
    
@app.route('/userAdmin/AddTask',methods=['POST','GET'])
def userAdminAddTask():
     if request.method == 'POST': 
        user_id = request.form['user_id']
        descricao = request.form['descricao']
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("INSERT INTO tarefas (descricao, concluido, id_user) VALUES(%s, 0, %s);", (descricao, int(user_id)))
        flash("Dados Adicionados com sucesso!")
        db.commit()
        return redirect(url_for('userAdmin', id_user = user_id))  
    
    
@app.route('/AddTask',methods=['POST','GET'])
def AddTask():
     if request.method == 'POST': 
        user_id = session['user_id']
        descricao = request.form['descricao']
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("INSERT INTO tarefas (descricao, concluido, id_user) VALUES(%s, 0, %s);", (descricao, user_id))
        flash("Dados Adicionados com sucesso!")
        db.commit()
        return redirect(url_for('user'))

    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True) # serve para quando em desenvolvimento verificar erros no codigo
                        # em produçao retirar o debug

