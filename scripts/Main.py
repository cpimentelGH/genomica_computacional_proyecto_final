from CGRfuncs import data_set_gen
# from Model import BaseVGG
import cv2, pickle

# m = BaseVGG(200,200)
# m.load_data('data/filtered/vanilla_set/train', 'data/filtered/vanilla_set/test')
# m.train(200, 100, 'archive/15_06_20/', 'base_vanilla_1')

# data_set_gen('data/raw_data/to_predict/HCoV-229E.fasta', 'data/filtered/to_predict',
#                'HCoV-229E')

im = cv2.imread('data/filtered/to_predict/HCoV-229E0.png', cv2.IMREAD_GRAYSCALE)
print(im.shape)


predictor = pickle.load(open('archive/15_06_20/base_vanilla_1_model.sav', 'rb'))

print(predictor.predict(im.reshape(1,200,200,1)))
