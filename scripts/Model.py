from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import matplotlib.pyplot as plt
import os, sys


class CNNmodel:

    """
    Clase que define la arquitectura de la CNN a utilizar
    y utilidades asociadas
    """

    def __init__(self, img_width, img_height):
            """
            Constructor de la arquitectura de la CNN
            """
            if K.image_data_format() == 'channels_first':
                input_shape = (3, img_width, img_height)
            else:
                input_shape = (img_width, img_height, 3)
            #
            self.model = Sequential()
            self.model.add(Conv2D(32, (3, 3), input_shape=input_shape))
            self.model.add(Activation('relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2)))
            #
            self.model.add(Conv2D(32, (3, 3)))
            self.model.add(Activation('relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2)))
            #
            self.model.add(Conv2D(64, (3, 3)))
            self.model.add(Activation('relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2)))
            #
            self.model.add(Flatten())
            self.model.add(Dense(64))
            self.model.add(Activation('relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(4))
            self.model.add(Activation('softmax'))
            #
            self.model.compile(loss='binary_crossentropy',
                          optimizer='adam',
                          metrics=['accuracy'])
    # end def

    def load_data(self, pathtotrain, pathtotest):
        """
        Genera un DirectoryIterator sobre las muestras de entrenamiento y prueba
        """
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)
        #
        test_datagen = ImageDataGenerator(rescale=1./255)
        #
        self.train_generator = train_datagen.flow_from_directory(
            pathtotrain,
            target_size=(200, 200),
            batch_size=10,
            class_mode='categorical')
        #
        self.validation_generator = test_datagen.flow_from_directory(
            pathtotest,
            target_size=(200, 200),
            batch_size=10,
            class_mode='categorical')
        #
        self.train_samples = sum(len(files) for _, _, files in os.walk(pathtotrain))
        self.test_samples = sum(len(files) for _, _, files in os.walk(pathtotest))
    # end def

    def train(self, epochs, batch_size, savepath, testname):
        """
        Entrena el modelo con las muestras de entrenamiento y prueba cargados
        Además guarda los pesos y la gráfica de presición
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
        self.model.save_weights(savepath + '/' + testname + '.h5')
    # end def

    def graf_entrenamiento(self, historia, archivo):
        """
        Grafica el entrenamiento del modelo
        """
        fig = plt.figure(figsize=(10,10))
        # plot loss
        plt.subplot(211)
        plt.title('Cross Entropy')
        plt.plot(historia.history['loss'], color='blue', label='train')
        plt.plot(historia.history['val_loss'], color='orange', label='test')
        # plot accuracy
        plt.subplot(212)
        plt.title('Accuracy')
        plt.plot(historia.history['accuracy'], color='blue', label='train')
        plt.plot(historia.history['val_accuracy'], color='orange', label='test')
        # save plot to file
        plt.savefig(archivo + '/_plot.png')
        plt.show()
        del(fig)
    # end def

# END CNNmodel
