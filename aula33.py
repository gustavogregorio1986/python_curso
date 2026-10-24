"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutaveis que vimos: str, int, flat, bool
"""


string = 'Luiz Otavio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC'
print(string)
print(outra_variavel)
print(string.capitalize())
print(string.zfill(100))