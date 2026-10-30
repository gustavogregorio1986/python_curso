# Dictonary Comprehension re Set Comprehension
produto = {
    'nome':'caneta Azul',
    'preco': 2.5,
    'categoria':'Escritorio',
}

print(produto.items())

for chave, valor in produto.items():
    print(chave, valor)

dc = {
    chave: valor.upper()
    if isinstance(valor, (int, float)) else valor
    for chave, valor
    in produto.items()
    if chave == 'categoria'
}

lista = [
    {'a','valor a'},
    {'b','valor a'},
    {'b','valor a'},
]

dc = {
     chave: valor
     for chave, valor in lista
}


s1 = {i ** 2 for i in range(10)}

print(s1)