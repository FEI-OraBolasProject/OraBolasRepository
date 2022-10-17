from ast import main
import os
from Interceptacao_Bola.interceptacao_bola import interceptacao_bola

def main():

    #Apaga os arquivos preexistentes para criação dos gráficos. Evitando conflitos quando a posição do robo é sorteada novamente
    if(os.path.isfile("Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt" or "Dados_Grafico/Gerar_Grafico/vx_vy_robo.txt" or "Dados_Grafico/Gerar_Grafico/distancia_robo_bola.txt"or "Dados_Grafico/Gerar_Grafico/cx_cy_aceleracao_robo.txt")):#Verifica se existe esses arquivo na pasta "Dados_Grafico"
        os.remove("Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt")#Remove o arquivo
        os.remove("Dados_Grafico/Gerar_Grafico/vx_vy_robo.txt")#Remove o arquivo
        os.remove("Dados_Grafico/Gerar_Grafico/distancia_robo_bola.txt")#Remove o arquivo
        os.remove("Dados_Grafico/Gerar_Grafico/cx_cy_aceleracao_robo.txt")#Remove o arquivo
        

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
    #Exibe os dados presentes na "matriz_traj" :" : 
    for linha in range(len(matriz_traj)):
        
        tempo = float(matriz_traj[linha][0])
        x_bola = float((matriz_traj[linha][1]))
        y_bola = float(matriz_traj[linha][2])

        interceptacao = interceptacao_bola(tempo,x_bola,y_bola)

        if (interceptacao == True):
            break
        else:
            pass

    #Para testarmos é melhor tirar o tempo, depois a gente coloca!!!
    #time.sleep(0.2)# leitura dos dados a cada 2 segundos

    print("Fim do programa")

    traj_bola.close()#fecha o arquivo

if __name__ == "__main__":#Verifica de esta executando no arquivo principal

    main()