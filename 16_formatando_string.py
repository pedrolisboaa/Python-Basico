"""
Manipulando Strings
* String indice
* Fatiamento [inicio:fim:passo]
*Funções build-in
"""

nome_completo = 'Olívia Oliveira Lisboa'
print(nome_completo[2])
print(nome_completo[-1])  # -1 pega a última letra

prime_nome = nome_completo[:6]
sobrenome = nome_completo[7:]
pulando = nome_completo[::2]
print(prime_nome)
print(sobrenome)
print(pulando)

print(len(nome_completo))
