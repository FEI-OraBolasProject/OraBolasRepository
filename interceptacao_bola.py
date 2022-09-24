import time


#Função que recebe os dados da trajetoria da bola e exibe na tela
def interceptacao_bola(t,x,y):
    print("%s" %(t))
    print("%s" %(x))
    print("%s" %(y))
    print( )




#Leitura de dados do arquivo trajetoria_bola.txt
traj_bola = open("traj_teste.txt", "r")#
dados = traj_bola.readlines()#faz a leitura das linhas presentes no arquivo

matriz_traj = [] #matriz_pedidos (os dados seram organizados dentro dela )
for i in range(len(dados)):
        palavra = dados[i].strip('\n')#remove a quebra de linha presentes na linha do arquivo
        palavra = palavra.split("\t")#seleciona os dados separados por "\t"
        matriz_traj.append(palavra)#insere os dados separados dentro da "matriz_traj"
#print(matriz_traj)

# Indice por lista : [0][0] = t/s, [0][1] = x/m, [0][2] = y/m 
#Exibe os dados presentes na "matriz_traj" :" : 
for linha in range(len(matriz_traj)):
        
    tempo = matriz_traj[linha][0]
    x = matriz_traj[linha][1]
    y = matriz_traj[linha][2] 
    interceptacao_bola(tempo,x,y)
    
    time.sleep(2)# leitura dos dados a cada 2 segundos
print("Fim do programa")
traj_bola.close()#fecha o arquivo