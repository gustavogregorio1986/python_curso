"""

Retorno de valores das funções (return)
"""
variavel = print('Luiz')

print(variavel is None)

def soma(x, y):
     print('Olha')
     print('só')
     print('que')
     print('legal')
     return x + y

def soma(x, y):
     if x > 10:
         return 10,20 
     return x + y

# variavel = soma(1, 2)
# variavel = int('1')
# print(variavel)

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)
