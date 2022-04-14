from tkinter import *
from comida import *
from cobra import *
import random as rd

RODANDO = True
GAME_OVER = False

def novo_jogo():

    global RODANDO,GAME_OVER,cobra,comida,direcao,pontuacao,legenda,bota2

    if not RODANDO:

        GAME_OVER = False
        quadro.delete(ALL)

        cobra = Cobra(quadro)
        comida = Comida(quadro)
        direcao = rd.choice(DIRECOES)
        pontuacao = 0
        legenda.config(text =f'Pontuação: {pontuacao}')
        bota2.config(text = 'Pause',command=pausar)

        RODANDO = True
        janela.after(VELOCIDADE, proxima_vez, cobra, comida)

    return

def proxima_vez(cobra,comida):

    if RODANDO:
        x,y = cobra.coordenadas[0]

        if direcao == 'cima':
            y-= TAMANHO_PARTE
        elif direcao == 'baixo':
            y+= TAMANHO_PARTE
        elif direcao == 'esquerda':
            x-= TAMANHO_PARTE
        elif direcao == 'direita':
            x+= TAMANHO_PARTE

        cobra.coordenadas.insert(0,(x,y))

        quadrado = quadro.create_rectangle(x,y,x+TAMANHO_PARTE,y+TAMANHO_PARTE,fill=COR_COBRA)

        cobra.quadrados.insert(0,quadrado)


        if x == comida.coordenadas[0] and y == comida.coordenadas[1]:

            global pontuacao

            pontuacao += 1

            legenda.config(text = f'Pontuação: {pontuacao}')

            quadro.delete('comida')

            comida = Comida(quadro)
        else:

            del cobra.coordenadas[-1]
            quadro.delete(cobra.quadrados[-1])
            del cobra.quadrados[-1]

        if verificar_colisoes(cobra):
            game_over()
            return

        janela.after(VELOCIDADE,proxima_vez,cobra,comida)

    return

def mudar_direcao(nova_direcao):


    global direcao


    if nova_direcao == 'esquerda':
        if direcao != 'direita':
            direcao = nova_direcao
    elif nova_direcao == 'direita':
        if direcao != 'esquerda':
            direcao = nova_direcao
    elif nova_direcao == 'cima':
        if direcao != 'baixo':
            direcao = nova_direcao
    elif nova_direcao == 'baixo':
        if direcao != 'cima':
            direcao = nova_direcao

    return

def verificar_colisoes(cobra):

    x,y = cobra.coordenadas[0]       # Cabeça da cobra (lespa)

    if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
        return True

    for parte in cobra.coordenadas[1:]:
        if x == parte[0] and y == parte[1]:
            return True

    return False

def pausar():

    global RODANDO,bota2,GAME_OVER

    if not GAME_OVER:

        RODANDO = False

        bota2.config(text = 'Retomar',command=retomar)
        return
def retomar():

    global RODANDO,bota2,comida,quadro,janela

    RODANDO = True

    bota2.config(text='Pausar', command=pausar)
    quadro.delete(comida)
    comida = Comida(quadro)
    janela.after(VELOCIDADE,proxima_vez,cobra,comida)
    janela.update()

    return
def game_over():

    global RODANDO,GAME_OVER

    quadro.create_text(quadro.winfo_width()/2,quadro.winfo_height()/2,
                       font = ('Comic Sans',70),text = 'GAME OVER',fill='red',tag='game over')
    RODANDO = False
    GAME_OVER = True

    return

janela = Tk()
janela.config(bg = FUNDO)
janela.title('Jogo da cobra')

icone = PhotoImage(file = 'Fótons/Cobra.png')
janela.iconphoto(True,icone)

pontuacao = 0
direcao = rd.choice(DIRECOES)

legenda = Label(janela,text= 'Pontuação: {}'.format(pontuacao),font = ('consolas',33),
                bg = FUNDO,fg = 'white')
legenda.pack()

quadro = Canvas(janela,bg = FUNDO,height= ALTURA,width= LARGURA)
quadro.pack()

versao = Label(janela,text = 'v. Alpha 1.1.0',font = ('Comic Sans',10),fg = 'white'
               ,bg = FUNDO)
versao.place(x=LARGURA-145,y = 38)

autor = Label(janela,text = '© Lobato J.F.C \n a.k.a Imperador João',font = ('Comic Sans',13),fg = 'white'
               ,bg = FUNDO)
autor.place(x = LARGURA-175,y=0)

janela.update()

largura_janela = janela.winfo_width()
altura_janela = janela.winfo_height()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

margem_x = int((largura_tela-largura_janela)/2)
margem_y = int((altura_tela-altura_janela)/2)

janela.geometry(f'{largura_janela}x{altura_janela}+{margem_x}+{margem_y}')



bota1 = Button(janela,command=novo_jogo,
       text = 'Novo Jogo',font = ('Comic Sans',13),fg = COR_COBRA,bg = FUNDO)
bota1.place(x=LARGURA/20,y=0)

bota2 = Button(janela,command=pausar,
       text = 'Pausar',font = ('Comic Sans',13),fg = COR_COBRA,bg = FUNDO)
bota2.place(x=LARGURA/20,y=33)


janela.bind('<Left>', lambda evento: mudar_direcao(DIRECOES[0]))
janela.bind('<Right>', lambda evento: mudar_direcao(DIRECOES[1]))
janela.bind('<Up>', lambda evento: mudar_direcao(DIRECOES[2]))
janela.bind('<Down>', lambda evento: mudar_direcao(DIRECOES[3]))


cobra = Cobra(quadro)
comida = Comida(quadro)

proxima_vez(cobra,comida)

janela.mainloop()