from vpython import *

# Configuração da cena
scene = canvas(width=800, height=600, background=color.black)  # Fundo preto
scene.camera.pos = vector(60, 60, 60)  # Posição da câmera para visão isométrica
scene.camera.axis = vector(-60, -60, -60)  # Direcionando a câmera para o centro da curva

# Definindo parâmetros do sistema
m = 1500  # Massa do carro (kg)
g = 9.8  # Aceleração gravitacional (m/s²)
atrito_pneu1 = 0.4  # Atrito do pneu 1
atrito_pneu2 = 0.2  # Atrito pneu 2
raio = 50  # Raio da curva em metros
velocidade_carro = 50  # Velocidade do carro (km/h)
velocidade_carro = velocidade_carro / 3.6  # Converte para m/s

# Criar o plano horizontal (verde)
plano = ring(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=raio, thickness=0.5, color=color.green)

# Criar o bloco representando o carro (branco)
block = box(pos=vector(raio, 0.5, 0), size=vector(3, 1, 2), color=color.white)

# Cálculo das velocidades máximas para os coeficientes de atrito
v1 = (atrito_pneu1 * g * raio) ** 0.5  # Velocidade máxima para μ = 0.4 (em m/s)
v2 = (atrito_pneu2 * g * raio) ** 0.5  # Velocidade máxima para μ = 0.2 (em m/s)

# Verificação do movimento
if velocidade_carro <= v1:
    # O carro consegue fazer a curva com segurança
    aceleracao = velocidade_carro
    omega = velocidade_carro / raio  # Velocidade angular
    movimento = True
    capotagem = False
else:
    # O carro derrapa e capota
    aceleracao = velocidade_carro
    movimento = False
    capotagem = True

# Exibir informações iniciais
print(f"Velocidade máxima para μ={atrito_pneu1:.2f} é {v1 * 3.6:.2f} km/h")
print(f"Velocidade máxima para μ={atrito_pneu2:.2f} é {v2 * 3.6:.2f} km/h")

if movimento:
    print("O carro faz a curva normalmente.")
    print(f"A velocidade do carro será de {aceleracao * 3.6:.2f} km/h")
else:
    if capotagem:
        print("O carro ultrapassou o limite de velocidade e capotou.")
        print(f"A velocidade do carro será de {aceleracao * 3.6:.2f} km/h")
    else:
        print("O carro derrapa.")

# Parâmetros de tempo
dt = 0.01  # Intervalo de tempo
angulo = 0  # Ângulo inicial para o movimento circular

# Função de animação do bloco (carro)
def mover_bloco():
    global angulo, omega, capotagem
    if movimento:
        while True:
            rate(100)  # Controlar a taxa de atualização
            # Atualizar a posição angular do carro
            angulo += omega * dt
            
            # Atualizar a posição do carro em coordenadas polares (transformada em cartesianas)
            block.pos.x = raio * cos(angulo)
            block.pos.z = raio * sin(angulo)
    elif capotagem:
        # Simulação de capotagem
        for i in range(200):  # Capotagem dura alguns quadros
            rate(50)  # Controla a taxa de atualização
            block.rotate(angle=radians(10), axis=vector(1, 0, 0))  # Faz o carro "girar" no ar
            block.pos.y += 0.1  # O carro sobe levemente ao capotar

# Iniciar a simulação
mover_bloco()
