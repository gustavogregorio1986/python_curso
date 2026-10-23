# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
else:
    print('Senha Incorreta')

senha = input('Senha: ')

if senha != '123456':
    print('Senha Incorreta')

print(not 0)
print(not 1123456)