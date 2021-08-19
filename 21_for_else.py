
variavel = ['Batata', 'Alura', 'Melancia']


for valor in variavel:
    if valor.upper().startswith('J'):
        print('Existe palavra que começa com J')
        break
else:
    print('Não existe uma palavra que começa com J')

