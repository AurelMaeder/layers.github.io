from PIL import Image
import os
import numpy as np
import pandas as pd
import time
import psutil

path_img = '/home/nulpe/Desktop/cultural_data_sculp/img_data/'
path_data = '/home/nulpe/Desktop/cultural_data_sculp/meta_data.csv'

meta_data = pd.read_csv(path_data)
dirList = os.listdir(path_img)
image_list = meta_data.objectID.tolist()
chroma_list = []

for image_id in image_list:
    if str(image_id)+'.jpg' in dirList:
        img = Image.open(path_img+str(image_id)+'.jpg')
        chroma_mean = np.mean(np.asarray(img.convert('LA'))[:,:,0])
        chroma_list.append(chroma_mean)
    else: chroma_list.append(-1)




meta_data['chroma_mean'] = chroma_list

print(meta_data)
meta_data.to_csv(path_data+'meta_data.csv_1')




