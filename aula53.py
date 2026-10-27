"""
enumerate - enumera iteráveis (indices)
"""

lista = ['Maria','Helena','Luiz']
lista.append('Joao')

lista_enumerada = enumerate(lista)

print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)

    