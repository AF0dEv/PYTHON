import random
from jogo import Avatar
 
print('########################################################')
nomeP1 = input('Introduza o nome da primeira personagem:')
nomeP2 = input('Introduza o nome da segunda personagem:')
print('########################################################')
 
p1 = Avatar(nomeP1, random.randint(20, 100))
p2 = Avatar(nomeP2, random.randint(20, 100))
 
print('---------------------------')
p1.mostra_status()
print('---------------------------')
p2.mostra_status()
print('---------------------------')
 
print('########################################################')
print('Perde 5 energia ao movimentar..')
p1.move_direita()
p2.move_direita()
print('Energia atual P1:', p1.energia)
print('Energia atual P2:', p2.energia)
print('########################################################')
 
i = 0
while i <= 1:
    p1.alimenta()
    p2.alimenta()
    i += 1
else:
    print('A aumentar a energia em 10 a troco de 20 dinheiro..')
 
print('########################################################')
print('---------------------------')
p1.mostra_status()
print('---------------------------')
p2.mostra_status()
print('---------------------------')
print('########################################################')