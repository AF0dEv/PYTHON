from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'iefp crud'

app.config['MYSQL_HOST'] = '62.28.39.135'
app.config['MYSQL_USER'] = 'Raquel'
app.config['MYSQL_PASSWORD'] = 'Silva1234'
app.config['MYSQL_DB'] = 'flask_app'


mysql = MySQL(app)


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('index2.html', accounts=data )


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Registo apagado com sucesso!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE users
               SET username=%s, password=%s, email=%s
               WHERE id=%s
            """, (username, password, email, id_data))
        flash("Dados actualizados com sucesso!")
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
