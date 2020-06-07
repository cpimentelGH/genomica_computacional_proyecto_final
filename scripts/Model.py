from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import matplotlib.pyplot as plt

# Sorry prof me volé su función del notebook ==================================
def graf_entrenamiento(historia, archivo):
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
    if not os.path.exists(archivo):
        os.makedirs(archivo)
    plt.savefig(archivo + '_plot.png')
    plt.show()
    del(fig)
#============================================================================

img_width, img_height = 200, 200

train_data_dir = 'data/filtered/train'
validation_data_dir = 'data/filtered/test'
nb_train_samples = 1596
nb_validation_samples = 660
epochs = 10
batch_size = 10


# Construcción del Modelo ===============================
if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(4))
model.add(Activation('softmax'))

model.summary() # Resumen de la arquitectura

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
#=======================================================

# Inicialización de conjuntos de prueba y entrenamiento=
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'data/filtered/train',
    target_size=(200, 200),
    batch_size=10,
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    'data/filtered/test',
    target_size=(200, 200),
    batch_size=10,
    class_mode='categorical')
#=======================================================

# Entrenamiento y evaluación ============================
history = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

graf_entrenamiento(history, 'archive/test1/')
model.save_weights('archive/test1/Test.h5')
#=======================================================
