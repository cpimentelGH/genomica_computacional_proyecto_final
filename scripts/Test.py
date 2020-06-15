from Model import BaseVGG
# import cv2
#
# im = cv2.imread('data/filtered/train/alhpa/alpha0.png')
# print(im.shape)

m = BaseVGG(200,200)
m.load_data('data/filtered/train', 'data/filtered/test')
m.train(1, 100, 'archive/tests/test1', 'test1')
