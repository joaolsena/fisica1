import math
m=75 #massa em kg
g=9.8
queda_livre=10 
c_humano= 1
a_sem_paraquedas=0.7
a_paraquedas=20
c_paraquedas=1.5
p=1.225

velocidade_terminal_inicial=((2 * m * g) / (p * c_humano * a_sem_paraquedas)) ** 0.5
print(f"a velocidade terminal antes da da abertutura do paraquedas = {velocidade_terminal_inicial:.2f}m/s")
velocidade_terminal_final=((2 * m * g) / (p * c_paraquedas * a_paraquedas) )** (1/2)
print(f"a velocidade terminal depois da abertura do paraquedas = {velocidade_terminal_final:.2f}m/s")
b=0.5 * p * c_paraquedas * a_paraquedas
tempo_99= -(m/b)* math.log(0.01)
print(f"Tempo para atingir 99% da nova velocidade terminal: {tempo_99:.2f} s")