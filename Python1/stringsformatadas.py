'''
nome = "Joana"
apelido = "Santos"
idade = 17

# A Joana (Santos) tem 17 anos

# frase = "A " + nome + " ( " + apelido + " ) tem " + idade + " anos"
# print(frase)
# Dá erro Porque NAO SE PODE CONCATENAR STRINGS COM INTS

frase2 = "A " + nome + " (" + apelido + ") tem " + str(idade) + " anos"
print(frase2)

frase3 = f'A {nome} ({apelido}) tem {idade} anos'
print(frase3)
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = input("Indique um Nº: ")
for no in numeros:
    print(n + " X " + no + " = " + str(int(n) * no))