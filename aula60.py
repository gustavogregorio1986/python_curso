"""

Operação ternária (condicional de unma linha)
<valor> if <codicao> else <outro valor>
"""

print('Valor' if True else 'Outro valor')
codicao = 10 == 11

variavel = 'Valor' if codicao else 'Outro Valor'
print(variavel)

digito = 1
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)