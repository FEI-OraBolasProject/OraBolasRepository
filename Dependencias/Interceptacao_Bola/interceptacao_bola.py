#mport time
from Dependencias.Dados_Grafico.gerar_dados import gerarDados
from math import *

#Função que recebe os dados da trajetoria da bola e exibe na tela
def interceptacao_bola(tempo,robo, bola):

    # Para caso o y_bola seja igual y_robo não dar erro de divisão!
    if (bola['y'] == robo['y']):
        tendencia_0 = 0.00000000000000001
        modulo_tangente = sqrt(((bola['x'] - robo['x'])/(tendencia_0))**2)
    else:
        modulo_tangente =sqrt(((bola['x']-robo['x'])/(bola['y']-robo['y']))**2)

    #Pegar o angulo da tangente
    angulo = atan(modulo_tangente)

    bola['distancia_robo'] = sqrt(((bola['x'] - robo['x']) ** 2) + ((bola['y'] - robo['y']) ** 2))

    if bola['distancia_robo']>=2.8:
        robo['vmax'] = 2.8
        robo['acel'] = 2.8
    elif 2.8 > bola['distancia_robo']>=1.4:
        robo['vmax']=1.4
        robo['acel'] = 0.7
    elif 1.4 > bola['distancia_robo'] >= 1:
        robo['vmax'] = 1
        robo['acel'] = 0.5
    elif 1 > bola['distancia_robo'] >= 0.5:
        robo['vmax'] = 0.5
        robo['acel'] = 0.25
    elif 0.5 > bola['distancia_robo'] >= 0.25:
        robo['vmax'] = 0.25
        robo['acel'] = 0.125
    elif 0.25 > bola['distancia_robo'] >= 0.1:
        robo['vmax'] = 0.1
        robo['acel'] = 0.05
    if robo['vel'] < robo['vmax']:
        robo['vel'] = robo['vel'] + robo['acel']*0.2
    elif robo['vel'] > robo['vmax']:
        robo['vel'] = robo['vel'] - robo['acel']*0.2
    else:
        robo['vel'] = robo['vel']

    robo['vel_x'] = robo['vel'] * sin(angulo)
    robo['vel_y'] = robo['vel'] * cos(angulo)

    #Calculo da aceleração no eixo x e y
    robo['acel_x'] = robo['acel'] * sin(angulo)
    robo['acel_y'] = robo['acel'] * cos(angulo)

    #Analise das coordenadas dos robôs e da bola para determinar o sentido da vel
    if (robo['x'] < bola['x']):
        robo['vel_x'] = sqrt(robo['vel_x']**2)
    else:
        robo['vel_x'] = sqrt(robo['vel_x']**2) * (-1)

    if (robo['y'] < bola['y']):
        robo['vel_y'] = sqrt(robo['vel_y']**2)
    else:
        robo['vel_y'] = sqrt(robo['vel_y']**2) * (-1)

    #Aplicar a vel no robô
    robo['x'] += robo['vel_x']
    robo['y'] += robo['vel_y']
    
    #Função responsável por criar arquivos que contém  os dados necessários para a futura criação dos gráfico
    gerarDados(tempo,robo,bola)


    #Coloquei uma condição para que ao entrar no R de interceptação, o robô pare!
    if (bola['distancia_robo'] <= robo['raio_interceptacao']):
        print("\n########################")
        #Se a distância estiver dentro do intervalo, o robô para e retorna "TRUE" para parar o for
        print("-> Bola interceptada! <-\n")
        print("Tempo = %.2f" %tempo)
        print("Raio de interceptação: %.2f cm" %(robo['raio_interceptacao']*100))
        print("Distância Final entre o robo e a bola: %.2f cm" %(bola['distancia_robo']*100))
        print("########################\n")

        robo['interceptou_bola'] = True
        
        return robo
    else:
        #Se a distância não estiver dentro do intervalo, o robô continua e retorna "FALSE" para continuar o for
        robo['interceptou_bola'] = False
        return robo



