# Clasificador de firmas genómicas


### Replicación de la Ejecución

Existen algunos archivos `.fasta` de prueba en el directorio `data/raw_data/beta` y `data/raw_data/alpha` para betacoronavirus y alphacoronavirus respectivamente.

Para generar las CGR's de todos los archivos de uno de estos directorios deberá de ejecutarse `python scripts/Test.py` desde el directorio base. Este último script genera por defecto la CGR de betacoronavirus mediante la línea `batch_cgr('data/raw_data/beta/','figures/beta/', 'beta')`. Para generar los datos de alphacoronavirus deberán de cambiarse las rutas de entrada y salida correspondientes y agregar una etiqueta para los `.png` generados. Más información sobre el método `batch_cgr(...)` en el script `CGRfuncs.py`.
