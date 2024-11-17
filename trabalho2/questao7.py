import math

#Uma balança de mola é calibrada de tal forma que o prato desce de 1 cm quando
#uma massa de 0,5 kg está em equilíbrio sobre ele. Uma bola de 0,5 kg de massa fresca de pão,
#guardada numa prateleira 1m acima do prato da balança, escorrega da prateleira e cai sobre ele.
#Não levando em conta as massas do prato e da mola, de quanto desce o prato da balança?

d = 1e-2 #para m
m = 0.5
c = 1
g = 9.8

#calcular a cosntante elastica
k = (m*g)/d

#calcular a velocidade da bola
v = math.sqrt(2*g*c)

#calcular a energia cinetica
ec = (m*v**2)/2

#calcular a compressao
x = (math.sqrt((2*ec)/k))+d

#converter para cm
x = x*1e+2

print(f"o prato da balnca desceu: {x:.2f} cm")