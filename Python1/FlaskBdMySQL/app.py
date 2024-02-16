from flask import Flask, request, session, render_template, redirect, url_for
from mysql.connector import connect
from config import *

app = Flask(__name__) # Determinar Caminho Raiz Aplicação
app.config.from_pyfile('config.py') # Carregar Ficheiro de Configurações pelo ficheiro 'config.py'
app.secret_key = 'secret' # Definir chave secreta da Aplicação Flask -> Utilizado para Assinar Cookies

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


@app.route('/') # direcionar pagina para raiz
def index(): # pagina de origem e sempre chamado de index
    return 'Olá Mundo!'


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users where username = %s and password = %s',(username, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['is_admin'] = user[4]
            return redirect(url_for('admin' if user[4] else 'user')) # se for admin vai para admin senao vai para user
        else:
            return render_template('login.html', error='Nome ou Palavra-Passe Incorreta!')    
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('index'))

@app.route('/user')
def user():
    if 'user_id' in session:
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        return render_template('user.html', users= users)
    else:
        return redirect(url_for('login'))



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

@app.route('/registo', methods = ['GET', 'POST'])
def registo():
    if request.method == "POST":
        user = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        is_admin = request.form.get('tipo')
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute('INSERT INTO users (username, password, email, is_admin) VALUES(%s, %s, %s, %s)', (user, password, email, is_admin))
        db.commit()
        return admin()
    else:
        return render_template('registo.html')



if __name__ == '__main__':
    app.run(debug=True) # serve para quando em desenvolvimento verificar erros no codigo
                        # em produçao retirar o debug



