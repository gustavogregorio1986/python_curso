"""

args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-se de desampacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
   total = 0
   for numero in args:
     total = total + numero
   print(total)

soma(1,2,3,4,5,6)

def soma(*arga):
   total = 0
   for numero in arga:
      total += numero
   return total

soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

numeros = soma(1,2,3,4,5,6,7,8,9,10)
outra_soma = 1,2,3,4,5,6,7,8,9,10

print(outra_soma)

print(numeros)