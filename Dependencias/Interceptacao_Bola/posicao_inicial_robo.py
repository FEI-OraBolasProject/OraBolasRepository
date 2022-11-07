from random import randint
from math import *

def gerar_posicao_inicial(xi_bola,yi_bola):

    xi_max_robo = int((xi_bola + 1) * 100)
    xi_min_robo = int((xi_bola - 1) * 100)

    yi_max_robo = int((yi_bola + 1) * 100)
    yi_min_robo = int((yi_bola - 1) * 100)

    while(True):

        xi_robo = randint(xi_min_robo,xi_max_robo) / 100
        yi_robo = randint(yi_min_robo,yi_max_robo) / 100

        raio = sqrt((xi_robo - xi_bola)**2 + (yi_robo - yi_bola)**2)

        if raio <= 1:
            break
        else:
            continue

    return (xi_robo, yi_robo)