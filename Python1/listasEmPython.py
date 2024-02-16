age = [10, 15, 8, 9, 17]
print(age)
name = ["Marcos", "Joana", "Pedro", "Ana", "Rita"]
print(name)
print(name[1])
print(name[-1])
print(name[1:3])
print(name[2][0]) # Caracter 0 do nome na posição 2

name[2] = 'Maria'
print(name)

name.append("Pedro")
print(name)

for names in name:
    print(names)

for letters in 'Afonso':
    print(letters)
    print('=' * 6)

for num2 in range(5):
    print(num2)
    print('=' * 6)

for num3 in range(2,5):
    print(num3)
    print('=' * 6)

for num4 in range(2,10, 2):
    print(num4)
    print('=' * 6)

Lista = name + age
print(Lista)

if 'Marcos' in name:
    print('sim')