frase = 'Hoje está sol'
print(frase[0]) # Ao Colocar o index[0], ele Mostra a Letra na Posição 0
print(frase[0:6]) # Ao Colocar o index[0:6], estamos a dizer que queremos ver todas as letras da posição 0 até 6
print(frase[:6]) # Se omitir o 0, o python assume como se tivesse um 0
print(frase[6:]) # Se omitir a posição final, o python assume que vai do 6 até ao Final 
print(frase[-2:]) # Neste caso vai contar de trás para a frente
fraseinverso = frase[::-1] # Guarda frase invertida
print(fraseinverso)
print (len(frase)) # Neste caso, mostra um inteiro que corresponde ao tamanho da string