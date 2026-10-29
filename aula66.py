"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argkmento não nomeado recebe apenas o argumento (valor)
"""

# Definição
def soma(x, y, z):
    print(f'{x=} + {y} y={z}','|','x + y + z =',x + y + z)

soma(1,2, 3)
soma(2,1,5)
soma(y=2,z=3,x=5)
print(1,2,3, sep='-')