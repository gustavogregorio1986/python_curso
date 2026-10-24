""" Calculasdora com while """

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador: ')

    numeros_validos = None

    try:
      num_1_float = 0
      num_2_float = 0
      numeros_validos = True
    except Exception as error:
      numeros_validos = False

    if numeros_validos is None:
       print('um ou antes os números digitados são invalidos.')
       continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
       print('Operador inválido')
       continue

    if len(operador) > 1:
       print('Digite apenas um operador')
       continue

    if operador == '+':
       print(f'[num_1_float + num_2_float=]', num_1_float + num_2_float)
    elif operador == '-':
       print(f'[num_1_float - num_2_float=]',num_1_float - num_2_float)
    elif operador == '*':
       print(f'[num_1_float * num_2_float=]',num_1_float * num_2_float)
    elif operador == '/':
       print(f'[num_1_float / num_2_float=]',num_1_float / num_2_float)
    else:
       print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im ').lower().startswith('s')

    if sair is True:
       break