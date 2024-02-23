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
        cursor.execute('SELECT username FROM users WHERE is_admin = 0')
        users = cursor.fetchall()
        return render_template('adminTarefa.html', users = users)
        
        
    elif 'user_id' in session:
        db = connect_to_database()
        cursor = db.cursor()
        user = session['user_id']
        
        cursor.execute('SELECT tarefa_id, descricao, concluido FROM tarefas WHERE id_user = %s', (user,))
        tarefas = cursor.fetchall()
        return render_template('user.html', tarefas = tarefas)
    
    else:
        return redirect(url_for('login'))


@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("""
               UPDATE users
               SET username=%s, password=%s, email=%s
               WHERE id=%s
            """, (username, password, email, id_data))
        flash("Dados actualizados com sucesso!")
        db.commit()
        return redirect(url_for('Index'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True) # serve para quando em desenvolvimento verificar erros no codigo
                        # em produçao retirar o debug
