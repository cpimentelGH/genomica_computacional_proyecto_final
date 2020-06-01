import numpy as np
import matplotlib.pyplot as plt
import os, sys

def seq_generator(pathtofasta):
    """
    Devuelve la concatenación de los reads de un archivo fasta
    """
    fasta_file = open(pathtofasta)
    final_seq = ''
    for i, read in enumerate(fasta_file):
        if i > 0:
            final_seq += read.rstrip()
    fasta_file.close()
    return final_seq
# end

def generatePoints(dnaSeq):
    """
    Dada una secuencia de caracteres obtiene los puntos mediante
    las reglas del juego del caos
    """
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

def to_cgr(fastapath, outpath, figname):
    """
    Obtiene una secuencia de un archivo fasta, obtiene sus puntos y grafica
    su CGR
    """
    pts = generatePoints(seq_generator(fastapath))
    #
    x,y = zip(*pts)
    fig = plt.figure(figsize=(2,2))
    plt.scatter(x,y,s=0.01,color='black')
    plt.axis('off')
    plt.tight_layout()
    fig.savefig(outpath + '/' + figname + '.png')
    plt.close()
# end

def batch_cgr(fastadir, outdir, label):
    """
    Genera la CGR para varios archivos vertidos en un directorio
    """
    if not os.path.exists(fastadir) or len(os.listdir(fastadir)) == 0:
        sys.exit("No data, for " + fastadir )
    else:
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        i = 0
        for file in os.listdir(fastadir):
            current_file = os.path.join(fastadir, file)
            if os.path.isfile(current_file):
                to_cgr(current_file, outdir, label+str(i))
                i+=1
# end
