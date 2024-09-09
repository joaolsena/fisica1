import math
r=0.001
pa=1000
par=1.225
c=0.5
g=9.8

m= (4/3) *math.pi* r**3 *pa

a=math.pi*r**2

vt=math.sqrt((2*m*g)/(par*a*c))
print(f"velocidade terminal= {vt:.2f} m/s")
b=0.5*c*par*a
t_95= -(m/b)*math.log(0.05)

a_95=0.5*vt*t_95
print(f"Altura mínima para atingir 95% da velocidade terminal: {a_95:.2f} m ")

