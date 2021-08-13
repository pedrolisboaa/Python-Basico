"""
Condições IF, ELIF e ELSE 
"""


if False:
    print('If verdadeiro')
    nome = 'Pedro'
    print(nome)
elif True:
    print('Elif verdadeiro')
    print('Tudo aqui é dentro do ELIF')
    if True:
        print('Dentro do dentro do elif')
    else: 
        print('Dentro do dentro mas com else!')
else:
    print('Else verdadeiro')
    print('Final das minhas condições com 3!')

print('-' * 20)
print('Chegamos ao final!')

    