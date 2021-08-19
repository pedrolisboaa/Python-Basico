"""
Desempacotamento Listas
"""

lista = ['Pedro', 'Juliana', 'Olívia', 1, 2, 7 ,3, 5,'churrasco', 'último da lista']
n1, n2, *outra_lista,comida, ultimo_da_lista = lista

print(n2)
print(outra_lista)
print(ultimo_da_lista)
print(comida)