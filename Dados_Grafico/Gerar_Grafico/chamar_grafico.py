import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
def aceleracao_robo(path=os.getcwd()):
    dataset = open(path + "/Dados_Grafico/Gerar_Grafico/acel_robo.txt", "r")
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

    plt.title("Aceleracao X e Y do Robo em funcao do Tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Aceleração (m/s²)")
    plt.legend(["Aceleração X","Aceleração Y"])

    plt.savefig(path + "/Dados_Grafico/Gerar_Grafico/Graficos/acel_robo.png", dpi=300, bbox_inches='tight')
    plt.show()
def aceleracao_bola(path=os.getcwd()):
    # separar em listas as linhas do excel
    dataset = open(path + "/Dados_Grafico/Gerar_Grafico/acel_bola.txt", "r")
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

    plt.title("Aceleracao X e Y do Bola em funcao do Tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Aceleração (m/s²)")
    plt.legend(["Aceleração X", "Aceleração Y"])

    plt.savefig(path + "/Dados_Grafico/Gerar_Grafico/Graficos/acel_bola.png", dpi=300, bbox_inches='tight')
    plt.show()
def distancia_relativa(path=os.getcwd()):
    # separar em listas as linhas do excel
    dataset = open(path + "/Dados_Grafico/Gerar_Grafico/distancia_robo_bola.txt", "r")
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

    plt.title("Distancia entre Robo e Bola em funcao do Tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Distancia (m)")
    plt.legend(["Distancia"])

    plt.savefig(path + "/Dados_Grafico/Gerar_Grafico/Graficos/distancia_robo_bola.png", dpi=300, bbox_inches='tight')
    plt.show()
def velocidade_bola(path = os.getcwd()):
    # separar em listas as linhas do excel
    dataset = open(path + "/Dados_Grafico/Gerar_Grafico/velocidade_bola.txt", "r")
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

    plt.title("Velocidade X e Y da Bola em funcao do Tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Velocidade X e Y")
    plt.legend(["Velocidade X", "Velocidade Y"])

    plt.savefig(path + "/Dados_Grafico/Gerar_Grafico/Graficos/velocidade_bola.png", dpi=300, bbox_inches='tight')
    plt.show()
def velocidade_robo(path = os.getcwd()):

    # separar em listas as linhas do excel
    dataset = open(path + "/Dados_Grafico/Gerar_Grafico/velocidade_robo.txt", "r")
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

    plt.title("Velocidade X e Y do Robo em funcao do Tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Velocidade X e Y")
    plt.legend(["Velocidade X", "Velocidade Y"])

    plt.savefig(path + "/Dados_Grafico/Gerar_Grafico/Graficos/velocidade_robo.png", dpi=300, bbox_inches='tight')
    plt.show()
def pos_x_robo_bola(path=os.getcwd()):
    # separar em listas as linhas do excel
    dataset = open(path + "/Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt", "r")
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

    plt.title("Posicao X em funcao do Tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Coordenada X (m)")
    plt.legend(["Bola", "Robo"])

    plt.savefig(path + "/Dados_Grafico/Gerar_Grafico/Graficos/x_t_robo_bola.png", dpi=300, bbox_inches='tight')
    plt.show()
def pos_xy_robo_bola(path=os.getcwd()):
    # separar em listas as linhas do excel
    dataset = open(path + "/Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt", "r")
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

    plt.title("Posicao do Robo e da Bola (posicao Y em funcao de X")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.legend(["Bola", "Robo"])

    plt.savefig(path + "/Dados_Grafico/Gerar_Grafico/Graficos/x_y_robo_bola.png", dpi=300, bbox_inches='tight')
    plt.show()
def pos_y_robo_bola(path = os.getcwd()):
    # separar em listas as linhas do excel
    dataset = open(path + "/Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt", "r")
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

    plt.title("Posicao Y em funcao do Tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Coordenada Y (m)")
    plt.legend(["Bola", "Robo"])

    plt.savefig(path + "/Dados_Grafico/Gerar_Grafico/Graficos/y_t_robo_bola.png", dpi=300, bbox_inches='tight')
    plt.show()

def criar_graficos():
    aceleracao_robo()
    aceleracao_bola()
    distancia_relativa()
    velocidade_bola()
    velocidade_robo()
    pos_y_robo_bola()
    pos_x_robo_bola()
    pos_xy_robo_bola()
