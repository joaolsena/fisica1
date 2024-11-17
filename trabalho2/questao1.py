import math
#Questão 1: Uma pulga de massa igual a 2 mg é capaz de saltar verticalmente a uma altura de 50
#cm. Durante o intervalo de tempo (muito curto) em que estica as patas para impulsionar o salto,
#ela se eleva de 1 mm antes que suas patas "decolem" do solo. Calcule a força média (em kgf)
#exercida pela pulga sobre o solo ao pular e compare-a com o peso da pulga.

#solucao
#1 dados
m = 2e-6 #massa em kg
h = 50e-2 #altura em m
eleva = 1e-3 #elevacao em m
g = 9.8 #gravidade

# 2. Definição das equações e funções usadas

#2.1 calculando a velocida inicial
v0 = math.sqrt(2*g*h)

#2.2 calculando a aceleraco no impulso
a = v0**2/(2*eleva)

#calculando a forca media 
fm = m*a

#calculando o peso da pulga
p = m*g

#coverter para kgf
fm = fm/g
p = p/g
 
#comparacao 
c = fm/p


print(f"Velocidade inicial do salto: {v0:.2f} m/s")
print(f"aceleracao no impulso: {a:.2f} m/s2")
print(f"forca media: {fm:.3f} kgf")
print(f"comparacao: {c:.2f} vezes")