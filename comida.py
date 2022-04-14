import random
from configuracoes import *

class Comida:
    def __init__(self,quadro):

        x = random.randint(0,LARGURA/TAMANHO_PARTE - 1)*TAMANHO_PARTE
        y = random.randint(0,ALTURA/TAMANHO_PARTE - 1)*TAMANHO_PARTE
        self.coordenadas = [x,y]

        quadro.create_oval(x,y, x+TAMANHO_PARTE,y+TAMANHO_PARTE,fill=COR_COMIDA,tag = 'comida')

