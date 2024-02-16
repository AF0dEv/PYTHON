# Programa Encontra o Maior Lista

numbers = [1, 21, 30, 44, 75, 96, 27, 68, 39, 10]

maior = 0
for number in numbers:
    if number > maior:
        maior = number

print(str(maior))