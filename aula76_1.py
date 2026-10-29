pessoa = {}

pessoa['nome'] = 'Luiz Otavio'
lista = []

print(pessoa)
print(pessoa['nome'])

chave = 'nome_completo'

pessoa[chave] = 'Luiz Otavio'

print(pessoa[chave])

print(pessoa)


chave = 'nome_completo'

pessoa[chave] = 'Luiz Otavio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'maria'

print(pessoa)

del pessoa['sobrenome']
print(pessoa)