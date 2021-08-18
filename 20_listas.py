"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

var1 = 'Cachorro'
var2 = 'Azul'
var3 = 'Banana'
var4 = 'Coca cola'

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numeros2 = list(range(0, 50))
lista_nomes = ['Pedro', 'Juliana', 'Marcia', 'Olívia']
lista_variaveis = [var1, var2, var3, var4]

# print(lista_nomes[-1])
# print(lista_variaveis[::-1])

# print(lista_nomes)
# print(lista_variaveis)
#
# lista_numeros.append(11)
# print(lista_numeros)
#
# lista_nomes.insert(0, 'Ana')
# print(lista_nomes)
#
# lista_numeros.pop()
# print(lista_numeros)
#
# del(lista_numeros[3:5])
# print(lista_numeros)

print(max(lista_numeros))
print(min(lista_numeros))
print(sum(lista_numeros))

# for valor in lista_numeros2:
#     print(valor ** valor)

palavra_secreta = 'churrasco'
digitadas = []
chance = 3

while True:
    if chance <= 0:
        print('Você perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite somente uma letra!')
        continue

    digitadas.append(letra)
    print(digitadas)

    if letra in palavra_secreta:
        print(f'UHUUUL, a letra {letra} existe na palavra.')
    else:
        print(f'AFFF, a letra {letra} não existe na palavra')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavra_secreta:
        print(f'Legal você ganhou! A palavra era {palavra_secreta}')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}')

    if letra not in palavra_secreta:
        chance -= 1

    print(f'Você ainda tem {chance} chances.')
    print()

    print(secreto_temporario)
print('FIM')