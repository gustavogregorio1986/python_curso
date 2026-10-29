"""
Higher Order Functions
Funções de primeira classe
"""

def  saudacao(msg):
    return msg

saudacao_2 = saudacao

v = saudacao('Bom dia')
print(v)

def executa(funcao, msg):
    return funcao(msg)




v = executa(saudacao, 'Bom dia')