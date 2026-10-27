"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Coppnhecimentos reutilizaveis - indices e fatiamento
Metodos úteis:
   append, insert, pop, del, clear, extend, +
create read update Delete
Criara, ler, aleterare, apagar = lista[i] CRUD
"""

lista = [10, 20, 30, 40]
numero = lista[2]
lista[2] = 300
print(numero)
print(lista[2])
del lista[2]
print(lista[2])

lista.append(50)

print(lista)

lista.append(60)
lista.pop()
lista.append(70)
lista.append(80)

print(lista)

ultimo_valor = lista.pop()

print(lista)
print(lista, 'Removido ',ultimo_valor)