import requests

link = 'https://APIFONSO.ElAfonsoProgram.repl.co/totalvendas'

requisicao = requests.get(link)
print(requisicao)