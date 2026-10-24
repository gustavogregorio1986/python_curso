"""
Introidução ao try/catch
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# numero = input('Vou dobrar o número que você digitar: ')

# num_float = float(numero)
# print(f'O dobro de {numero} é {num_float * 2:.0f}')

try:
    numero = input('Vou dobrar o número que você digitar: ')

    num_float = float(numero)
    print(f'O dobro de {numero} é {num_float * 2:.0f}')
except:
    print('Isso não é um numero')

