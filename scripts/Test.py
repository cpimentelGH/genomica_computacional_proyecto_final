
from NoiseFuncs import add_noise, noise_data_gen
from matplotlib.pyplot import imread
import matplotlib.pyplot as plt

# image  = imread('figures/alpha_training/alpha0.png')
# add_noise(image, 0, 'figures/noised', 'test1')
# add_noise(image, 1, 'figures/noised', 'test2')

noise_data_gen('figures/alpha_training', 'figures/noised_test', 50, 0, 'label')
