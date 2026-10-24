"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio' # Iteraveis

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

print(nome[3])

nome = 'Maria Helena'
tamanho_nome = len(nome)  # Retorna a quantidade total de letras/espaços
indice = 0
nova_string = ''

while indice < tamanho_nome:
    letra = nome[indice]
    nova_string += f'*{letra}'  
    indice += 1                 

nova_string += '*'
print(nova_string)