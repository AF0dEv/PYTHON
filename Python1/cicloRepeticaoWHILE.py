"""
while condiçao:
    instrução1
    instruçao2
    instruçao3
    break
else:
    instrução
instrução
"""
'''
n = 1

while n <= 5:
    print(n)
    n += 1
    if n == 6:
        break  # Quando o IF for Verdadeiro, vai Parar o Programa e vai para o Ultimo Print
else:  # Se nao tiver BREAK ou a Condição do While for False, corre sempre o Else
    print('Fim do ciclo WHILE')
print('Fim do Programa.')
'''

n = input("Insira um Nº para começar: ")
while int(n) <= 30:
    print(n)
    n = int(n) + 3
    if int(n) > 30:
        break
    
print("Fim do Programa")