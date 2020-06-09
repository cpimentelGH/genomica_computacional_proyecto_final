from Model import CNNmodel
from CGRfuncs import data_set_gen

m = CNNmodel(200,200)

m.load_data('data/filtered/train', 'data/filtered/test')

m.train(2, 5, 'archive/09062020', 'test1')
