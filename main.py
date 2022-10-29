from Interceptacao_Bola.interceptacao_bola import interceptacao_bola
from Interceptacao_Bola.posicao_inicial_robo import gerar_posicao_inicial
from Dados_Grafico.dadosMovimentacaoBola import dadosVelBola,dadosAcelBola
from Dados_Grafico.Gerar_Grafico.chamar_grafico import criar_graficos
from Dados_Grafico.velocidadeRelativa import pegarVelRelativa
import os
def main():
    path = os.getcwd()
    try:
        #Remover os dados caso o programa já tenha sido rodado!
        os.remove(path + '/Dados_Grafico/Gerar_Grafico/acel_robo.txt')
        os.remove(path + '/Dados_Grafico/Gerar_Grafico/acel_bola.txt')
        os.remove(path + '/Dados_Grafico/Gerar_Grafico/distancia_robo_bola.txt')
        os.remove(path + '/Dados_Grafico/Gerar_Grafico/velocidade_bola.txt')
        os.remove(path + '/Dados_Grafico/Gerar_Grafico/velocidade_robo.txt')
        os.remove(path + '/Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt')
        os.remove(path + '/Dados_Grafico/Gerar_Grafico/velocidade_relativa.txt')
        os.rmdir(path + '/Dados_Grafico/Gerar_Grafico/Graficos')
    except:
        pass

    try:
        os.mkdir(path + '/Dados_Grafico/Gerar_Grafico/Graficos')
    except:
        pass

    #Leitura de dados do arquivo trajetoria_bola.txt
    traj_bola = open("trajetoria_formatada.txt", "r")#
    dados = traj_bola.readlines()#faz a leitura das linhas presentes no arquivo

    matriz_traj = [] #matriz_pedidos (os dados seram organizados dentro dela )

    for i in range(len(dados)):
        palavra = dados[i].strip('\n')#remove a quebra de linha presentes na linha do arquivo
        palavra = palavra.replace(",",".")#substitui a virgula por ponto
        palavra = palavra.split("\t")#seleciona os dados separados por "\t"

        matriz_traj.append(palavra)#insere os dados separados dentro da "matriz_traj"

    # Indice por lista : [0][0] = t/s, [0][1] = x/m, [0][2] = y/m

    #Dados iniciais do robo:
    xi_bola = float(matriz_traj[0][1])
    yi_bola = float(matriz_traj[0][2])
    x_robo,y_robo = gerar_posicao_inicial(xi_bola,yi_bola)
    velocidade = 0
    vmax = 0
    aceleracao = 0

    #Raio de interceptação
    escolha = int(input("Deseja alterar o raio de interceptação? (1-Sim/2-Não) "))
    if escolha == 1:
        raio_interceptacao = float(input("Digite o novo raio de interceptação: "))
    else:
        #Tem esse intervalo por causa da incerteza de 0.5 - R = 10.29 +- 0.25 -> 0.1054 metros
        raio_interceptacao = 0.1054

    #Exibe os dados presentes na "matriz_traj" :" : 
    for linha in range(len(matriz_traj)):
        
        tempo = float(matriz_traj[linha][0])
        x_bola = float((matriz_traj[linha][1]))
        y_bola = float(matriz_traj[linha][2])

        x_robo, y_robo, velocidade, aceleracao, vmax, interceptacao = interceptacao_bola(tempo,x_bola,y_bola,x_robo, y_robo, velocidade, aceleracao, vmax,raio_interceptacao)

        if (interceptacao == True):
            break
        else:
            pass

    #Para testarmos é melhor tirar o tempo, depois a gente coloca!!!
    #time.sleep(0.2)# leitura dos dados a cada 2 segundos

    #Pegar valores da velocidade e aceleracao da bola:
    dadosVelBola(tempo)
    dadosAcelBola(tempo)
    pegarVelRelativa()
    

    print("Fim do programa")

    traj_bola.close()#fecha o arquivo

if __name__ == "__main__":#Verifica de esta executando no arquivo principal
    main()
    criar_graficos()