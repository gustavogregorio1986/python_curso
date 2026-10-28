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

# --- 1. Cálculo do Primeiro Dígito Verificador ---
nove_digitos = cpf[:9]
contador_1 = 10
soma_1 = 0

for digito in nove_digitos:
    soma_1 += int(digito) * contador_1
    contador_1 -= 1

digito_1 = (soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


# --- 2. Cálculo do Segundo Dígito Verificador ---
# Pegamos os 9 dígitos + o primeiro dígito verificador recém-calculado (total de 10)
dez_digitos = nove_digitos + str(digito_1)
contador_2 = 11
soma_2 = 0

for digito in dez_digitos:
    soma_2 += int(digito) * contador_2
    contador_2 -= 1

digito_2 = (soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


print(f"Primeiro dígito: {digito_1}")
print(f"Segundo dígito: {digito_2}")
print(f"Dígitos verificadores calculados: {digito_1}{digito_2}")