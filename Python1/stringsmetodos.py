nome = "Joana Santos"
print(len(nome)) # comprimento string
print(nome.upper()) # tudo MAIUSCULAS
print(nome.lower()) # tudo minusculas
print(nome.find('a')) # mostra posição primeiro 
print(nome.find('tos')) # mostra primeira posicao do primeiro caracter
print(nome.find('ks')) # mostra -1 pois não existe

contem1 = "Joana" in nome # guarda resposta da procura "Joana" no nome
print(contem1) # True se existir False se não existir

contem2 = "Jon" in nome # guarda resposta da procura "Joana" no nome
print(contem2) # True se existir False se não existir
