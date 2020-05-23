from CGRfuncs import to_cgr

'''
Clase principal
'''

'''
Para generar una CGR únicamente hay que proporcionar la ruta del archivo
y el nombre de salida
'''

# Genera test1.png en figures/
to_cgr('data/raw_data/bat.fasta', 'test1')

# Genera test2.png en figures/
to_cgr('data/raw_data/sequence.fasta', 'test2')

# Genera test3.png en figures/
to_cgr('data/raw_data/white-eye.fasta', 'test3')


'''
La idea es poner todos los archivos .fasta en data/ y automatizar la generación
de sus CGR
'''
