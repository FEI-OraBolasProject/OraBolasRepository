from math import *


def pegarVelRelativa(robo):

    if robo['querAlterarRaio'] == 0:

    # Leitura de dados do arquivo velocidade_bola.txt
        velocidade_bola = open("Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_bola.txt", "r")  #
        dados = velocidade_bola.readlines()  # faz a leitura das linhas presentes no arquivo
        velocidade_bola.close()
        matriz_vel_bola = []  # matriz_pedidos (os dados seram organizados dentro dela )

        for i in range(len(dados)):
            palavra = dados[i].strip('\n')  # remove a quebra de linha presentes na linha do arquivo
            palavra = palavra.replace(",", ".")  # substitui a virgula por ponto
            palavra = palavra.split("\t")  # seleciona os dados separados por "\t"

            matriz_vel_bola.append(palavra)  # insere os dados separados dentro da "matriz_traj"

    # Leitura de dados do arquivo velocidade_robo.txt
        velocidade_robo = open("Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_robo.txt", "r")  #
        dados = velocidade_robo.readlines()  # faz a leitura das linhas presentes no arquivo
        velocidade_robo.close()
        matriz_vel_robo = []  # matriz_pedidos (os dados seram organizados dentro dela )

        for i in range(len(dados)):
            palavra = dados[i].strip('\n')  # remove a quebra de linha presentes na linha do arquivo
            palavra = palavra.replace(",", ".")  # substitui a virgula por ponto
            palavra = palavra.split("\t")  # seleciona os dados separados por "\t"

            matriz_vel_robo.append(palavra)  # insere os dados separados dentro da "matriz_traj"



        velocidade_relativa = open("Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_relativa.txt", "w")


        for linha in range(1,len(matriz_vel_bola)):
            tempo = float(matriz_vel_robo[linha][0])

            velocidade_relativa_x = float(matriz_vel_bola[linha-1][1]) - float(matriz_vel_robo[linha][1])
            velocidade_relativa_y = float(matriz_vel_bola[linha-1][2]) - float(matriz_vel_robo[linha][2])

            modulo_velocidade_relativa = sqrt((velocidade_relativa_x**2)+(velocidade_relativa_y**2))

            velocidade_relativa.write("%.2f\t%.2f\n" % (tempo, modulo_velocidade_relativa))

        velocidade_relativa.close()

        return 0
    
    else:
        # Leitura de dados do arquivo velocidade_bola.txt
        velocidade_bola = open("Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_bola.txt", "r")  #
        dados = velocidade_bola.readlines()  # faz a leitura das linhas presentes no arquivo
        velocidade_bola.close()
        matriz_vel_bola = []  # matriz_pedidos (os dados seram organizados dentro dela )

        for i in range(len(dados)):
            palavra = dados[i].strip('\n')  # remove a quebra de linha presentes na linha do arquivo
            palavra = palavra.replace(",", ".")  # substitui a virgula por ponto
            palavra = palavra.split("\t")  # seleciona os dados separados por "\t"

            matriz_vel_bola.append(palavra)  # insere os dados separados dentro da "matriz_traj"

    # Leitura de dados do arquivo velocidade_robo.txt
        velocidade_robo = open("Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_robo.txt", "r")  #
        dados = velocidade_robo.readlines()  # faz a leitura das linhas presentes no arquivo
        velocidade_robo.close()
        matriz_vel_robo = []  # matriz_pedidos (os dados seram organizados dentro dela )

        for i in range(len(dados)):
            palavra = dados[i].strip('\n')  # remove a quebra de linha presentes na linha do arquivo
            palavra = palavra.replace(",", ".")  # substitui a virgula por ponto
            palavra = palavra.split("\t")  # seleciona os dados separados por "\t"

            matriz_vel_robo.append(palavra)  # insere os dados separados dentro da "matriz_traj"



        velocidade_relativa = open("Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_relativa.txt", "w")


        for linha in range(1,len(matriz_vel_bola)):
            tempo = float(matriz_vel_robo[linha][0])

            velocidade_relativa_x = float(matriz_vel_bola[linha-1][1]) - float(matriz_vel_robo[linha][1])
            velocidade_relativa_y = float(matriz_vel_bola[linha-1][2]) - float(matriz_vel_robo[linha][2])

            modulo_velocidade_relativa = sqrt((velocidade_relativa_x**2)+(velocidade_relativa_y**2))

            velocidade_relativa.write("%.2f\t%.2f\n" % (tempo, modulo_velocidade_relativa))

        velocidade_relativa.close()

        return 0


        