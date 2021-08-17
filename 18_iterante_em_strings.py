frase = 'O rato roeu a rica roupa do rei de Roma! A rainha raivosa rasgou o resto e depois resolveu remendar!'
tamanho_frase = len(frase)
contador = 0
nova_string = ""

letra_usuario = input('Qual letra deseja deixar maiscula:')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == letra_usuario:
        nova_string += letra_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)