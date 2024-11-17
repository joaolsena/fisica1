import math

#Uma criança desliza, para mergulhar dentro de uma piscina, do alto de uma
#escorregadeira de 3m de comprimento e 30° de inclinação com respeito à horizontal. A
#extremidade inferior da escorregadeira está 3m acima da água. A que distância horizontal dessa
#extremidade a criança mergulha na água?

c = 3
a = math.radians(30)
g = 9.8

# velocidade enquanto ela esta na escorregadeira 
v0 = math.sqrt(2*g*math.sin(a)*3)

#calcular o tempo de queda livre
t = ( math.sqrt(((v0*math.sin(a))**2)-4*(1/2*g)*(-3))-(v0*math.sin(a)))/(2*(1/2*g))

#calcular o deslocamento

x = v0*math.cos(a)*t 



print(f"Velocidade inicial do salto: {x:.2f} m")