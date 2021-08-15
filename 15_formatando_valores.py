"""
Formatando valores com modificadores

:s texto
:d inteiro
:f número de ponto flutuante
:.(numero) - Qualquer quantidade de casas decimais
:(caractere) (> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'Pedro Henrique'
print(f'{nome:s}')

numero_novo = 1
nome_novo = 'Pedro Lisboa'
print(numero_novo)
print(f'{numero_novo:0>10}')
print(f'{numero_novo:+<10}')
print(f'{numero_novo:_^10}')
print(f'{nome:&^50}')

nome_formatado = '{:#<20}'.format(nome)
print(nome_formatado)

nome_estranho = 'Pedro lisBoA'
print(nome_estranho.lower())
print(nome_estranho.upper())
print(nome_estranho.title())
print(nome_estranho.capitalize())
