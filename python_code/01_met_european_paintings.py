import requests
import shutil
import pandas as pd
import json

url_euro = 'https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=11'

path_data = '/home/nulpe/Desktop/cultural_data_sculp/'
path_img = '/home/nulpe/Desktop/cultural_data_sculp/img_data/'


response = requests.get(url_euro)
img_ids = response.json()['objectIDs']

columns = ['objectID', 'primaryImage', 'primaryImageSmall', 'title', 'artistNationality', 'artistBeginDate', 'artistEndDate',  'objectDate', 'objectBeginDate', 'objectEndDate', 'geographyType','city', 'state', 'county', 'country', 'region', 'subregion']
json_data = []



for idx, id in enumerate(img_ids):
    img_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(id)
    response = requests.get(img_url, stream=True).json()
    json_data.append([response[dat] for dat in columns])



    img_low_res = response['primaryImageSmall']
    try:
        response_img = requests.get(img_low_res, stream=True)


        with open(path_img+str(id)+'.jpg', 'wb') as out_file:
            shutil.copyfileobj(response_img.raw, out_file)
    except: pass

    print('on image ', idx+1)



df_meta_data = pd.DataFrame(json_data, columns=columns)
print(df_meta_data)
df_meta_data.to_csv(path_data+'meta_data.csv')
