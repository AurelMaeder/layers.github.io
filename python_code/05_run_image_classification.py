import rasta.python.models
import rasta.python.evaluation
import os
import pandas as pd

model = rasta.python.evaluation.init('/home/nulpe/Desktop/cultural_data_sculp/rasta/models/default/model.h5')


path_img = '/home/nulpe/Desktop/cultural_data_sculp/img_data/'
path_data = '/home/nulpe/Desktop/cultural_data_sculp/meta_data_3.csv'

meta_data = pd.read_csv(path_data)
image_list = meta_data.objectID.tolist()

painting_style = []
painting_classification_certainty = []

for idx, image_name in enumerate(image_list):

    prediction = rasta.python.evaluation.get_pred(model, path_img+str(image_name)+'.jpg')

    painting_style.append(prediction[0][0])
    painting_classification_certainty.append(prediction[1][0])

    print(prediction[0][0])


meta_data['style_classification'] = painting_style
meta_data['style_classification_certainty'] = painting_classification_certainty


meta_data.to_csv('/home/nulpe/Desktop/cultural_data_sculp/meta_data_4.csv', index=False)

print(meta_data['style_classification'] )