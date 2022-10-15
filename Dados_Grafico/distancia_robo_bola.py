from cProfile import label
from re import X
import sys
import matplotlib
import tkinter
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

#separar em listas as linhas do excel
dataset = open("distancia_robo_bola.txt", "r")
linhas = dataset.readlines()

ListaLinhas = []
tempo = []
Distancia = []

for i in range(1,len(linhas)):
    ListaLinhas.append(linhas[i].strip("\n").replace(",",".").split("\t"))

for item in ListaLinhas:
    tempo.append(float(item[0]))
    Distancia.append(float(item[1]))

print(tempo)
print(Distancia)

plt.plot(tempo,Distancia)

plt.title("Distancia entre Robo e Bola em funcao do Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Distancia (m)")
plt.show()
