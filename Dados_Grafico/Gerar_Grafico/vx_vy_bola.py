from cProfile import label
from re import X
import sys
import matplotlib
import tkinter
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

#separar em listas as linhas do excel
dataset = open("vx_vy_bola.txt", "r")
linhas = dataset.readlines()

ListaLinhas = []
tempo = []
Robo_Vx = []
Robo_Vy = []

for i in range(1,len(linhas)):
    ListaLinhas.append(linhas[i].strip("\n").replace(",",".").split("\t"))

for item in ListaLinhas:
    tempo.append(float(item[0]))
    Robo_Vx.append(float(item[1]))
    Robo_Vy.append(float(item[2]))

print(tempo)
print(Robo_Vx)
print(Robo_Vy)

plt.plot(tempo,Robo_Vx)
plt.plot(tempo,Robo_Vy)

plt.title("Velocidade X e Y da Bola em funcao do Tempo")
plt.xlabel("Tempo")
plt.ylabel("Velocidade X e Y")
plt.legend(["Velocidade X","Velocidade Y"])

plt.savefig("vx_vy_bola.png", dpi=300, bbox_inches='tight')
plt.show()