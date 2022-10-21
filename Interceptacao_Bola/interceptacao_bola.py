import time
from Dados_Grafico.gerar_dados import gerarDados
from math import *

#Função que recebe os dados da trajetoria da bola e exibe na tela
def interceptacao_bola(t,x_bola,y_bola, x_robo, y_robo, velocidade, aceleracao,vmax,raio_interceptacao):

    # Para caso o y_bola seja igual y_robo não dar erro de divisão!
    if (y_bola == y_robo):
        tendencia_0 = 0.0000000000000000000000000000000000000000000000000000001
        modulo_tangente = sqrt(((x_bola - x_robo) ** 2) / ((tendencia_0) ** 2))
    else:
        modulo_tangente =sqrt(((x_bola-x_robo)**2)/((y_bola-y_robo)**2))


    #Pegar o angulo da tangente
    angulo = atan(modulo_tangente)

    distancia = sqrt(((x_robo - x_bola) ** 2) + ((y_robo - y_bola) ** 2))

    print("Tempo: ", t)
    print("X_robo: %.3f" % x_robo)
    print("Y_robo: %.3f" % y_robo)
    print("X_BOLA: %.3f" % x_bola)
    print("Y_BOLA: %.3f" % y_bola)
    print("Dist_x: %.3f" % (x_bola - x_robo))
    print("Dist_y: %.3f" % (y_bola - y_robo))
    print("Distancia: %.3f" % distancia)

    if distancia>=2.8:
        vmax = 2.8
        aceleracao = 2.8
    elif 2.8 > distancia>=1.4:
        vmax=1.4
        aceleracao = 0.7
    elif 1.4 > distancia >= 1:
        vmax = 1
        aceleracao = 0.5
    elif 1 > distancia >= 0.5:
        vmax = 0.5
        aceleracao = 0.25
    elif 0.5 > distancia >= 0.25:
        vmax = 0.25
        aceleracao = 0.25
    elif 0.25 > distancia >= 0.1:
        vmax = 0.1
        aceleracao = 0.05

    if velocidade < vmax:
        velocidade = velocidade + aceleracao*0.2
    elif velocidade > vmax:
        velocidade = velocidade - aceleracao*0.2
    else:
        velocidade = velocidade

    #Velocidade em cada eixo com base no vetor velocidade e seu ângulo direção
    angulo = (angulo*180)/pi

    velocidade_x = velocidade * sin(angulo)
    velocidade_y = velocidade * cos(angulo)

    #Calculo da aceleração no eixo x e y
    aceleracao_x = aceleracao * sin(angulo)
    aceleracao_y = aceleracao * cos(angulo)

    #Analise das coordenadas dos robôs e da bola para determinar o sentido da velocidade
    if (x_robo < x_bola):
        velocidade_x = sqrt(velocidade_x**2)
    else:
        velocidade_x = sqrt(velocidade_x**2) * (-1)

    if (y_robo < y_bola):
        velocidade_y = sqrt(velocidade_y**2)
    else:
        velocidade_y = sqrt(velocidade_y**2) * (-1)

    #Aplicar a velocidade no robô
    x_robo += velocidade_x
    y_robo += velocidade_y

    #Calculo da distancia entre o robô e a bola
    print("Angulo %.3f" %angulo)
    print("Vx: %.3f" % velocidade_x)
    print("Vy: %.3f" % velocidade_y)
    print()

    #Função responsável por criar arquivos que contém  os dados necessários para a futura criação dos gráfico
    gerarDados(t,x_robo, y_robo,velocidade_x,velocidade_y,distancia,x_bola,y_bola,aceleracao_x, aceleracao_y)

    #Coloquei uma condição para que ao entrar no R de interceptação, o robô pare!
    if (distancia <= raio_interceptacao):
        #Se a distância estiver dentro do intervalo, o robô para e retorna "TRUE" para parar o for
        print("\nBola interceptada!")
        print("Tempo = %.2f \n" %t)
        interceptacao = True
        return x_robo, y_robo, velocidade, aceleracao, vmax, interceptacao
    else:
        #Se a distância não estiver dentro do intervalo, o robô continua e retorna "FALSE" para continuar o for
        interceptacao = False
        return x_robo, y_robo, velocidade, aceleracao, vmax, interceptacao



