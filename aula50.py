"""
Exercicio
Exiba os indices da lista
"""

lista = ['Maria','Helena','Luiz']

for index, nome in enumerate(lista):
    print(index, nome)

print("Segunda solução")

for i in range(len(lista)):
    print(i, lista[i])