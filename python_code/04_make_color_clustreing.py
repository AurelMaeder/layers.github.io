import PIL
from PIL import Image
from matplotlib import pyplot as plt
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import cv2
import numpy as np

def hexencode(rgb):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    return '#%02x%02x%02x' % (r,g,b)


path_img = '/home/nulpe/Desktop/cultural_data_sculp/img_data/'
path_data = '/home/nulpe/Desktop/cultural_data_sculp/meta_data_2.csv'

meta_data = pd.read_csv(path_data)
image_list = meta_data.objectID.tolist()



for idx, image_name in enumerate(image_list):

    img = cv2.imread(path_img+str(image_name)+'.jpg')

    r = cv2.calcHist([img],[0],None,[10],[0,256])
    g = cv2.calcHist([img], [1], None, [10], [0, 256])
    b = cv2.calcHist([img],[2],None,[10],[0,256])
    colors = np.concatenate((r,g,b), axis=0).T


    if idx == 0:color_histograms = colors
    else:color_histograms = np.append(color_histograms, colors, axis=0)


print(color_histograms.shape)


k = 10
clusters = KMeans(6, random_state = 40)
clusters.fit(color_histograms)

print(clusters.labels_[:10])
print(image_list[:10])


meta_data['color_cluster'] = clusters.labels_

meta_data.to_csv('/home/nulpe/Desktop/cultural_data_sculp/meta_data_3.csv', index=False)









