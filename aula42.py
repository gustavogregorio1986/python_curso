frase = 'O Python é uma linguagem de programação ' \
        'multiplataforma. ' \
        'Python foi criado por Guido van Rossum.'.lower()

print("Contagem de 'python':", frase.count("python"))
print("Contagem de 'a':", frase.count("a"))
print("Contagem de 'o':", frase.count("o"))
print("-" * 40)

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    # Ignora espaços em branco para focar nas letras
    if letra_atual.strip(): 
        quantidade_vezes_letra_apareceu = frase.count(letra_atual)

        if qtd_apareceu_mais_vezes < quantidade_vezes_letra_apareceu:
            qtd_apareceu_mais_vezes = quantidade_vezes_letra_apareceu
            letra_apareceu_mais_vezes = letra_atual

    i += 1

# O print final fica fora do while para mostrar apenas o vencedor
print('A letra que apareceu mais vezes foi:', f"'{letra_apareceu_mais_vezes}'", f"com {qtd_apareceu_mais_vezes} repetições.")