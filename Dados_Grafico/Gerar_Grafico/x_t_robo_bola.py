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
Bola_coordX = []
Robo_coordX = []

for i in range(1,len(linhas)):
    ListaLinhas.append(linhas[i].strip("\n").replace(",",".").split("\t"))

for item in ListaLinhas:
    tempo.append(float(item[0]))
    Bola_coordX.append(float(item[1]))
    Robo_coordX.append(float(item[3]))

print(tempo)
print(Bola_coordX)
print(Robo_coordX)

plt.plot(tempo,Bola_coordX)
plt.plot(tempo,Robo_coordX)

plt.title("Posicao X em funcao do Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Coordenada X (m)")
plt.legend(["Bola","Robo"])

plt.savefig("x_t_robo_bola.png", dpi=300, bbox_inches='tight')
plt.show()
