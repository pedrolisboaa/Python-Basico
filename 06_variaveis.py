Variaveis
"""
Inicia com letra, pode conter números, separar_, letra mínuscula
"""

nome = 'Pedro'
idade = 28
altura = 1.90
peso = 120
e_maior = idade >= 18

imc = peso / altura ** 2

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Altura: {altura}')
print(f'É maior dade idade: {e_maior}')
print(f'{nome} tem {idade}anos e seu IMC = {imc:.2f}')
