import requests
import shutil
import pandas as pd
import json
import cloudinary
import cloudinary.api
from PIL import Image
# private cloudinary keys
#######################################################################################################################
cloud_name = ''
API_key = ''
API_key_secret = ''
environmetal_variable = ''
sample_url = ''
#######################################################################################################################
path_data = '/home/nulpe/Desktop/cultural_data_sculp/'

cloudinary.config(cloud_name=cloud_name, api_key=API_key,api_secret=API_key_secret)
resources = cloudinary.api.resources(type='upload', max_results=5)


data = []
cursor = None
while True:
    resources = cloudinary.api.resources(type='upload', max_results=500, next_cursor=cursor)

    for el in resources['resources']:
        data.append([el['public_id'], el['url']])

    if 'next_cursor' in resources:
        cursor = resources['next_cursor']
        print(len(resources['resources']))
        print(resources['next_cursor'])

    else:
        break

df_cloudinary = pd.DataFrame(data, columns=['public_id', 'cloudnary_url'])
df_cloudinary['met_id'] = [el[:6] for el in df_cloudinary.public_id.tolist()]
print(df_cloudinary)
print(len(df_cloudinary))
df_cloudinary.to_csv(path_data+'cloudinary_data.csv')

#merge cloudinary paths to data frame
meta_data_1 = pd.read_csv(path_data+'meta_data_1.csv')
df_cloudinary = pd.read_csv(path_data+'cloudinary_data.csv')
print(len(meta_data_1))
print(len(df_cloudinary))
print()

meta_data_1 = meta_data_1.merge(df_cloudinary, left_on='objectID', right_on='met_id')
meta_data_1.to_csv(path_data+'meta_data_2.csv')
