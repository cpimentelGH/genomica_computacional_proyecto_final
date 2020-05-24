import numpy as np
import matplotlib.pyplot as plt
import os, sys

def seq_generator(pathtofasta):
    '''
    Devuelve la concatenación de los reads de un archivo fasta
    '''
    fasta_file = open(pathtofasta)
    final_seq = ''
    for i, read in enumerate(fasta_file):
        if i > 0:
            final_seq += read.rstrip()
    fasta_file.close()
    return final_seq
# end

def generatePoints(dnaSeq):
    '''
    Dada una secuencia de caracteres obtiene los puntos mediante
    las reglas del juego del caos
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

def to_cgr(pathtofasta, figname):
    """
    Obtiene una secuencia de un archivo fasta, obtiene sus puntos y grafica
    su CGR
    """
    pts = generatePoints(seq_generator(pathtofasta))
    #
    x,y = zip(*pts)
    fig = plt.figure(figsize=(7,7))
    plt.scatter(x,y,s=0.1,color='black')
    plt.axis('off')
    plt.tight_layout()
    fig.savefig('figures/'+figname+'.png')
# end

def batch_cgr(opt):
    """
    A partir de la opción dada genera todos las CGR de los archivos
    correspondientes
    0 -> betacoronavirus
    1 -> alphacoronavirus
    2 -> gammacoronavirus
    3 -> deltacoronavirus
    """
    opts = {0: ('data/raw_data/beta/.', 'beta'),
    1: ('data/raw_data/alpha/.', 'alpha'),
    2: ('data/raw_data/gamma/.', 'gamma'),
    3: ('data/raw_data/delta/.', 'delta')}
    #
    current_path = (opts[opt])[0]
    current_label = (opts[opt])[1]
    i = 0
    for file in os.listdir(current_path):
        current_file = os.path.join(current_path, file)
        if os.path.isfile(current_file):
            label = current_label+str(i)
            i+=1
            to_cgr(current_file, label)
# end
