"""
Ciuidados com dados mutáveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'Luiz'
noutra_variavel = nome
nome = 'João'

print(nome)
print(noutra_variavel)

lista_a = ['Luiz','Maria']
lista_b = lista_a

lista_a[0] = "Qualquer coisa"
print(lista_a)
print(lista_b)