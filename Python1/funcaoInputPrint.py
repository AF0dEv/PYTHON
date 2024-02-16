nome = input('Qual é o seu Nome? ') # Faz Output a Frase, e Input da Resposta
print('Olá ' + nome)

nomeProf = input('Qual é o seu Nome? ')
corpref = input('Qual a sua cor Favorita? ')

frase = f'Olá {nomeProf} , a sua cor favorita é {corpref}'
print(frase)

anonascimento = input('Diga o seu ano de Nascimento ')
idade = 2023 - int(anonascimento) 
print('A sua Idade é ' + str(idade))
print('A sua Idade é', idade)
print(f'A sua Idade é {idade}')
print(idade)