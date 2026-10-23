"""
Formatação básica de strings
s - sring
d - int
f - float
.<numero de digitos>
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - Centro
Sinal - + ou - 
Ex.: 0>-100,.1f
Conversion flags - !r !s  !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{10000.48736481237460:>+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')