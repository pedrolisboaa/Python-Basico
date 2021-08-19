"""
Operador ternário
"""

usuario_logado = True
idade = 20

msg = 'Usuário logado' if usuario_logado else 'Usuário precisa logar'
msg2 = 'Maior de idade' if idade >= 18 else 'Menor de idade'

print(msg)
print(msg2)

