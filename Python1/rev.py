'''
resultado = {
    'teste': '01',
    'dono': 'Paulo',
    'quantidade': 30.0,
}
print(resultado)
'''
# Criar Função Criar(), em que ao Fornecer os Dados -> 02, Ana, 40.0 <- Ele crie teste2

# teste2 = criar('02', 'Ana', 40.0)

def criar(id, nome, numero):
     return  {
    'teste': id,
    'dono': nome,
    'quantidade': numero,
    }


teste2 = criar('02', 'Ana', 40.0)
print(teste2)