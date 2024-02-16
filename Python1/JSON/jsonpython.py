'''
    JSON é um formato de Dados Leve e de Fácil Leitura utilizado para troca de Informações
entre sistemas computacionais.
    É utilizado para Transmitir dados entre Servidor e um Cliente em Aplicações WEB e Móveis.
'''

import json

d1 = {
    'Pessoa 1': {
    'nome': 'Luis',
    'idade': 25,
    },
    'Pessoa 2':{
    'nome': 'Rosa',
    'idade': 30,
    },
}
'''
print(d1)
print(d1['Pessoa 1'])
print(d1['Pessoa 2'])
'''

# Imprimir JSON
d1_json = json.dumps(d1)
print(d1_json)
d1_json = json.dumps(d1, indent= True)
print(d1_json)

# GUARDAR JSON em Ficheiro

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)