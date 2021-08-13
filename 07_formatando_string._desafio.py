
from datetime import date

nome = 'Pedro Lisboa'
idade = 28
altura = 1.90
peso = 130
ano_atual = date.today().year
ano_nascimento = ano_atual - idade
imc = (peso / altura ** 2)

print(f'{nome} nasceu em {ano_nascimento} portanto tem {idade} anos')
print(f'Seu peso e de {peso}kg e sua altura {altura} m seu imc = {imc:.2f}')
print('Teste : é è ç ^ ã ê ')


