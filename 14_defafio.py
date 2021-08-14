
"""
Desafio - 1 Par ou Ímpar
"""

numero = input('Digite um número inteiro positivo: ')

if numero.isdigit():
	par_ou_impar = int(numero) % 2
	if par_ou_impar == 0:
		print(f'O número {numero} é par.')
	else:
		print(f'O número {numero} é ímpar.')
else:
	print('Dígite um número válido.')


"""
Desafio - 2 Horário super simples
"""

hora = float(input('Que horas são? '))

if hora >= 0 and hora <= 12:
	print('Bom dia!')
elif hora > 12 and hora <= 18:
	print('Boa tarde!')
elif hora <= 24 and hora > 0:
	print('Boa noite!')
else:
	print('Hora inválida.')

"""
Desafio - 3 tamanho do nome
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome < 5:
	print('Seu nome é muito curto!')
elif tamanho_nome < 7:
	print('Seu nome é normal')
else:
	print('Nome grande!')
