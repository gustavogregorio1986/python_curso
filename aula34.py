"""
Repetições 
while (enquanto)
Executa a ação enqaunto uma condição for verdadeira
Loop infinito -> quando o codigo não tem fim
"""

condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    if nome == 'sair':
      break

print('Acabou')