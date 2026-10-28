"""

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores poor uma
contagem regressiva começando de 10

Ex.: 746.824.890-70 (74682489070)

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se resultado anterior for mai8or que 9:
   resultado = 0
contrario disso:
   resultado é o valor da conta

o primeiro digito do CPF é 7
"""

cpf = '74682489070'
nove_digitos = cpf[:9]


contador_regressivo_1 = 10

resultado = 0
for digito_1 in nove_digitos:
   resultado += int(digito_1) * contador_regressivo_1
   contador_regressivo_1 -= 1
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
