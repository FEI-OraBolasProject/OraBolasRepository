import matplotlib.pyplot as plt
import numpy as np

#Aceleração do Robo
def aceleracao_robo():

    dataset = open("cx_cy_aceleracao_robo.txt", "r")
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

    print(tempo)
    print(cx)
    print(cy)

    plt.plot(tempo,cx)
    plt.plot(tempo,cy)

    plt.title("Aceleracao X e Y do Robo em funcao do Tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Aceleração (m/s²)")
    plt.legend(["Aceleração X","Aceleração Y"])

    plt.savefig("img/cx_cy_aceleracao_robo.png", dpi=300, bbox_inches='tight')
    plt.show()