import random

num1 = random.randint(1, 6)
print("Vou pensar em um numero entre 1 e 6. Tente advinhar...")

tentativas = 0
print(num1)
while tentativas < 3:
    tentativas += 1
    num = int(input("Digite um numero Para Adivinhar: "))
    print("PROCESSANDO...")
    if num == num1:
        print("ACERTOU")
        break
else:
    print("PERDEU, SEM TENTATIVAS.")
    print(f'O numero era {num1}')
