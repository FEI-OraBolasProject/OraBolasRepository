import time
from math import *

#Função que recebe os dados da trajetoria da bola e exibe na tela
def interceptacao_bola(t,x_bola,y_bola):
    global x_robo, y_robo, velocidade, desacelerar

    # Para caso o y_bola seja igual y_robo não dar erro de divisão!
    if (y_bola == y_robo):
        tendencia_0 = 0.0000000000000000000000000000000000000000000000000000001
        modulo_tangente = sqrt(((x_bola - x_robo) ** 2) / ((tendencia_0) ** 2))
    else:
        modulo_tangente =sqrt(((x_bola-x_robo)**2)/((y_bola-y_robo)**2))

    #Pegar o angulo da tangente
    angulo = atan(modulo_tangente)

    #Velocidade em cada eixo com base no vetor velocidade e seu ângulo direção
    velocidade_x = velocidade * sin(radians(angulo))
    velocidade_y = velocidade * cos(radians(angulo))

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
    distancia = sqrt(((x_robo - x_bola) ** 2) + ((y_robo - y_bola) ** 2))

    if velocidade >= 2.8 and distancia <= 2.8:
        print("velocidade x: ", velocidade_x)
        print("velocidade y: ", velocidade_y)
        print("distancia: ", distancia)
        print()
        desacelerar = True

    #Coloquei uma condição para que ao entrar no R de interceptação, o robô pare!
    #Tem esse intervalo por causa da incerteza de 0.5 - R = 10.29 +- 0.25 -> 0.1054 metros
    if (distancia <= 0.1054):
        #Se a distância estiver dentro do intervalo, o robô para e retorna "TRUE" para parar o for
        print("\nBola interceptada!")
        print("Tempo = %.2f \n" %t)
        interceptacao = True
        return interceptacao
    else:
        #Se a distância não estiver dentro do intervalo, o robô continua e retorna "FALSE" para continuar o for
        interceptacao = False
        return interceptacao


#Leitura de dados do arquivo trajetoria_bola.txt
traj_bola = open("trajetoria_formatada.txt", "r")#
dados = traj_bola.readlines()#faz a leitura das linhas presentes no arquivo

matriz_traj = [] #matriz_pedidos (os dados seram organizados dentro dela )

for i in range(len(dados)):
        palavra = dados[i].strip('\n')#remove a quebra de linha presentes na linha do arquivo
        palavra = palavra.replace(",",".")#substitui a virgula por ponto
        palavra = palavra.split("\t")#seleciona os dados separados por "\t"

        matriz_traj.append(palavra)#insere os dados separados dentro da "matriz_traj"

#Criei as posições iniciais do robo e a velocidade como essas só para teste
x_robo = 0.0
y_robo = 0.5
aceleracao = 2.8 #metros por segundo ao quadrado (m/s²)
desaceleracao = 0.01 #metros por segundo ao quadrado (m/s²)
desacelerar = False #Variável para saber se o robô deverá começar a desacelerar (booleano)
velocidade = 0 #Velocidade inicial do robô em metros por segundo (m/s)


# Indice por lista : [0][0] = t/s, [0][1] = x/m, [0][2] = y/m 
#Exibe os dados presentes na "matriz_traj" :" : 
for linha in range(len(matriz_traj)):
        
    tempo = float(matriz_traj[linha][0])
    x = float((matriz_traj[linha][1]))
    y = float(matriz_traj[linha][2])

    #Calculo da velocidade do robo em funcao do tempo
    if velocidade <= 2.8 and desacelerar == False:
        velocidade = aceleracao * tempo
    elif desacelerar == True:
        if velocidade >= 0.10:
            velocidade = velocidade - desaceleracao * tempo

    interceptacao = interceptacao_bola(tempo,x,y)

    if (interceptacao == True):
        break
    else:
        pass

    #Para testarmos é melhor tirar o tempo, depois a gente coloca!!!
    #time.sleep(0.2)# leitura dos dados a cada 2 segundos

print("Fim do programa")

traj_bola.close()#fecha o arquivo