import math

#Um automóvel estacionado no alto de uma ladeira molhada pela chuva, de 100 m de
#comprimento e 25 m de altura, perde os freios e desliza pela ladeira (despreze o atrito). Com
#que velocidade, em km/h, ele atinge o pé da ladeira?


#solucao
#1 dados
c = 100
h = 25
g = 9.8

# Cálculo da velocidade
vf = math.sqrt(2*g*h)

#coversao para km
vf = vf*3.6

print (f"velocidade final: {vf:.2f} km/h")
