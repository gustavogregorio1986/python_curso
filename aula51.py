"""
Introdução ao desempácotamento + tuples (tuplas)
"""

nomes = ['Maria','Helena','Luiz']
nome1, nome2, nome3 = nomes
print(nome2)

nome1, nome2, nome3 =  ['Maria','Helena','Luiz']
print(nome2)

# nome1, nome2 =  ['Maria','Helena','Luiz']
# print(nome2)

nome1, *resto = ['Maria','helena','Luiz']
print(nome1, resto)