# Exercicios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos 
# Retorno o total para uma variável e mostre o valor

def multiplicacao(a,b,c):
    print(a * b * c)

multiplicacao(1,2,3)

# Crie uma função fala se um numero é par ou impar.
# Retorne se o número é par ou impar.

def parOuImpar(x):
    if x % 2 == 0:
        print("Numero é par")
    print("Numero é impar")

parOuImpar(4)