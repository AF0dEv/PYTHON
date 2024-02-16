from jogo import Avatar

nome = 'Joana'
p1 = Avatar(nome, 100)
p2 = Avatar('Rita', 100)

print(type(nome))
print(type(p1))

p1.move_direita()
p2.move_esquerda()

p1.nome = 'Joana'
p2.nome = 'Rita'

print(p1.nome)