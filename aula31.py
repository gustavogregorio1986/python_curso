"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 65 # Acima da velocidade do radar (61)
local_carro = 100 # Bem em cima do local do radar 1

RADAR_1 = 61 
LOCAL_1 = 100 
RADAR_RANGE = 1 

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_multado_radar_1 and vel_carro_pass_radar_1:
    print('carro multado em radar 1')