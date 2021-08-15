"""
while
"""

# contador = 0
# while True:
#     contador += 1
#     print(contador)
#     if contador == 1000:
#         break
#
# print('Fim do while')
#
# flag = 2
# while flag < 1000000:
#     flag *= flag
#     print(flag)

while True:
    numero_1 = input('Digite um número inteiro positivo: ')
    numero_2 = input('Digite outro inteiro positivo: ')
    operador = input('Digite um operador - "*" "/" "+" "-": ')

    if not numero_1.isdigit() and not numero_2.isdigit():
        print('Você digitou um número errado.')
        break

    numero_1 = int(numero_1)
    numero_2 = int(numero_2)

    if operador == '*':
        print(f'{numero_1} * {numero_2} = {numero_1 * numero_2}')
    elif operador == '/':
        print(f'{numero_1} / {numero_2} = {numero_1 / numero_2}')
    elif operador == '+':
        print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')
    elif operador == '-':
        print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')
    else:
        print('Seu operador é invalido.')
