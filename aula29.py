"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idaxde
se o nome  eidade forem digitados:
    exiba
       seu nome {nome}
       se nome invertido
       seu nome contem (ou não) espaços
       Seu nome tem {n} letras
       A primeira letra ao seu nome é {letra}
       A ultima letra letra do sue nome é {letra}
se nada for digiatdo em nome ou idade:
exiba "Desculpe, voce tem campos vazios."
"""

nome = input('Digite o nome: ')
idade = input('Digite a idade: ')

# Verifica se o nome ou a idade estão vazios
if nome == '' or idade == '':
    print("Desculpe, você tem campos vazios.")
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    
    # Verifica se contém espaços
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome NÃO contém espaços.')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')