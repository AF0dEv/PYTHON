'''
idade = input('Diga a sua Idade: ')

if int(idade) < 18:
    print('Ainda não tens Idade para tirar a Carta')
    print('Espera mais algum Tempo.')
    
elif condição:
    instruçao
elif condição:
    instrução 
    
else:
    print('Podes tirar a Carta')

# -----------------------------------------------------------------------------------

nota = int(input('Qual a nota do teste? '))
if nota < 50:
    print('Insuficiente')
elif 50 < nota < 70:
    print('Suficiente')
elif 70 < nota < 90:
    print('Bom')
else:
    print('Muito Bom')

# OPERADORES LÓGICOS -> AND / OR / NOT

domigo_faz_sol = True
tenho_boleia = True

if domigo_faz_sol and tenho_boleia: # Tem que ser as Duas Condições Verdadeiras
    print('Vou à Praia')
else:
    print('Fico em Casa')


if domigo_faz_sol or tenho_boleia: # Tem que ser pelo menos Uma Condição Verdadeira
    print('Vou à Praia')
else:
    print('Fico em Casa')


if domigo_faz_sol and not tenho_boleia: 
    print('Vou à Praia')
else:
    print('Fico em Casa')

# OPERADORES DE COMPARAÇÃO
# < MENOR
# > MAIOR
# <= MENOR/IGUAL
# >= MAIOR/IGUAL
# == IGUAL
# != DIFERENTE
'''
pswd = input('Qual é a sua password? ')
if len(pswd) < 6 or len(pswd) > 15:
    print('A Password não é Válida ')
else:
    print('A Password foi Aceite.')