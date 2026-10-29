# Métodos úteis dois dicionarios em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iteravel com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópua rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome':'Luiz Otavio',
    'sobrenome':'Miranda 1',
    'idade':900,
    # 'sobrenome':'Miranda 2',
    # 'sobrenome':'Miranda 3',
}

print(pessoa.__len__())
print(len(pessoa))
print(pessoa.keys())
print(tuple(pessoa.keys()))

for chave in pessoa.keys():
     print(chave)

print(list(pessoa.values()))
print(list(pessoa.items()))
for chave, valor in pessoa.items():
     print(chave, valor)