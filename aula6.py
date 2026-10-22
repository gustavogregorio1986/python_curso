# conversão tipos, coerção
# type convertion, typecasting, coercion
# é o ato que converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + 1)
# print('1' + 1) # TypeError: can only concatenate str (not "int") to str
print('a' + 'b')
print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1') + 1)
print(float('1.2') + 1)
print(bool(' '))
print(str(11) + 'b')