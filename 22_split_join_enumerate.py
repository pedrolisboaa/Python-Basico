"""
Split, join, enumerate
* split - dividir uma string
* join - juntar uma string
* enumerate - enumerar elementos da lista
"""

# string = 'Velho coloca R$50,00 no macaco, vai ser na cabeça. Velho coloca macaco'
# lista_1 = string.split(",")
# lista_2 = string.split(" ")
# lista_vazia = []
#
# print(lista_1)
# print(lista_2)
#
# palavra = ''
# contagem = 0
# for valor in lista_2:
#     qtd_vezes = lista_2.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} apareceu ({contagem})x')

# nome = '   Pedro henrique lisboa    '
# print(nome)


# nome = 'Pedro Henrique do Nascimento Lisboa'
# print(nome)
# lista_nome = nome.split(' ')
# print(lista_nome)
# nome2 = '#'.join(lista_nome)
# print(nome2)

string = 'Minha filha amo a boneca'
frase = string.split(' ')

print(frase)

for indice, valor_da_lista in enumerate(frase):
    print(f'{indice} = {valor_da_lista}')

