def gerarDados(tempo,robo,bola): 
    
    if robo['querAlterarRaio'] == 0:
        #Arquivos contendo os dados referentes as posição do robo e bola(x_y_robo.txt):
        posicao_robo_bola = open("Dependencias/Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt", "a") # Abre o arquivo
        posicao_robo_bola.write("%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n" %(tempo,robo['x'],robo['y'],bola['x'],bola['y']))#Inserção de dados no arquivo
        posicao_robo_bola.close()#Fecha e salva as informações no arquivo


        #Arquivo contendo os dados referentes a velocidade do robo no eixo x e y (vx_vy_robo.txt):
        vx_vy_robo = open("Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_robo.txt", "a") #Abre o arquivo
        vx_vy_robo.write("%.2f\t%.2f\t%.2f\n" %(tempo,robo['vel_x'],robo['vel_y']))#Inserção de dados no arquivo
        vx_vy_robo.close()#Fecha e salva as informações no arquivo


        #Arquivo contendo os dados referentes a distância entre o robo e a bola (distancia_robo_bola.txt):
        distancia_robo_bola = open("Dependencias/Dados_Grafico/Gerar_Grafico/distancia_robo_bola.txt", "a") # Abre o arquivo
        distancia_robo_bola.write("%.2f\t%.2f\n" %(tempo,bola['distancia_robo']))#Inserção de dados no arquivo
        distancia_robo_bola.close()#Fecha e salva as informações no arquivo

        #Arquivo contendo os dados referentes a aceleração do robo no eixo x e y (cx_cy_aceleracao_robo.txt):
        aceleracao_robo = open("Dependencias/Dados_Grafico/Gerar_Grafico/acel_robo.txt", "a") # Abre o arquivo
        aceleracao_robo.write("%.2f\t%.2f\t%.2f\n" %(tempo,robo['acel_x'],robo['acel_y']))#Inserção de dados no arquivo
        aceleracao_robo.close()#Fecha e salva as informações no arquivo    
    
    else:
        #Arquivos contendo os dados referentes as posição do robo e bola(x_y_robo.txt):
        posicao_robo_bola = open("Dependencias/Dados_Grafico/Gerar_Grafico/RA_x_y_robo_bola.txt", "a") # Abre o arquivo
        posicao_robo_bola.write("%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n" %(tempo,robo['x'],robo['y'],bola['x'],bola['y']))#Inserção de dados no arquivo
        posicao_robo_bola.close()#Fecha e salva as informações no arquivo


        #Arquivo contendo os dados referentes a velocidade do robo no eixo x e y (vx_vy_robo.txt):
        vx_vy_robo = open("Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_robo.txt", "a") #Abre o arquivo
        vx_vy_robo.write("%.2f\t%.2f\t%.2f\n" %(tempo,robo['vel_x'],robo['vel_y']))#Inserção de dados no arquivo
        vx_vy_robo.close()#Fecha e salva as informações no arquivo


        #Arquivo contendo os dados referentes a distância entre o robo e a bola (distancia_robo_bola.txt):
        distancia_robo_bola = open("Dependencias/Dados_Grafico/Gerar_Grafico/RA_distancia_robo_bola.txt", "a") # Abre o arquivo
        distancia_robo_bola.write("%.2f\t%.2f\n" %(tempo,bola['distancia_robo']))#Inserção de dados no arquivo
        distancia_robo_bola.close()#Fecha e salva as informações no arquivo

        #Arquivo contendo os dados referentes a aceleração do robo no eixo x e y (cx_cy_aceleracao_robo.txt):
        aceleracao_robo = open("Dependencias/Dados_Grafico/Gerar_Grafico/RA_acel_robo.txt", "a") # Abre o arquivo
        aceleracao_robo.write("%.2f\t%.2f\t%.2f\n" %(tempo,robo['acel_x'],robo['acel_y']))#Inserção de dados no arquivo
        aceleracao_robo.close()#Fecha e salva as informações no arquivo    

    