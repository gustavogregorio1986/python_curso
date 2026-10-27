"""
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos utéis: apedn, insert, pop del, clear, extend, + 
"""
#      01234
#     -54321
string = 'ABCDE'
lista = [123, True,'Luiz Otavio', 1.2, []]
print(bool(lista))
print(lista, type(lista))
print(lista[2], type(lista[2]))
print(lista[2].upper(), type(lista[2]))
lista[-3] = 'Maria'
print(lista)