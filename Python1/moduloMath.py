a = 7.4
b = 7.6
c = -7.6
print(round(a)) # Arredondar, se for Menor que 5 arredonda para BAIXO
print(round(b)) # Arredondar, se for Maior ou Igual a 5 arredonda para CIMA
print(abs(c)) # Calcula o valor Absoluto

from math import ceil, floor, pi # Importa Apenas os Métodos Pretendidos
# Ao usar assim, não precisamos usar "Math." antes dos métodos
# EX: 
# import math
# math.ceil(), math.floor(), math.pi() 

print(ceil(a)) # Arrendondar, CEIL para CIMA
print(ceil(b)) # Arrendondar, CEIL para CIMA
print(floor(a)) # Arrendondar, FLOOR para BAIXO
print(floor(b)) # Arrendondar, FLOOR para BAIXO
print(pi) # Valor Pi