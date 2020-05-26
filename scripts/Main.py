from CGRfuncs import to_cgr, batch_cgr

"""
Clase principal
"""

"""
Para generar una CGR únicamente hay que proporcionar la ruta del archivo
y el nombre de salida
"""

# Genera test1.png en figures/
# Ej.
# to_cgr('data/raw_data/beta/sequences.fasta', 'test1')

"""
Ahora se puede obtener el cgr de todos los .fasta de un directorio con los
parámetros correspondientes
0 -> betacoronavirus # Probado
1 -> alphacoronavirus
2 -> gammacoronavirus
3 -> deltacoronavirus
"""
# batch_cgr(0)
batch_cgr(1) # aún no hay data
# batch_cgr(2) # aún no hay data
# batch_cgr(3) # aún no hay data
