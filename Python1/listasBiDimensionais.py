'''[
    1 2 3
    4 5 6
    7 8 9
]'''

matriz = [ # Listas dentro de lista
    [1, 2, 3], # = [1, 2, 3], [4, 5, 6], [7, 8 , 9]
    [4, 5, 6],
    [7, 8, 9]
]
'''
print(matriz)

print(matriz[0])
print(matriz[1])
print(matriz[2])


print(matriz[0][1])
print(matriz[0][0])

for l in range(3):
    for c in range(3):
        print(matriz[l][c])
'''
'''
# MÉTODOS EM LISTAS

numeros = [1, 3 ,5 , 4, 9, 7]
print(numeros)

numeros.append(9) # Acrescenta 9 ao final da lista
print(numeros)

numeros.insert(0, 6) # Acrescenta na posição zero (ou outra) 
print(numeros)

n2 = numeros.copy() # Copia lista para variavel n2 (ou outra)
print(n2)

numeros.sort() # Ordenar lista forma CRESCENTE
print(numeros)

numeros.reverse()
print(numeros) # Ordenar ordem DECRESCENTE

print(numeros.count(9)) # Contar ocorrência de certo número

print(numeros.index(9)) # Dá a posiçao do primeiro a encontrar

numeros.sort()
print(numeros.pop()) # Retira o Último elemento da lista e Retorna o nr retirado
print(numeros)

encontrar = 8 in numeros
print(encontrar) # dá falso pois não existe
'''

# Dada uma determinada Lista,
# Com vários números,
# Deverá ser criado um programa que remova os Duplicados

n1 = [1, 3, 9, 2, 5, 4, 3, 9, 7, 1]
x = []
print(x)

for n in n1:

    if n not in x:
        x.append(n)

''' x = list(dict.fromkeys(n1)) ''' # Outra maneira de Fazer
''' n1 = list(set(n1)) ''' # outra maneira, Ordena e Limpa os Duplicados


print(n1)
print(x)
