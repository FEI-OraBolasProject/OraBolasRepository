import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os

def aceleracao_robo(robo,path=os.getcwd()):

    if (robo['querAlterarRaio'] == 0):

        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/acel_robo.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        cx = []
        cy = []

        for i in range(1,len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",",".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            cx.append(float(item[1]))
            cy.append(float(item[2]))

        plt.plot(tempo,cx)
        plt.plot(tempo,cy)

        plt.title("Grafico da aceleracao X (m/s²) e Y (m/s²) do Robo em funcao do Tempo (s)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Aceleração (m/s²)")
        plt.legend(["Aceleração X do robo","Aceleração Y do robo"])

        plt.savefig("Graficos_Raio_Padrao/acel_robo.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    else:
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/RA_acel_robo.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        cx = []
        cy = []

        for i in range(1,len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",",".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            cx.append(float(item[1]))
            cy.append(float(item[2]))

        plt.plot(tempo,cx)
        plt.plot(tempo,cy)

        plt.title("Grafico da aceleracao X (m/s²) e Y (m/s²) do Robo em funcao do Tempo (s) com Raio de Interceptação Alterado: %.3f cm" %(robo['raio_interceptacao']*100))
        plt.xlabel("Tempo (s)")
        plt.ylabel("Aceleração (m/s²)")
        plt.legend(["Aceleração X do robo","Aceleração Y do robo"])

        plt.savefig("Graficos_Raio_Alterado/RA_acel_robo.png", dpi=300, bbox_inches='tight')
        plt.close()

def aceleracao_bola(robo,path=os.getcwd()):
    if (robo['querAlterarRaio'] == 0):
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/acel_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        cx = []
        cy = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            cx.append(float(item[1]))
            cy.append(float(item[2]))

        plt.plot(tempo, cx)
        plt.plot(tempo, cy)

        plt.title("Grafico de aceleracao X (m/s²) e Y (m/s²) da Bola em funcao do Tempo (s)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Aceleração (m/s²)")
        plt.legend(["Aceleração X da bola", "Aceleração Y da bola"])

        plt.savefig("Graficos_Raio_Padrao/acel_bola.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    else:  
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/RA_acel_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        cx = []
        cy = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            cx.append(float(item[1]))
            cy.append(float(item[2]))

        plt.plot(tempo, cx)
        plt.plot(tempo, cy)

        plt.title("Grafico de aceleracao X (m/s²) e Y (m/s²) da Bola em funcao do Tempo (s) com Raio de Interceptação Alterado: %.3f cm" %(robo['raio_interceptacao']*100))
        plt.xlabel("Tempo (s)")
        plt.ylabel("Aceleração (m/s²)")
        plt.legend(["Aceleração X da bola", "Aceleração Y da bola"])

        plt.savefig("Graficos_Raio_Alterado/RA_acel_bola.png", dpi=300, bbox_inches='tight')
        plt.close()


def distancia_relativa(robo,path=os.getcwd()):
    if (robo['querAlterarRaio'] == 0):
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/distancia_robo_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Distancia = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Distancia.append(float(item[1]))

        plt.plot(tempo, Distancia)

        plt.title("Grafico da distancia (m) entre Robo e Bola em funcao do Tempo (s)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Distancia (m)")
        plt.legend(["Distancia"])

        plt.savefig("Graficos_Raio_Padrao/distancia_robo_bola.png", dpi=300, bbox_inches='tight')
        plt.close()
        
    else:
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/RA_distancia_robo_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Distancia = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Distancia.append(float(item[1]))

        plt.plot(tempo, Distancia)

        plt.title("Grafico da distancia (m) entre Robo e Bola em funcao do Tempo (s) com Raio de Interceptação Alterado: %.3f cm" %(robo['raio_interceptacao']*100))
        plt.xlabel("Tempo (s)")
        plt.ylabel("Distancia (m)")
        plt.legend(["Distancia"])

        plt.savefig("Graficos_Raio_Alterado/RA_distancia_robo_bola.png", dpi=300, bbox_inches='tight')
        plt.close()

def velocidade_bola(robo,path = os.getcwd()):
    if (robo['querAlterarRaio'] == 0):
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Robo_Vx = []
        Robo_Vy = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Robo_Vx.append(float(item[1]))
            Robo_Vy.append(float(item[2]))

        plt.plot(tempo, Robo_Vx)
        plt.plot(tempo, Robo_Vy)

        plt.title("Grafico da velocidade X (m/s) e Y (m/s) da Bola em funcao do Tempo (s)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade (m/s)")
        plt.legend(["Velocidade X da bola", "Velocidade Y da bola"])

        plt.savefig("Graficos_Raio_Padrao/velocidade_bola.png", dpi=300, bbox_inches='tight')
        plt.close()
        
    else:
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Robo_Vx = []
        Robo_Vy = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Robo_Vx.append(float(item[1]))
            Robo_Vy.append(float(item[2]))

        plt.plot(tempo, Robo_Vx)
        plt.plot(tempo, Robo_Vy)

        plt.title("Grafico da velocidade X (m/s) e Y (m/s) da Bola em funcao do Tempo (s) com Raio de Interceptação Alterado: %.3f cm" %(robo['raio_interceptacao']*100))
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade (m/s)")
        plt.legend(["Velocidade X da bola", "Velocidade Y da bola"])

        plt.savefig("Graficos_Raio_Alterado/RA_velocidade_bola.png", dpi=300, bbox_inches='tight')
        plt.close()
        

def velocidade_robo(robo,path = os.getcwd()):

    if (robo['querAlterarRaio'] == 0):
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_robo.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Robo_Vx = []
        Robo_Vy = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Robo_Vx.append(float(item[1]))
            Robo_Vy.append(float(item[2]))

        plt.plot(tempo, Robo_Vx)
        plt.plot(tempo, Robo_Vy)

        plt.title("Grafico da velocidade X (m/s) e Y (m/s) do Robo em funcao do Tempo (s)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade (m/s)")
        plt.legend(["Velocidade X do robo", "Velocidade Y do robo"])

        plt.savefig("Graficos_Raio_Padrao/velocidade_robo.png", dpi=300, bbox_inches='tight')
        plt.close()
        
    else:
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_robo.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Robo_Vx = []
        Robo_Vy = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Robo_Vx.append(float(item[1]))
            Robo_Vy.append(float(item[2]))

        plt.plot(tempo, Robo_Vx)
        plt.plot(tempo, Robo_Vy)

        plt.title("Grafico da velocidade X (m/s) e Y (m/s) do Robo em funcao do Tempo (s) com Raio de Interceptação Alterado: %.3f cm" %(robo['raio_interceptacao']*100))
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade (m/s)")
        plt.legend(["Velocidade X do robo", "Velocidade Y do robo"])

        plt.savefig("Graficos_Raio_Alterado/RA_velocidade_robo.png", dpi=300, bbox_inches='tight')
        plt.close()

def pos_x_robo_bola(robo,path=os.getcwd()):

    if (robo['querAlterarRaio'] == 0):
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Bola_coordX = []
        Robo_coordX = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Bola_coordX.append(float(item[1]))
            Robo_coordX.append(float(item[3]))

        plt.plot(tempo, Bola_coordX)
        plt.plot(tempo, Robo_coordX)

        plt.title("Grafico da posicao X (m) do robo e da bola em funcao do Tempo (s)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Coordenada X (m)")
        plt.legend(["Posicao X da bola", "Posicao X do robo"])

        plt.savefig("Graficos_Raio_Padrao/x_t_robo_bola.png", dpi=300, bbox_inches='tight')
        plt.close()
        
    else:
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/RA_x_y_robo_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Bola_coordX = []
        Robo_coordX = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Bola_coordX.append(float(item[1]))
            Robo_coordX.append(float(item[3]))

        plt.plot(tempo, Bola_coordX)
        plt.plot(tempo, Robo_coordX)

        plt.title("Grafico da posicao X (m) do robo e da bola em funcao do Tempo (s) com Raio de Interceptação Alterado: %.3f cm" %(robo['raio_interceptacao']*100))
        plt.xlabel("Tempo (s)")
        plt.ylabel("Coordenada X (m)")
        plt.legend(["Posicao X da bola", "Posicao X do robo"])

        plt.savefig("Graficos_Raio_Alterado/RA_x_t_robo_bola.png", dpi=300, bbox_inches='tight')
        plt.close()


def pos_xy_robo_bola(robo,path=os.getcwd()):

    if (robo['querAlterarRaio'] == 0):
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Robo_coordX = []
        Robo_coordY = []
        Bola_coordX = []
        Bola_coordY = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Robo_coordX.append(float(item[1]))
            Robo_coordY.append(float(item[2]))
            Bola_coordX.append(float(item[3]))
            Bola_coordY.append(float(item[4]))

        plt.plot(Bola_coordX, Bola_coordY)
        plt.plot(Robo_coordX, Robo_coordY)
        # plt.plot(tempo,coordX)

        plt.title("Grafico da posicao X (m) do Robo e da Bola em funcao da posicao Y (m)")
        plt.xlabel("Coordenada X (m)")
        plt.ylabel("Coordenada Y (m)")
        plt.legend(["Posicao da Bola", "Posicao do Robo"])

        plt.savefig("Graficos_Raio_Padrao/x_y_robo_bola.png", dpi=300, bbox_inches='tight')
        plt.close()
        
    else:
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/RA_x_y_robo_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Robo_coordX = []
        Robo_coordY = []
        Bola_coordX = []
        Bola_coordY = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Robo_coordX.append(float(item[1]))
            Robo_coordY.append(float(item[2]))
            Bola_coordX.append(float(item[3]))
            Bola_coordY.append(float(item[4]))

        plt.plot(Bola_coordX, Bola_coordY)
        plt.plot(Robo_coordX, Robo_coordY)
        # plt.plot(tempo,coordX)

        plt.title("Grafico da posicao X (m) do Robo e da Bola em funcao da posicao Y (m) com Raio de Interceptação Alterado: %.3f cm" %(robo['raio_interceptacao']*100))
        plt.xlabel("Coordenada X (m)")
        plt.ylabel("Coordenada Y (m)")
        plt.legend(["Posicao da Bola", "Posicao do Robo"])

        plt.savefig("Graficos_Raio_Alterado/RA_x_y_robo_bola.png", dpi=300, bbox_inches='tight')
        plt.close()


def pos_y_robo_bola(robo,path = os.getcwd()):

    if (robo['querAlterarRaio'] == 0):
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Bola_coordY = []
        Robo_coordY = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Bola_coordY.append(float(item[2]))
            Robo_coordY.append(float(item[4]))

        plt.plot(tempo, Bola_coordY)
        plt.plot(tempo, Robo_coordY)

        plt.title("Grafico da posicao Y (m) do robo e da bola em funcao do Tempo (s)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Coordenada Y (m)")
        plt.legend(["Posicao Y da Bola", "Posicao Y do Robo"])

        plt.savefig("Graficos_Raio_Padrao/y_t_robo_bola.png", dpi=300, bbox_inches='tight')
        plt.close()
        
    else:
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/RA_x_y_robo_bola.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        Bola_coordY = []
        Robo_coordY = []

        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            Bola_coordY.append(float(item[2]))
            Robo_coordY.append(float(item[4]))

        plt.plot(tempo, Bola_coordY)
        plt.plot(tempo, Robo_coordY)

        plt.title("Grafico da posicao Y (m) do robo e da bola em funcao do Tempo (s) com Raio de Interceptação Alterado: %.3f cm" %(robo['raio_interceptacao']*100))
        plt.xlabel("Tempo (s)")
        plt.ylabel("Coordenada Y (m)")
        plt.legend(["Posicao Y da Bola", "Posicao Y do Robo"])

        plt.savefig("Graficos_Raio_Alterado/RA_y_t_robo_bola.png", dpi=300, bbox_inches='tight')
        plt.close()


def criarGraficoVelocidadeRelativa(robo,path = os.getcwd()):

    if (robo['querAlterarRaio'] == 0):
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_relativa.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        velocidade_relativa = []


        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            velocidade_relativa.append(float(item[1]))

        plt.plot(tempo, velocidade_relativa)
    

        plt.title("Gráfico da velocidade relativa (m/s )entre o robo e a bola em funcao do Tempo (s)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade Relativa (m/s)")

        plt.savefig("Graficos_Raio_Padrao/velocidade_relativa.png", dpi=300, bbox_inches='tight')
        plt.close()
        
    else:
        # separar em listas as linhas do excel
        dataset = open(path + "/Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_relativa.txt", "r")
        linhas = dataset.readlines()

        ListaLinhas = []
        tempo = []
        velocidade_relativa = []


        for i in range(1, len(linhas)):
            ListaLinhas.append(linhas[i].strip("\n").replace(",", ".").split("\t"))

        for item in ListaLinhas:
            tempo.append(float(item[0]))
            velocidade_relativa.append(float(item[1]))

        plt.plot(tempo, velocidade_relativa)
    

        plt.title("Gráfico da velocidade relativa (m/s )entre o robo e a bola em funcao do Tempo (s) com Raio de Interceptação Alterado: %.3f cm" %(robo['raio_interceptacao']*100))
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade Relativa (m/s)")

        plt.savefig("Graficos_Raio_Alterado/RA_velocidade_relativa.png", dpi=300, bbox_inches='tight')
        plt.close()


def criar_graficos(robo):

    pos_xy_robo_bola(robo)
    pos_x_robo_bola(robo)
    pos_y_robo_bola(robo)
    distancia_relativa(robo)
    criarGraficoVelocidadeRelativa(robo)
    velocidade_bola(robo)
    velocidade_robo(robo)
    aceleracao_robo(robo)
    aceleracao_bola(robo)
    
