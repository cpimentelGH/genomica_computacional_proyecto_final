'''
Modulo para manejo de archivos fasta
'''

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
