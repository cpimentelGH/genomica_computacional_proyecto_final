# Clasificador de firmas genómicas


### Obtención de datos

Recolección manual de datos de [NCBI](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/) con los siguientes filtros

- Entrenamiento: `taxid`, `genbank`, `complete` de mayor a menor longitud de secuencias

- Validación: `taxid`, `genbank`, `partial` de mayor a menor longitud de secuencias

### Modelo(s)

En el archivo `Modelo.py` se encuentra la aquitectura de la CNN utilizada.
Para poder entrenarse debe primero crearse una instancia de la clase, cargar los datasets de entrenamiento y prueba mediante sus paths y ejecutar el método `train()`. Tras finalizar el entrenamiento se genera un directorio dentro de `archive/` que contiene el *archivo de pesos* y la *gráfica de desempeño * correspondiente.
