from Interceptacao_Bola.interceptacao_bola import interceptacao_bola
from Dados_Grafico.dadosMovimentacaoBola import dadosVelBola,dadosAcelBola
from Dados_Grafico.criar_graficos import criar_graficos
from Dados_Grafico.velocidadeRelativa import pegarVelRelativa
from math import sqrt,atan,pi

def mostrarDadosIniciais(matriz_trajetoria,robo,bola):

    print("Dados Iniciais: \n")

    tempo = float(matriz_trajetoria[0][0])
    bola['x'] = float((matriz_trajetoria[0][1]))
    bola['y'] = float(matriz_trajetoria[0][2])

    # Para caso o y_bola seja igual y_robo não dar erro de divisão!
    if (bola['y'] == robo['y']):
        tendencia_0 = 0.00000000000000001
        modulo_tangente = sqrt(((bola['x'] - robo['x']) ** 2) / ((tendencia_0) ** 2))
    else:
        modulo_tangente =sqrt(((bola['x']-robo['x'])**2)/((bola['y']-robo['y'])**2))
    #Pegar o angulo da tangente
    angulo = atan(modulo_tangente)

    bola['distancia_robo'] = sqrt(((bola['x'] - robo['x']) ** 2) + ((bola['y'] - robo['y']) ** 2))
    print("\n########################")
    print("Tempo: ", tempo)
    print("X_robo: %.3f" % robo['x'])
    print("Y_robo: %.3f" % robo['y'])
    print("X_BOLA: %.3f" % bola['x'])
    print("Y_BOLA: %.3f" % bola['y'])
    print("Dist_x: %.3f" % (bola['x'] - robo['x']))
    print("Dist_y: %.3f" % (bola['y'] - robo['y']))
    print("Distancia: %.3f" % (sqrt(((bola['x'] - robo['x']) ** 2) + ((bola['y'] - robo['y']) ** 2))))
    print("Angulo %.3f" %((angulo*180)/pi))
    print("########################\n")

def movimentarRoboRaioPadrao(matriz_trajetoria,robo,bola):

    print("Rodando código com raio PADRÃO: 10.54 cm");

    for linha in range(len(matriz_trajetoria)):
        
        tempo = float(matriz_trajetoria[linha][0])
        bola['x'] = float((matriz_trajetoria[linha][1]))
        bola['y'] = float(matriz_trajetoria[linha][2])

        robo = interceptacao_bola(tempo,robo,bola)

        if (robo['interceptou_bola'] == True):
            break
        else:
            pass

    #Pegar valores da velocidade e aceleracao da bola:
    dadosVelBola(tempo,robo)
    dadosAcelBola(robo)
    pegarVelRelativa(robo)
    criar_graficos(robo)

def movimentarRoboRaioAlterado(matriz_trajetoria,robo,bola):

    robo_x_inicial = robo['x']
    robo_y_inicial = robo['y']

    print("Rodando código com raio ALTERADO: %.2f cm" % (robo['raio_interceptacao']*100));

    for vezes in range(2):

        for linha in range(len(matriz_trajetoria)):
            
            tempo = float(matriz_trajetoria[linha][0])
            bola['x'] = float((matriz_trajetoria[linha][1]))
            bola['y'] = float(matriz_trajetoria[linha][2])
            robo = interceptacao_bola(tempo,robo,bola)

            if (robo['interceptou_bola'] == True):
                break
            else:
                pass


        #Pegar valores da velocidade e aceleracao da bola:
        dadosVelBola(tempo,robo)
        dadosAcelBola(robo)
        pegarVelRelativa(robo)
        criar_graficos(robo)

        if vezes == 0:
            #Voltar o robo e a bola para posicoes e dados iniciais
            robo = {
            'querAlterarRaio': 0, #int (bool - 0 or 1)
            'raio_interceptacao': 0.1054, #float
            'x': robo_x_inicial, #float
            'y': robo_y_inicial, #float
            'vmax': 0, #float
            'vel': 0, #float
            'vel_x': 0, #float
            'vel_y': 0, #float
            'acel': 0, #float
            'acel_x': 0, #float
            'acel_y': 0, #float
            'interceptou_bola': False #bool
            }

            bola = {
                'x': 0, #float
                'y': 0, #float
                'distancia_robo': 0 #float
            }

            tempo=0
        

            print("Rodando código com raio PADRÃO: 10.54 cm");


