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
Robo_coordX = []
Robo_coordY = []
Bola_coordX = []
Bola_coordY = []


for i in range(1,len(linhas)):
    ListaLinhas.append(linhas[i].strip("\n").replace(",",".").split("\t"))

for item in ListaLinhas:
    tempo.append(float(item[0]))
    Robo_coordX.append(float(item[1]))
    Robo_coordY.append(float(item[2]))
    Bola_coordX.append(float(item[3]))
    Bola_coordY.append(float(item[4]))

print(tempo)
print(Bola_coordX)
print(Bola_coordY)
print(Robo_coordX)
print(Robo_coordY)

plt.plot(Bola_coordX,Bola_coordY)
plt.plot(Robo_coordX,Robo_coordY)
#plt.plot(tempo,coordX)

plt.title("Posicao X em funcao de Y")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.show()

#for para limitar o campo com o posicionamento do robô positivo.