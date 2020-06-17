# Clasificación de los géneros de la subfamilia *Coronavirinae* basada en firmas genómicas

## The Powerpuff Team
### Integrante 1: Abasolo Cortés Natalia 🍬
### Integrante 2: Pimentel Ruíz Carlos 🌰
### Integrante 3: Gómez Mora Héctor Eduardo 🔵

### Obtención de datos

Recolección manual de datos de [NCBI](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/) con los siguientes filtros

- Entrenamiento: `taxid`, `genbank`, `complete` de mayor a menor longitud de secuencias

- Validación: `taxid`, `genbank`, `partial` de mayor a menor longitud de secuencias

### Replicación

En el directorio `scripts/` existe un notebook `Main.ipynb` que provee todas las etapas realizadas para replicar las colecciones de imágenes, los entrenamientos y las predicciones.
