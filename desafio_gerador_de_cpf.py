"""
Gerador de CPF
"""
from random import randint

cpf = str(randint(100000000, 999999999))

valor_primeira_verificacao = []
valor_segunda_verificacao = []

# primeira verificação
for v1, v2 in enumerate(range(10, 1, -1)):
    valor_primeira_verificacao.append(int(cpf[v1]) * v2)

primeira_soma = sum(valor_primeira_verificacao)
primeiro_resultado = primeira_soma * 10 % 11

if primeiro_resultado == 10:
    primeiro_resultado = 0
cpf += str(primeiro_resultado)

# Segunda verificação
for v1, v2 in enumerate(range(11, 1, -1)):
    valor_segunda_verificacao.append(int(cpf[v1]) * v2)

segunda_soma = sum(valor_segunda_verificacao)
segundo_resultado = segunda_soma * 10 % 11

if segundo_resultado == 10:
    segundo_resultado = 0
cpf += str(segundo_resultado)

# Finalizando
print(f'Novo CPF gerado {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}')

