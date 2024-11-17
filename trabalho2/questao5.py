import math

#O coeficiente de atrito estático entre as roupas de uma pessoa e a parede cilíndrica
#de uma centrífuga de parque de diversões de 2 m de raio é 0,5. Qual é a velocidade angular
#mínima (em rotações por minuto) da centrífuga para que a pessoa permaneça colada à parede,
#suspensa acima do chão?

raio = 2
a = 0.5
g = 9.8
 
#velocidade angular

w = math.sqrt((g/(a*raio)))

#converter para rmp

c = (w/(2*3.14))*60

print(f"a velocidade angular mínima é: {c:.2f} rpm")