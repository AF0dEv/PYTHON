from flask import Flask, request,  render_template
import openpyxl
import os
import time

# app é a Instância que Representa o Aplicativo Flask
app = Flask(__name__) # Criar Estância da Classe Flask, onde o Argumento __name__ é Utilizado para Identificar o Aplicativo

# 1 ª Rota, rota mais baixa do nosso programa
@app.route('/', methods = ['GET', 'POST']) # GET -> serve para enviar dados por URL 
def index():
    if request.method == 'POST': # POST -> serve para enviar dados encapsulados
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
    
    # Verificar se Ficheiro já Existe
        if os.path.exists('Contacts.xlsx'):
            wb = openpyxl.load_workbook('Contacts.xlsx') # quando ja existe
            ws = wb.active
            ws.append([name, email, message])
        else:
    # Se Ficheiro Não Existir
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.append([name, email, message]) 
        
    # Guardar as Alterações
        wb.save('Contacts.xlsx')
        time.sleep(2)
        
        
        return render_template('contacts.html', success_massage = 'Dados Enviados com Sucesso!')
    return render_template('contacts.html')

if __name__ == '__main__': # __name__ -> Variável Especial do Python, Utilizado para Verificar se o Ficheiro está a ser Executado como Independente e Não um Módulo 
    app.run(debug = True)