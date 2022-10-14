def gerarDados(t,x_robo, y_robo,velocidade_x,velocidade_y,distancia):    
    #Cadastro dos dados referentes as posição do robo (x_y_robo.txt)
    cadastro_users = open("Dados_Grafico/x_y_robo.txt", "a") # Comando para abrir o arquivo "cadastro_users", aonde ficaram armazenados os cadastros de todos os clientes.
    cadastro_users.write("%.2f\t%.2f\t%.2f\n" %(t,x_robo,y_robo))#Inserção de nome_user, cpf_user e senha_user no arquivo "cadastro_users"
    cadastro_users.close()#Fecha e salva as informações no arquivo

    #Cadastro dos dados referentes a velocidade do robo no eixo x e y (x_y_robo.txt)
    cadastro_users = open("Dados_Grafico/vx_vy_robo.txt", "a") # Comando para abrir o arquivo "cadastro_users", aonde ficaram armazenados os cadastros de todos os clientes.
    cadastro_users.write("%.2f\t%.2f\t%.2f\n" %(t,velocidade_x,velocidade_y))#Inserção de nome_user, cpf_user e senha_user no arquivo "cadastro_users"
    cadastro_users.close()#Fecha e salva as informações no arquivo

    #Cadastro dos dados referentes a distância entre o robo e a bola (x_y_robo.txt)
    cadastro_users = open("Dados_Grafico/distancia_robo_bola.txt", "a") # Comando para abrir o arquivo "cadastro_users", aonde ficaram armazenados os cadastros de todos os clientes.
    cadastro_users.write("%.2f\t%.2f\n" %(t,distancia))#Inserção de nome_user, cpf_user e senha_user no arquivo "cadastro_users"
    cadastro_users.close()#Fecha e salva as informações no arquivo