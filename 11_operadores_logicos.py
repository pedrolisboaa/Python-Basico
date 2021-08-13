"""
Operadores lógicos
and, or, not
in e not in
"""
import getpass

a = 1
b = 2
c = 3
d = 4
vazia = ''
nome = 'Pedro Lisboa'

print(a == 1 and b > a)
print(a != d or c != c)
print(a != a or c == d)
print(not (a == a))
print(a == a)

if not vazia:
    print('Esta vazia')

print('o' in nome)
print('o' not in nome)

# getpass funciona somente no terminal
usuario = input('Digite seu usuario: ')
senha = getpass.getpass('Digite sua senha: ')

usuario_bd = 'pizza-grande'
senha_bd = '12345'

verificacao1 = usuario == usuario_bd
verificacao2 = senha == senha_bd

if verificacao1 and verificacao2:
    print(f'Seja bem vindo {usuario}.')
else:
    print(f'Usuário ou senha inválidos.')
