from vpython import *

# Configuração da cena
scene = canvas(width=1200, height=1000, background=color.black)  # Fundo preto

# Definindo parâmetros do sistema
m = 5.0  # Massa do bloco (kg)
g = 9.8  # Aceleração gravitacional (m/s^2)
theta = radians(30)  # Ângulo do plano inclinado (convertido para radianos)
mu_s = 0.4  # Coeficiente de atrito estático
mu_k = 0.3  # Coeficiente de atrito cinético

# Criar o plano inclinado (verde e maior)
plano = box(pos=vector(0, 0, 0), size=vector(15, 0.2, 4), color=color.green, axis=vector(cos(theta), sin(theta), 0))

# Criar o bloco (branco)
block = box(pos=vector(6 * cos(theta), 6 * sin(theta) + 0.5, 0), size=vector(1, 1, 1), color=color.white)

# Cálculo das forças
N = m * g * cos(theta)  # Força normal
f_atrito_estatico_max = mu_s * N  # Força máxima de atrito estático
f_paralela = m * g * sin(theta)  # Força paralela ao plano inclinado

# Verificação do movimento
if f_paralela > f_atrito_estatico_max:
    # O bloco se move
    f_atrito_cinetico = mu_k * N  # Força de atrito cinético
    f_resultante = f_paralela - f_atrito_cinetico  # Força resultante
    aceleracao = f_resultante / m  # Aceleração do bloco
    movimento = True
else:
    # O bloco não se move
    aceleracao = 0
    movimento = False

# Exibir informações iniciais
print(f"Força máxima de atrito estático: {f_atrito_estatico_max:.2f} N")
print(f"Força paralela: {f_paralela:.2f} N")
if movimento:
    print("O bloco se moverá.")
    print(f"A aceleração do bloco será de {aceleracao:.2f} m/s²")
else:
    print("O bloco permanecerá em repouso.")

# Parâmetros de tempo
velocidade = vector(0, 0, 0)
dt = 0.01  # Intervalo de tempo

# Função de animação do bloco
def mover_bloco():
    global velocidade, aceleracao, dt
    if movimento:
        while block.pos.x > -7 * cos(theta):  # Limite do movimento
            rate(100)  # Controlar a taxa de atualização
            velocidade.x += -aceleracao * cos(theta) * dt
            velocidade.y += -aceleracao * sin(theta) * dt
            block.pos += velocidade * dt

# Iniciar a simulação
mover_bloco()
