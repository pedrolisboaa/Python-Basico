"""
Validador de CPF
"""

while True:
    cpf = input('Digite um CPF: ')

    if not cpf.isdigit():
        print('O cpf deve ter somente número')
        continue

    if len(cpf) != 11:
        print('O CPF deve ter 11 dígitos.')
        continue

    novo_cpf = str(cpf[0:9])

    valor_primeira_verificacao = []
    valor_segunda_verificacao = []

    # primeira verificação
    for v1, v2 in enumerate(range(10, 1, -1)):
        valor_primeira_verificacao.append(int(cpf[v1]) * v2)

    primeira_soma = sum(valor_primeira_verificacao)
    primeiro_resultado = primeira_soma * 10 % 11

    if primeiro_resultado == 10:
        primeiro_resultado = 0
    novo_cpf += str(primeiro_resultado)

    # Segunda verificação
    for v1, v2 in enumerate(range(11, 1, -1)):
        valor_segunda_verificacao.append(int(cpf[v1]) * v2)

    segunda_soma = sum(valor_segunda_verificacao)
    segundo_resultado = segunda_soma * 10 % 11

    if segundo_resultado == 10:
        segundo_resultado = 0
    novo_cpf += str(segundo_resultado)

    # Finalizando
    if cpf == novo_cpf:
        print(f'O cpf {cpf} é válido.')
        continuar = input('Digite fazer uma nova validação: [S]IM / [N]ÃO: ').lower().strip()
        if continuar != 's':
            print('Obrigado volte sempre!')
            break
    else:
        print(f'O cpf {cpf} é inválido.')
