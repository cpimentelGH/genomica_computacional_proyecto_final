from matplotlib.pyplot import imread
import sys, os, cv2, random

def add_noise(image, noisetype, outpath, label):
    """
    Función que genera ruido en una imágen a través de filtros
    image : imagen a procesar
    noisetype : tipo de ruido deseado (0) mean filter (1) gaussian filter
    outpath : ruta en donde guardar la imagen generada
    label : etiqueta para la imagen
    """
    figure_size = 9
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if noisetype == 0:
        image = cv2.blur(image, (figure_size, figure_size))
    elif noisetype == 1:
        image = cv2.GaussianBlur(image, (figure_size, figure_size), 0)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    image = cv2.convertScaleAbs(image, alpha=(255.0))
    cv2.imwrite(outpath+"/"+label+".png", image)
# end def

def noise_data_gen(pathtoimgs, outpath, size, seed, glabel):
    """
    Dado un directorio de imágenes genera versiones ruidosas aleatoriamente
    pathtoimgs : directorio de imágenes
    outpath : directorio donde depositar las imágenes ruidosas
    size : número de imágenes ruidosas a generar
    seed : semilla para los números aleatorios
    glabel : etiqueta global para los archivos
    """
    random.seed(a=seed)
    for i in range(size):
        rndim = pathtoimgs + '/' + random.choice(os.listdir(pathtoimgs))
        image = imread(rndim)
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        label = glabel + str(i)
        add_noise(image, random.randint(0,1), outpath, label)
# end def

if __name__ == "__main__":

    # noise_data_gen('data/filtered/train/delta', 'data/filtered/train/delta',
    #                 62, 0, 'delta_noise')

    # noise_data_gen('data/filtered/train/alpha', 'data/filtered/train/alpha',
    #                 100, 0, 'alpha_noise')

    # noise_data_gen('data/filtered/train/beta', 'data/filtered/train/beta',
    #                 100, 0, 'beta_noise')

    noise_data_gen('data/filtered/train/delta', 'data/filtered/train/delta',
                    100, 0, 'delta_noise2')

    # noise_data_gen('data/filtered/train/delta', 'data/filtered/train/delta',
    #                 10, 0, 'delta_noise4')

    # noise_data_gen('data/filtered/train/gamma', 'data/filtered/train/gamma',
    #                 100, 0, 'gamma_noise')

    # Añadir ruido al conjunto de prueba

    # noise_data_gen('data/filtered/test/alpha', 'data/filtered/test/alpha',
    #                 50, 0, 'alpha_noise')

    # noise_data_gen('data/filtered/test/beta', 'data/filtered/test/beta',
    #                 50, 0, 'beta_noise')

    # noise_data_gen('data/filtered/test/delta', 'data/filtered/test/delta',
    #                 50, 0, 'delta_noise')

    # noise_data_gen('data/filtered/test/gamma', 'data/filtered/test/gamma',
    #                 50, 0, 'gamma_noise')
