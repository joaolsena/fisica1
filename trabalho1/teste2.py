from vpython import box, cylinder, vector, color, canvas, rate, cos, sin

# Configuração da cena
scene = canvas(width=1200, height=1000, background=color.white)  # Fundo preto

# Definindo parâmetros do sistema
m = 1500  # Massa do carro (kg)
g = 9.8  # Aceleração gravitacional (m/s²)
atrito_pneu1 = 0.4  # Coeficiente de atrito dos pneus (cenário 1)
atrito_pneu2 = 0.2  # Coeficiente de atrito dos pneus (cenário 2)
raio_curva = 50  # Raio da curva em metros
velocidade_carro = 30  # Velocidade inicial do carro em m/s

# Cálculo das velocidades máximas para diferentes coeficientes de atrito
v1 = (atrito_pneu1 * g * raio_curva) ** 0.5  # Velocidade máxima para μ = 0.4
v2 = (atrito_pneu2 * g * raio_curva) ** 0.5  # Velocidade máxima para μ = 0.2

plano = box(pos=vector(-raio_curva, 3, 0), size=vector(50, 1, 5), color=color.green)

# Criando a carroceria do carro (um box)
carroceria = box(pos=vector(-raio_curva, 1, 0), size=vector(4, 1, 2), color=color.red)

# Criando a parte superior do carro (um box menor)
teto = box(pos=vector(-raio_curva, 1.75, 0), size=vector(2.5, 0.5, 1.5), color=color.blue)

# Função para criar uma roda do carro
def criar_roda(posicao):
    return cylinder(pos=posicao, axis=vector(0, 0, 0.5), radius=0.5, color=color.black)

# Criando as rodas do carro
roda1 = criar_roda(vector(-raio_curva - 1.5, 0.5, 1))  # Roda traseira direita
roda2 = criar_roda(vector(-raio_curva + 1.5, 0.5, 1))  # Roda dianteira direita
roda3 = criar_roda(vector(-raio_curva - 1.5, 0.5, -1)) # Roda traseira esquerda
roda4 = criar_roda(vector(-raio_curva + 1.5, 0.5, -1)) # Roda dianteira esquerda

# Verificação do movimento
if velocidade_carro < v1:
    # O carro não ultrapassa o limite de velocidade (seguro)
    movimento = True
else:
    # O carro ultrapassa o limite e pode capotar
    movimento = False

# Exibir informações iniciais
print(f"Velocidade máxima para μ = 0.4: {v1 * 3.6:.2f} km/h")
print(f"Velocidade máxima para μ = 0.2: {v2 * 3.6:.2f} km/h")

if movimento:
    print("O carro faz a curva normalmente.")
else:
    print("O carro capota! Cuidado com a velocidade.")

# Parâmetros de tempo
velocidade = vector(velocidade_carro, 0, 0)
dt = 0.01  # Intervalo de tempo
angulo = 0  # Ângulo inicial para o movimento circular

# Função de animação do movimento do carro na curva
def mover_carro():
    global angulo
    while angulo < 2 * 3.1415:  # Uma volta completa
        rate(100)  # Controla a taxa de atualização
        angulo += velocidade_carro * dt / raio_curva  # Atualiza o ângulo
        # Atualiza a posição do carro para um movimento circular
        carroceria.pos = vector(raio_curva * cos(angulo), carroceria.pos.y, raio_curva * sin(angulo))
        teto.pos = vector(raio_curva * cos(angulo), teto.pos.y, raio_curva * sin(angulo))
        roda1.pos = vector(raio_curva * cos(angulo) - 1.5, roda1.pos.y, raio_curva * sin(angulo) + 1)
        roda2.pos = vector(raio_curva * cos(angulo) + 1.5, roda2.pos.y, raio_curva * sin(angulo) + 1)
        roda3.pos = vector(raio_curva * cos(angulo) - 1.5, roda3.pos.y, raio_curva * sin(angulo) - 1)
        roda4.pos = vector(raio_curva * cos(angulo) + 1.5, roda4.pos.y, raio_curva * sin(angulo) - 1)

# Função para simular o capotamento
def capotamento():
    global angulo
    while carroceria.pos.y < 5:  # O carro "capota" até alcançar uma altura
        rate(50)
        carroceria.pos.y += 0.1  # Aumenta a altura para simular o capotamento
        teto.pos.y += 0.1
        roda1.pos.y += 0.1
        roda2.pos.y += 0.1
        roda3.pos.y += 0.1
        roda4.pos.y += 0.1

# Iniciar a simulação de acordo com o movimento
if movimento:
    mover_carro()
else:
    capotamento()
