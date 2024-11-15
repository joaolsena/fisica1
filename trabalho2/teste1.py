# Solução:
# 1. Dados da questão
m = 20e-3 # massa em kg
v0 = 500 # velocidade em m/s
d = 10e-2 # profundidade em m
# 2. Definição das equações e funções usadas
# 2.1. aceleração: retirada da equação de Torricelli
def aceleracao(v0, d):
 a = -v0**2/(2*d)
 return a
# 2.2. força média
def forca_media(m, a):
 F = m*a
 return F
# 3. Cálculos
a = aceleracao(v0, d)
Forca = forca_media(m, a)
# 4. Resultados
print(f"A aceleração é de {a} m/s².")
print(f"A força média é de {Forca} N ou {Forca*0.102} kgf.")