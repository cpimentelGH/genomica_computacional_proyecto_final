# Clasificador de firmas genómicas


### Obtención de datos

Recolección manual de datos de [NCBI](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/) con los siguientes filtros

- Entrenamiento: `taxid`, `genbank`, `complete` de mayor a menor longitud de secuencias

- Validación: `taxid`, `genbank`, `partial` de mayor a menor longitud de secuencias


