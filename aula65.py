"""

Introdução às dunções (def) em Python
Funções sõa trechos de codigos usados para
replicar determinada ação ao longo do seu codigo.
Elas podem receber valores para paramtros (argumentos)
e retornar um valor especifico
Por padrão, funções Python retornam None (nada)
"""

# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')


# Print()
# Print()
# Print()
# Print()
# Print()

# def imprimir(a, b, c):
#      print('Várias1')
#      print('Várias2')
#      print('Várias3')
#      print('Várias4')


# imprimir(1,2,3)

def imprimir(a, b, c):
     print(a, b, c)


imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome = "Sem nome"):
     print(f'Ola {nome}')

saudacao('Luiz Otavio')
saudacao('Maria')
saudacao('Helena')
saudacao()
