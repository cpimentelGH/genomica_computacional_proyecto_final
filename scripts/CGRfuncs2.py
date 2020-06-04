import numpy as np
import matplotlib.pyplot as plt
import os, sys
from CGRfuncs import generatePoints, to_cgr


def complexPointGen(pathtofasta):
    """
    De un fasta con varios genomes juntos se calculan sus puntos
    """
    fasta_file = open(pathtofasta)
    point_set = []
    tmp_seq = ''
    for i, read in enumerate(fasta_file):
        if read[:1] != '>':
            tmp_seq += read.strip()
        else:
            point_set.append(generatePoints(tmp_seq))
            tmp_seq = []
    point_set.pop(0)
    return point_set
# end


def complexCGRGen(pathtofasta, outpath, figname):
    if not os.path.exists(pathtofasta):
        print(pathtofasta + " doesn't exists!!")
        return 0
    pts = foo(pathtofasta)
    #
    i=0
    for pl in pts:
        x,y = zip(*pl)
        fig = plt.figure(figsize=(2,2))
        plt.scatter(x,y,s=0.01,color='black')
        plt.axis('off')
        plt.tight_layout()
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        fig.savefig(outpath + '/' + figname + str(i) + '.png')
        i += 1
        plt.close()
    return 1
# end
