num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

#isnumeric isdigit isdecimal

#isnumeric - somente positivos inteiros 

if num1.isdigit() and num2.isdigit():
	print(int(num1) + int(num2))
else:
	print('Erro!')
