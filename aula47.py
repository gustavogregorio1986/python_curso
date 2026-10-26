"""

Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta qualquer e 
vai dar possibvilidade para o usuário usuário digitar a letra, 
você
vai conferir se a letra digitada esta na palavra secreta.
   - Se a letra digitada estiver na palavra secreta; exiba a 
   letra;
    -Se a letra digitada não esitver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário
"""

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    palavra_formada = ''
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
           palavra_formada += '*'

    print('Palavra fo0rmada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!!! PARABENS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
