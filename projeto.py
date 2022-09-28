from cProfile import label
from re import X
import sys
import matplotlib
import tkinter
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

#separar em listas as linhas do excel
dataset = open("Pasta1.txt", "r")
linhas = dataset.readlines()

ListaLinhas = []
tempo = []
coordX = []
coordY = []

for i in range(1,len(linhas)):
    ListaLinhas.append(linhas[i].strip("\n").replace(",",".").split("\t"))

for item in ListaLinhas:
    tempo.append(float(item[0]))
    coordX.append(float(item[1]))
    coordY.append(float(item[2]))

print(tempo)
print(coordX)
print(coordY)

plt.plot(coordY,coordX)
#plt.plot(tempo,coordX)

plt.title("Gráfico")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.show()

