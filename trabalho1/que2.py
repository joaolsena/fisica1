from vpython import *

# Configuração da cena
scene = canvas(width=1200, height=1000, background=color.black)  # Fundo preto

# Definindo parâmetros do sistema
m = 2  # Massa do bloco (kg)
g = 9.8  # Aceleração gravitacional (m/s²)
mu_s = 0.5  # Coeficiente de atrito estático
mu_k = 0.3  # Coeficiente de atrito cinético
f_aplicada = 15  # Força aplicada (N)

# Criar o plano horizontal (verde)
plano = box(pos=vector(0, 0, 0), size=vector(20, 0.2, 5), color=color.yellow)

# Criar o bloco (branco)
block = box(pos=vector(-11, 0.5, 0), size=vector(1, 1, 1), color=color.red)

# Cálculo das forças
N = m * g  # Força normal (N)
f_atrito_estatico_max = mu_s * N  # Força máxima de atrito estático
f_atrito_cinetico = mu_k * N  # Força de atrito cinético

# Verificação do movimento
if f_aplicada > f_atrito_estatico_max:
    # O bloco se move
    f_resultante = f_aplicada - f_atrito_cinetico  # Força resultante
    aceleracao = f_resultante / m  # Aceleração do bloco
    movimento = True
else:
    # O bloco não se move
    aceleracao = 0
    movimento = False

# Exibir informações iniciais
print(f"Força aplicada: {f_aplicada:.2f} N")
print(f"Força mínima para iniciar o movimento: {f_atrito_estatico_max:.2f} N")
print(f"Força de atrito cinético: {f_atrito_cinetico:.2f} N")

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
        while block.pos.x < 10.5:  # Limitar o movimento ao plano
            rate(100)  # Controlar a taxa de atualização
            velocidade.x += aceleracao * dt
            block.pos += velocidade * dt

# Iniciar a simulação
mover_bloco()
