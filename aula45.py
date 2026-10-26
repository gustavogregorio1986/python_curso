"""

Iteravel -> str, range, etc (__iter__)
Iterador -> quem sabe entrgar um valor pro vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# numeros = range(0,100, 8)
# #print(numeros)

# for numero in numeros:
#     print(numero)

texto = 'Luiz'.__iter__()

print(texto)

texto = iter('Luiz')

print(texto)

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())

texto = 'Luiz'
iteratador = iter(texto)

while True:
  try:
    letra = next(iteratador)
    print(letra)
  except StopIteration:
    break

for letra in texto:
  print(letra)