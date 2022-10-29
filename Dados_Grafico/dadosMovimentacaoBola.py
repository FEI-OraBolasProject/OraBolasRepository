
def dadosVelBola(tempoFinal):

    # Leitura de dados do arquivo trajetoria_bola.txt
    traj_bola = open("trajetoria_formatada.txt", "r")  #
    dados = traj_bola.readlines()  # faz a leitura das linhas presentes no arquivo
    traj_bola.close()
    matriz_traj = []  # matriz_pedidos (os dados seram organizados dentro dela )

    for i in range(len(dados)):
        palavra = dados[i].strip('\n')  # remove a quebra de linha presentes na linha do arquivo
        palavra = palavra.replace(",", ".")  # substitui a virgula por ponto
        palavra = palavra.split("\t")  # seleciona os dados separados por "\t"

        matriz_traj.append(palavra)  # insere os dados separados dentro da "matriz_traj"

    velocidade_bola = open("Dados_Grafico/Gerar_Grafico/velocidade_bola.txt", "w")

    for linha in range(len(matriz_traj)-1):
        tempo = float(matriz_traj[linha][0])

        if tempo == tempoFinal:
            break

        x_base = float(matriz_traj[linha][1])
        y_base = float(matriz_traj[linha][2])

        x_proximo = float(matriz_traj[linha + 1][1])
        y_proximo = float(matriz_traj[linha + 1][2])

        distancia_x = x_proximo - x_base
        distancia_y = y_proximo - y_base

        velocidade_x = distancia_x/0.2
        velocidade_y = distancia_y/0.2

        velocidade_bola.write("%.2f\t%.2f\t%.2f\n" % (tempo, velocidade_x, velocidade_y))

    velocidade_bola.close()


def dadosAcelBola(tempoFinal):
    # Leitura de dados do arquivo trajetoria_bola.txt
    velocidade_bola = open("Dados_Grafico/Gerar_Grafico/velocidade_bola.txt", "r")  #
    dados = velocidade_bola.readlines()  # faz a leitura das linhas presentes no arquivo
    velocidade_bola.close()
    matriz_vel = []  # matriz_pedidos (os dados seram organizados dentro dela )

    for i in range(len(dados)):
        palavra = dados[i].strip('\n')  # remove a quebra de linha presentes na linha do arquivo
        palavra = palavra.replace(",", ".")  # substitui a virgula por ponto
        palavra = palavra.split("\t")  # seleciona os dados separados por "\t"

        matriz_vel.append(palavra)  # insere os dados separados dentro da "matriz_traj"

    aceleracao_bola = open("Dados_Grafico/Gerar_Grafico/acel_bola.txt", "w")

    for linha in range(len(matriz_vel) - 1):
        tempo = float(matriz_vel[linha][0])

        vx_base = float(matriz_vel[linha][1])
        vy_base = float(matriz_vel[linha][2])

        vx_proximo = float(matriz_vel[linha + 1][1])
        vy_proximo = float(matriz_vel[linha + 1][2])

        delta_vx = vx_proximo - vx_base
        delta_vy = vy_proximo - vy_base

        aceleracao_x = delta_vx / 0.2
        aceleracao_y = delta_vy / 0.2

        aceleracao_bola.write("%.2f\t%.2f\t%.2f\n" % (tempo, aceleracao_x, aceleracao_y))

    aceleracao_bola.close()
