import math

#Um garoto quer atirar um pedregulho de massa igual a 50 g num passarinho
#pousado num galho 5 m à sua frente e 2 m acima do seu braço. Para isso, utiliza um estilingue
#em que cada elástico se estica de 1 cm para uma força aplicada de 1 N. O garoto aponta numa
#direção a 30° da horizontal. De que distância deve puxar os elásticos para acertar no
#passarinho?

pedra = 50e-3 #em kg
posicaox = 5
posicaoy = 2
estica = 1e-2 #para m
f = 1*2 #pois sao dois elasticos
a = math.radians(30)
g = 9.8

#calcular a constante elastica 
k = f/estica

#calcular a velocidade atraves da equacao da trajetoria parabolica
v = math.sqrt((g*posicaox**2)/((2*(math.cos(a)**2))*(posicaox*math.tan(a)-posicaoy)))

#calcular a deformacao usando a coservacaio da energia mecanica: energia cinetica= energia potencial elastica
x = v*(math.sqrt((0.05/k)))

#converter para cm
x = x*1e+2



print(f"a distacia para puxar o elastico é:{x:.2f} cm")