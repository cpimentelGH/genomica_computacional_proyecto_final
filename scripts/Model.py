from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Convolution2D, AveragePooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from keras import backend as K
import matplotlib.pyplot as plt
import os, sys, pickle

class BaseVGG:

    """
    Clase encargada de definir la arquitectura MiniVGG de tres bloques
    y sus utilidades de entrenamiento
    """

    def __init__(self, img_width, img_height):
        """ Creación de la arquitectura MiniVGG de 3 bloques
        img_width : int
            ancho de las imágenes target
        img_height : int
            altura de las imágenes target
        """
        if K.image_data_format() == 'channels_first':
            inshp = (1, img_width, img_height)
        else:
            inshp = (img_width, img_height, 1)
        # 1er bloque
        self.model = Sequential()
        self.model.add(Convolution2D(32, kernel_size=(3,3), padding="same",
                                     kernel_initializer="he_uniform",
                                     activation='relu', input_shape=inshp))
        self.model.add(Convolution2D(32, kernel_size=(3,3), padding="same",
                                     kernel_initializer="he_uniform",
                                     activation='relu'))
        self.model.add(MaxPooling2D((2,2), strides=(2,2)))
        # 2do bloque
        self.model.add(Convolution2D(64, kernel_size=(3,3), padding="same",
                                     kernel_initializer="he_uniform",
                                     activation='relu'))
        self.model.add(MaxPooling2D((2,2), strides=(2,2)))
        self.model.add(BatchNormalization())
        # 3er bloque
        self.model.add(Convolution2D(128, kernel_size=(3,3), padding="same",
                                     kernel_initializer="he_uniform",
                                     activation='relu'))
        self.model.add(MaxPooling2D((2,2), strides=(2,2)))
        self.model.add(BatchNormalization())
        # Bloque final
        self.model.add(Flatten())
        self.model.add(Dense(128, activation='tanh'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(4, activation='softmax'))
        # Compilar
        opt = Adam(lr=0.0001)
        self.model.compile(loss='categorical_crossentropy',
                      optimizer=opt,
                      metrics=['accuracy'])
    # end def

    def load_data(self, pathtotrain, pathtotest):
        """ Genera un DirectoryIterator sobre las muestras de entrenamiento y prueba
        pathtotrain : str
            ruta del directorio de imágenes de entrenamiento
        pathtotrain : str
            ruta del directorio de imágenes de prueba
        """
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=False)
        #
        test_datagen = ImageDataGenerator(rescale=1./255)
        #
        self.train_generator = train_datagen.flow_from_directory(
            pathtotrain,
            target_size=(200, 200),
            color_mode='grayscale',
            batch_size=10,
            class_mode='categorical')
        #
        self.validation_generator = test_datagen.flow_from_directory(
            pathtotest,
            target_size=(200, 200),
            color_mode='grayscale',
            batch_size=10,
            class_mode='categorical')
        #
        self.train_samples = sum(len(files) for _, _, files in os.walk(pathtotrain))
        self.test_samples = sum(len(files) for _, _, files in os.walk(pathtotest))
    # end def

    def train(self, epochs, batch_size, savepath, testname):
        """ Entrena el modelo, guarda pesos y genera gráfica
        epochs : int
            número de épocas
        batch_size : int
            tamaño del batch
        savepath : str
            ruta donde guardar los pesos y la gráfica generados
        testname : str
            label para identifcar al entrenamiento
        """
        history = self.model.fit_generator(
            self.train_generator,
            steps_per_epoch = self.train_samples // batch_size,
            epochs=epochs,
            validation_data = self.validation_generator,
            validation_steps = self.test_samples // batch_size)
        #
        if not os.path.exists(savepath):
            os.makedirs(savepath)
        self.graf_entrenamiento(history, savepath)
        # Salva los pesos optimizados
        # self.model.save_weights(savepath + '/' + testname + '.h5')
        # Salva el modelo entrenado
        # self.model.model.save('m.h5')
        save_label = '/' + testname + '_model.sav'
        pickle.dump(self.model, open(savepath + save_label, 'wb'))
    # end def

    def graf_entrenamiento(self, historia, archivo):
        """ Grafica el entrenamiento del modelo
        historia :
            un modelo entrenado
        archivo : ruta donde guardar la gráfica
        """
        fig = plt.figure(figsize=(10,10))
        # plot loss
        plt.subplot(211)
        plt.plot(historia.history['loss'], color='blue', label='train')
        plt.plot(historia.history['val_loss'], color='orange', label='test')
        plt.title('Cross Entropy Loss')
        plt.ylabel('loss')
        # plot accuracy
        plt.subplot(212)
        plt.plot(historia.history['accuracy'], color='blue', label='train')
        plt.plot(historia.history['val_accuracy'], color='orange', label='test')
        plt.title('Model Accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        # save plot to file
        plt.savefig(archivo + '/_plot.png')
        plt.show()
        del(fig)
    # end def

    def load_weights(self, filepath):
        """ Carga los pesos dependiendo
        filepath : str
        """
        self.model.load_weights(filepath)
    # end def

# END BaseVGG
