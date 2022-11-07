import os
import shutil

def apagarArquivosAnteriores(path=os.getcwd()):

    try:
        #!Remover os dados caso o programa já tenha sido rodado!
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/acel_robo.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/acel_bola.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/distancia_robo_bola.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_bola.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_robo.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/velocidade_relativa.txt')
        shutil.rmtree(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/Graficos_Raio_Padrao', ignore_errors=True)
    except:
        pass
    
    try:
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/RA_acel_robo.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/RA_acel_bola.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/RA_distancia_robo_bola.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_bola.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_robo.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/RA_x_y_robo_bola.txt')
        os.remove(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/RA_velocidade_relativa.txt')
        shutil.rmtree(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/Graficos_Raio_Alterado', ignore_errors=True)
    except:
        pass
    
    try:
        os.mkdir(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/Graficos_Raio_Padrao')
        os.mkdir(path + '/Dependencias/Dados_Grafico/Gerar_Grafico/Graficos_Raio_Alterado')
    except:
        pass