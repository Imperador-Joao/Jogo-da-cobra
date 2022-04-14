from configuracoes import *


class Cobra:

    def __init__(self,quadro):

        self.tamanho = QTD_PARTES
        self.coordenadas = []
        self.quadrados = []

        for i in range(0,QTD_PARTES):
            self.coordenadas.append([LARGURA//2,ALTURA//2])

        for x,y in self.coordenadas:
            quadrado = quadro.create_rectangle(x,y,x+TAMANHO_PARTE,y+TAMANHO_PARTE,fill = COR_COBRA,tag = 'cobra')
            self.quadrados.append(quadrado)
