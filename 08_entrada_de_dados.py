"""
Entrada de dados
"""
from datetime import date

nome = input('Qual é seu nome? ')
idade = input('Qual sua idade? ')
ano_nascimento = date.today().year - int(idade)

print()
print(f'Olá {nome} você tem {idade} anos!')
print(f'{nome} nasceu em {ano_nascimento}.')


numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

print(int(numero1) + int(numero2))