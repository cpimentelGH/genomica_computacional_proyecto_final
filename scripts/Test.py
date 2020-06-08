from Model import CNNmodel

model = CNNmodel(200,200)

model.load_data('data/filtered/train', 'data/filtered/test')

model.train(10,5,'archive/test2','test2')
