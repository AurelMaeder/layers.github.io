import os
import pandas as pd


path_data = '/home/nulpe/Desktop/cultural_data_sculp/meta_data_4.csv'

meta_data = pd.read_csv(path_data)
df_grouped = meta_data.groupby(['style_classification'])['objectID'].agg(['count'])

sorted = df_grouped.sort_values('count', ascending=False)



print(sorted)


style_dic = {'Baroque':0, 'Northern_Renaissance':1, 'Rococo':2, 'Romanticism': 3,
             'Realism':4, 'Neoclassicism':5, 'Early_Renaissance':6,
             'Impressionism':7, 'Post-Impressionism':8, 'Expressionism':7,
             'Mannerism_(Late_Renaissance)':9, 'Surrealism':10, 'Art_Nouveau_(Modern)': 11, 'High_Renaissance':9}

style_cluster = [style_dic[i] if i in style_dic else 12 for i in meta_data['style_classification']]


cluster_name = []
for idx, el in enumerate(style_cluster):
    if el not in [7, 9, 12]:
        cluster_name.append(meta_data['style_classification'][idx])
    elif el == 7:
        cluster_name.append('Impressionism & Expressionism')
    elif el == 9:
        cluster_name.append('Mannerism & High_Renaissance')
    elif el == 12:
        cluster_name.append('Primitivism, Pop_Art & various')







meta_data['style_cluster'] = style_cluster
meta_data['cluster_names'] = cluster_name
#meta_data['cluster_name_check'] = cluster_name


df_grouped = meta_data.groupby(['style_cluster'])['objectID'].agg(['count'])
sorted = df_grouped.sort_values('count', ascending=False)
print(sorted)



image_crop = 'https://res.cloudinary.com/epfl/image/upload/w_500,h_500,c_pad,b_rgb:222222'



meta_data['cropped_cloudinary_url'] = meta_data.cloudnary_url.apply(lambda x: image_crop+x[x.rfind('/v'):-4]+'.png')



meta_data.to_csv('/home/nulpe/Desktop/cultural_data_sculp/meta_data_5.csv', index=False)

#meta_data_5 -->



print(meta_data['objectBeginDate'].max())

print(meta_data['chroma_mean'].min())