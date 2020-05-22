import numpy as np
import matplotlib.pyplot as plt

'''
Modulo para generación de firmas genómicas
'''

def generatePoints(dnaSeq):
    '''
    Dada una secuencia obtiene los puntos mediante las reglas del juego del caos
    '''
    pntStack = [(0.5,0.5)]
    newX, newY = 0, 0
    while len(dnaSeq) != 0:
        nextNt = dnaSeq[0] # se obtiene el siguiente caracter
        dnaSeq = dnaSeq[1:] # se acorta la cadena
        # Obtención de puntos mediante juego del caos
        if nextNt.lower() == 'a':
            newX = (0 + (pntStack[-1])[0]) / 2
            newY = (0 + (pntStack[-1])[1]) / 2
        elif nextNt.lower() == 'c':
            newX = (0 + (pntStack[-1])[0]) / 2
            newY = (1 + (pntStack[-1])[1]) / 2
        elif nextNt.lower() == 't':
            newX = (1 + (pntStack[-1])[0]) / 2
            newY = (1 + (pntStack[-1])[1]) / 2
        elif nextNt.lower() == 'g':
            newX = (1 + (pntStack[-1])[0]) / 2
            newY = (0 + (pntStack[-1])[1]) / 2
        pntStack.append((newX,newY))
    #
    pntStack.pop(0) # se elimina el punto inicial
    return pntStack
# end

def chaos_game_rep(pts, figname):
    '''
    De un conjunto de puntos obtiene su representación gráfica y la guarda en
    el directorio figures
    '''
    x,y = zip(*pts)
    fig = plt.figure(figsize=(7,7))
    plt.scatter(x,y,s=0.1,color='black')
    plt.axis('off')
    plt.tight_layout()
    fig.savefig('figures/'+figname+'.png')
# end
