
from vpython import box, vector, rate, scene

# Configuração da cena
scene.background = vector(1, 1, 1)
scene.width = 1000
scene.height = 1000

# Criando a superfície e o bloco
floor = box(pos=vector(0, 0, 0), size=vector(10, 0.2, 4), color=vector(0.5, 0.5, 0.5))
block = box(pos=vector(-4, 0.6, 2), size=vector(1, 1, 1), color=vector(0, 0, 1))

# Parâmetros do sistema
mu_s = 0.4  # Coeficiente de atrito estático
mu_k = 0.3  # Coeficiente de atrito cinético
g = 9.8     # Aceleração gravitacional (m/s^2)
m = 5.0     # Massa do bloco (kg)
N = m * g   # Força normal (N)

# Força de atrito máximo estático e força de atrito cinético
f_atrito_estatico = mu_s * N
f_atrito_cinetico = mu_k * N

# Exibir resultados
print(f"Força de atrito estático máxima: {f_atrito_estatico:.2f} N")
print(f"Força de atrito cinético: {f_atrito_cinetico:.2f} N")

# Simulação do movimento do bloco com atrito cinético
velocidade = vector(0, 0, 0)  # Velocidade inicial (m/s)
dt = 0.01                     # Intervalo de tempo (s)

while block.pos.x < 4:
    rate(100)
    f_atrito = -f_atrito_cinetico * velocidade.norm()  # Força de atrito atuando contra o movimento
    aceleracao = f_atrito / m                          # Segunda Lei de Newton
    velocidade += aceleracao * dt
    block.pos += velocidade * dt
