"""
Operadores Relacionais
== > >= < <= !=
"""
"""
print(2 == 2)
print(2 < 2)
print(2 <= 2)
print(2 >= 2)
print(2 > 2)
print(2 == '2')
print(2 != '2')

num1 = 'dez'
num2 = 10

expressao = num1 == num2
print(expressao)
expressao2 = num1 != num2
print(expressao2)

nome = 'juliana'
nome1 = 'Juliana'
print(nome == nome1)
print(nome.upper() == nome1.upper())

"""

idade_minima_emprestimo = 25
idade_maxima_emprestimo = 50

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

#  idade >= idade_minima_emprestimo and idade <= idade_maxima_emprestimo:
if idade_minima_emprestimo <= idade <= idade_maxima_emprestimo:
    print(f'{nome.capitalize()} pode pegar um emprestimo.')
else:
    print(f'{nome.capitalize()} não pode pegar um emprestimo.')




