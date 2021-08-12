"""
Formando String
Utilizando f String
"""

nome = 'Pedro'
idade = 28
altura = 1.90
peso = 120
e_maior = idade >= 18
imc = peso / altura ** 2

print(f"Ola me chamo {nome} e tenho {idade} anos!")
print('Meu peso é {} tenho {}m de altura e meu IMC: {:.2f}'.format(peso, altura, imc))
