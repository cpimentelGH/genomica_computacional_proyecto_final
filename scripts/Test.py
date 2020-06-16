# from Model import BaseVGG
import cv2
import pickle
#
im = cv2.imread('figures/alpha_training/alpha0.png', cv2.IMREAD_GRAYSCALE)
print(im.shape)

# import PIL
# from PIL import Image
# import numpy as np

# im = Image.open('figures/alpha_training/alpha0.png')
# a = im.resize((200,200), Image.ANTIALIAS)
#
# arrimg = np.array(a)
# arrimg.reshape(1,200,200,4)
# print(arrimg.shape)

# m = BaseVGG(200,200)
# m.load_data('data/filtered/train', 'data/filtered/test')
# m.train(1, 100, 'archive/tests/test1', 'test1')

loaded_model = pickle.load(open('archive/tests/test1test1_model.sav', 'rb'))

print(loaded_model.predict(im.reshape(1,200,200,1)))
