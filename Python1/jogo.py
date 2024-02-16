class Avatar:
    def __init__(self, nome, energia, dinheiro=100):
        self.nome = nome
        self.energia = energia
        self.dinheiro = dinheiro
 
    def move_direita(self):
        self.energia -= 5
 
    def move_esquerda(self):
        self.energia -= 5
 
    def alimenta(self):
        self.energia += 5
        self.dinheiro -= 10
 
    def mostra_status(self):
        print('Nome: ', self.nome)
        print('Energia: ', self.energia)
        print('Dinheiro', self.dinheiro)
 
    def dinheiro(self):
        self.dinheiro += 100