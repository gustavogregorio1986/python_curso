# Desempacotamento em chamadas
# de metodos e funções
string = 'ABCD'
lista = ['Maria','Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python','é', 'legal'

a, b, c, *_ = lista
p, b, *_, ap, u = lista
print(a, c)
print(p, u, ap)

for nome in lista:
    print(nome, end=" ")

print(*lista)

print(*string)