from cProfile import label
from re import X
import sys
import matplotlib
import tkinter
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

#separar em listas as linhas do excel
dataset = open("x_y_robo_bola.txt", "r")
linhas = dataset.readlines()

ListaLinhas = []
tempo = []
Bola_coordY = []
Robo_coordY = []

for i in range(1,len(linhas)):
    ListaLinhas.append(linhas[i].strip("\n").replace(",",".").split("\t"))

for item in ListaLinhas:
    tempo.append(float(item[0]))
    Bola_coordY.append(float(item[2]))
    Robo_coordY.append(float(item[4]))

print(tempo)
print(Bola_coordY)
print(Robo_coordY)

plt.plot(tempo,Bola_coordY)
plt.plot(tempo,Robo_coordY)

plt.title("Posicao Y em funcao do Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Coordenada Y (m)")
plt.legend(["Bola","Robo"])

plt.savefig("y_t_robo_bola.png", dpi=300, bbox_inches='tight')
plt.show()
