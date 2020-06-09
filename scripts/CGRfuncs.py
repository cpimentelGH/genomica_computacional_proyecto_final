import numpy as np
import matplotlib.pyplot as plt
import os, sys

def seq_generator(pathtofasta):
    """
    Devuelve la concatenación de los reads de un archivo fasta
    """
    fasta_file = open(pathtofasta)
    final_seq = ''
    for read in fasta_file:
        if read[:1] != '>':
            final_seq += read.rstrip()
    fasta_file.close()
    return final_seq
# end

def points_gen(dnaSeq):
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

def cgr_plot(pts, outpath, figname):
    """
    De un lista de puntos generados por las reglas del juego del caos se
    grafican en su correspondiente CGR
    """
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
# end def

def train_set_gen(pathtofasta, outpath, classlabel):
    """
    De un fasta con varios genomas juntos se calculan sus puntos y se almacenan
    sus CGR's
    """
    if not os.path.exists(pathtofasta):
        print(pathtofasta + " doesn't exists!!")
        return 0
    fasta_file = open(pathtofasta)
    # Etapa de generación de puntos por juego del caos
    point_set = []
    tmp_seq = ''
    for read in fasta_file:
        if read[:1] != '>':
            tmp_seq += read.strip()
        else:
            point_set.append(points_gen(tmp_seq))
            tmp_seq = []
    point_set.append(points_gen(tmp_seq)) # The last genome in tmp_seq
    point_set.pop(0)
    # Etapa de graficación en CGR
    i=0
    for ps in point_set:
        x,y = zip(*ps)
        fig = plt.figure(figsize=(2,2))
        plt.scatter(x,y,s=0.01,color='black')
        plt.axis('off')
        plt.tight_layout()
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        fig.savefig(outpath + '/' + classlabel + str(i) + '.png')
        i += 1
        plt.close()
    print("Train set created!")
    return 1
# end def
