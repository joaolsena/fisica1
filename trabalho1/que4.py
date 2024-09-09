from vpython import sphere, vector, rate, scene, color, box

# Configuração da cena
scene.background = color.white
scene.width = 800
scene.height = 600
scene.camera.pos = vector(0, 1, 5)
scene.camera.axis = vector(0, -1, -5)

# Parâmetros do sistema
m = 0.05
g = 9.8
b = 0.47
raio = 1
area = 3.14 * raio**2
p = 1.225

v_com_arrasto = vector(0, 0, 0)
v_sem_arrasto = vector(0, 0, 0)
dt = 0.01

# Calculando a velocidade terminal
v_terminal = ((2 * m * g) / (p * b * area)) ** 0.5
print(f"Velocidade terminal = {v_terminal:.2f} m/s")

d = 0.5 * b * area * p
log_0_1 = -2.3026  # valor de log(0.1)
tempo_90_vt = -(m / d) * log_0_1
print(f"Tempo para atingir 90% da velocidade terminal: {tempo_90_vt:.2f} s")

# Criando a esfera com arrasto (cor azul)
bola_com_arrasto = sphere(pos=vector(-1, 5, 0), radius=raio, color=color.blue)

# Criando a esfera sem arrasto (cor vermelha)
bola_sem_arrasto = sphere(pos=vector(1, 5, 0), radius=raio, color=color.red)

# Criando um plano de fundo para representar o chão
chao = box(pos=vector(0, 0, 0), size=vector(5, 0.1, 1), color=color.gray(0.5))

# Gravidade
f_gravidade = vector(0, -m * g, 0)

# Simulação
while bola_com_arrasto.pos.y > bola_com_arrasto.radius or bola_sem_arrasto.pos.y > bola_sem_arrasto.radius:
    rate(100)
    
    # Para a bolinha com arrasto
    if bola_com_arrasto.pos.y > bola_com_arrasto.radius:
        v_com_arrasto_mag = mag(v_com_arrasto)
        f_arrasto_valor = 0.5 * p * b * area * v_com_arrasto_mag**2
        f_arrasto = -f_arrasto_valor * norm(v_com_arrasto)
        f_total_com_arrasto = f_gravidade + f_arrasto
        
        aceleracao_com_arrasto = f_total_com_arrasto / m
        v_com_arrasto += aceleracao_com_arrasto * dt
        bola_com_arrasto.pos += v_com_arrasto * dt

    # Para a bolinha sem arrasto
    if bola_sem_arrasto.pos.y > bola_sem_arrasto.radius:
        aceleracao_sem_arrasto = f_gravidade / m
        v_sem_arrasto += aceleracao_sem_arrasto * dt
        bola_sem_arrasto.pos += v_sem_arrasto * dt
    
    # Parar a bolinha vermelha quando atingir o chão
    if bola_sem_arrasto.pos.y <= bola_sem_arrasto.radius:
        v_sem_arrasto = vector(0, 0, 0)
        bola_sem_arrasto.pos.y = bola_sem_arrasto.radius

    # Parar a bolinha azul quando atingir o chão
    if bola_com_arrasto.pos.y <= bola_com_arrasto.radius:
        v_com_arrasto = vector(0, 0, 0)
        bola_com_arrasto.pos.y = bola_com_arrasto.radius
