from Interceptacao_Bola.posicao_inicial_robo import gerar_posicao_inicial
from Interceptacao_Bola.movimentarRobo import *
from Dados_Grafico.apagarArquivosAnteriores import *

def main():

    apagarArquivosAnteriores()

    #Leitura de dados do arquivo trajetoria_bola.txt
    arquivoTrajetoriaBolaTXT = open("trajetoria_formatada.txt", "r")#
    listaLinhasTrajBola = arquivoTrajetoriaBolaTXT.readlines()#faz a leitura das linhas presentes no arquivo
    arquivoTrajetoriaBolaTXT.close()#fecha o arquivo

    matriz_trajetoria = [] #matriz_pedidos (os dados seram organizados dentro dela )

    for linha in range(len(listaLinhasTrajBola)):
        dadosLinha = listaLinhasTrajBola[linha].strip('\n')#remove a quebra de linha presentes na linha do arquivo
        dadosLinha = dadosLinha.replace(",",".")#substitui a virgula por ponto
        dadosLinha = dadosLinha.split("\t")#seleciona os dados separados por "\t"

        matriz_trajetoria.append(dadosLinha)#insere os dados separados dentro da "matriz_traj"

    # Indice por lista : [0][0] = t/s, [0][1] = x/m, [0][2] = y/m





    #Raio de interceptação
    querAlterarRaio = int(input("Deseja alterar o raio de interceptação? Raio padrão: 10.54 cm \n(0-Não/1-Sim) "))

    if querAlterarRaio == 1:
        raio_interceptacao = (float(input("Digite o novo raio de interceptação em cm: ")))/100

    else:
        #Tem esse intervalo por causa da incerteza de 0.5 - R = 10.29 +- 0.25 -> 0.1054 metros
        raio_interceptacao = 0.1054

    #Dados iniciais do robo:
    xi_bola = float(matriz_trajetoria[0][1])
    yi_bola = float(matriz_trajetoria[0][2])
    x_robo,y_robo = gerar_posicao_inicial(xi_bola,yi_bola)

    robo = {
        'querAlterarRaio': querAlterarRaio, #int (bool - 0 or 1)
        'raio_interceptacao': raio_interceptacao, #float
        'x': x_robo, #float
        'y': y_robo, #float
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

    mostrarDadosIniciais(matriz_trajetoria,robo,bola)
    
    if (robo['querAlterarRaio']==0):
        movimentarRoboRaioPadrao(matriz_trajetoria,robo,bola)
    else:
        movimentarRoboRaioAlterado(matriz_trajetoria,robo,bola)

    print("Fim do programa")

if __name__ == "__main__":#Verifica de esta executando no arquivo principal
    main()
    