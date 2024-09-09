import math
r=0.02
ps=8000
pf=900
v=0.5
g=9.8
vt= (2*r**2*(ps-pf)*g) /(9*v)
print(f"velocidade terminal= {vt:.2f}m/s")
f_arrasto=6*math.pi*v*r*vt
print(f"força de arrasto= {f_arrasto:.2f} N")