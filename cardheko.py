# -*- coding: utf-8 -*-
"""cardheko.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aDnboDhNEtjn9J0jNBg0cvpCewRQFt5e
"""

import pandas as pd
from matplotlib import pyplot as plt

import pandas as pd

# Specify the engine parameter explicitly
data = pd.read_excel('/content/chennai_cars (1).xlsx')

# Now try to read the Excel file

data.shape #rows,columns

data.head()

data.new_car_detail[0]

# package to convert string to dictionary
import numpy as np
import ast
ast.literal_eval(data.new_car_detail[0])['ft']

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['ft'])

    continue

data["fuel type"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['bt'])

    continue

data["Body type"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['km'])

    continue

data["Kilometers driven"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['transmission'])

    continue

data["Transmission type"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['ownerNo'])

    continue

data["Number of previous owners"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['owner'])

    continue

data["Ownership details"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['oem'])

    continue

data["Original Equipment Manufacturer"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['model'])

    continue

data["Car model"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['modelYear'])

    continue

data["Year of car manufacture"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['centralVariantId'])

    continue

data["Central variant ID"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['variantName'])

    continue

data["Variant name"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['price'])

    continue

data["Price of the used car"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['priceActual'])

    continue

data["Actual price"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['priceSaving'])

    continue

data["Price saving "]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['priceFixedText'])

    continue

data["Fixed price details"]=collection_name  #create a new column

collection_name=[]
for i in data['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['trendingText'])

    continue

data["Trending car information"]=collection_name  #create a new column

data = data.drop(columns = ['new_car_detail'])

data

data = data.drop(columns = ['new_car_overview','new_car_feature','new_car_specs'])

data = data.drop(columns = ['car_links'])

data = data.drop(columns = ['Trending car information'])

data['Location'] = 'chennai'

data

d1=pd.read_excel("/content/hyderabad_cars.xlsx")#read the file

d1.shape #rows,columns

d1.head()

d1.new_car_detail[0]

collection_name=[]
for i in d1['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['ft'])

    continue

d1["fuel type"]=collection_name  #create a new column

import ast
import pandas as pd

# Assuming 'data' is your DataFrame

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('transmission'))

d1["Transmission type"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('bt'))

d1["Body type"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('km'))

d1["Kilometers driven"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('ownerNo'))

d1["Number of previous owners"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('owner'))

d1["Ownership details"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('oem'))

d1["Original Equipment Manufacturer"] = collection_name


collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('model'))

d1["Car model"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('modelYear'))

d1["Year of car manufacture"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('centralVariantId'))

d1[" Central variant ID"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('variantName'))

d1["Variant name"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('price'))

d1["Price of the used car"] = collection_name


collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceActual'))

d1["Actual price"] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceSaving'))

d1["Price saving "] = collection_name

collection_name = []
for i in d1['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceFixedText'))

d1["Fixed price details"] = collection_name

d1 = d1.drop(columns = ['new_car_overview','new_car_feature','new_car_specs'])

d1 = d1.drop(columns = ['car_links'])

d1 = d1.drop(columns = ['new_car_detail'])

d1['Location'] = 'Hyderabad'

d1

"""**concat**"""

#import pandas as pd

# Assuming 'data' and 'd1' are your DataFrames

# Concatenate vertically (along rows)
#concatenated_table = pd.concat([data, d1], ignore_index=True)

# concatenated_table now contains both data from 'data' and 'd1' stacked vertically.

d2=pd.read_excel("/content/delhi_cars.xlsx")#read the file

d2.shape #rows,columns

import ast
import pandas as pd

# Assuming 'data' is your DataFrame
collection_name=[]
for i in d2['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['ft'])

d2["fuel type"]=collection_name  #create a new column

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('transmission'))

d2["Transmission type"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('bt'))

d2["Body type"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('km'))

d2["Kilometers driven"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('ownerNo'))

d2["Number of previous owners"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('owner'))

d2["Ownership details"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('oem'))

d2["Original Equipment Manufacturer"] = collection_name


collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('model'))

d2["Car model"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('modelYear'))

d2["Year of car manufacture"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('centralVariantId'))

d2[" Central variant ID"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('variantName'))

d2["Variant name"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('price'))

d2["Price of the used car"] = collection_name


collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceActual'))

d2["Actual price"] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceSaving'))

d2["Price saving "] = collection_name

collection_name = []
for i in d2['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceFixedText'))

d2["Fixed price details"] = collection_name

d2 = d2.drop(columns = ['new_car_overview','new_car_feature','new_car_specs'])

d2 = d2.drop(columns = ['car_links'])

d2 = d2.drop(columns = ['new_car_detail'])

d2['Location'] = 'Delhi'

d2

d3=pd.read_excel("/content/jaipur_cars.xlsx")#read the file
d3.shape #rows,columns

import ast
import pandas as pd

# Assuming 'data' is your DataFrame
collection_name=[]
for i in d3['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['ft'])

d3["fuel type"]=collection_name  #create a new column

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('transmission'))

d3["Transmission type"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('bt'))

d3["Body type"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('km'))

d3["Kilometers driven"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('ownerNo'))

d3["Number of previous owners"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('owner'))

d3["Ownership details"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('oem'))

d3["Original Equipment Manufacturer"] = collection_name


collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('model'))

d3["Car model"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('modelYear'))

d3["Year of car manufacture"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('centralVariantId'))

d3[" Central variant ID"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('variantName'))

d3["Variant name"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('price'))

d3["Price of the used car"] = collection_name


collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceActual'))

d3["Actual price"] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceSaving'))

d3["Price saving "] = collection_name

collection_name = []
for i in d3['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceFixedText'))

d3["Fixed price details"] = collection_name

d3 = d3.drop(columns = ['new_car_overview','new_car_feature','new_car_specs'])
d3 = d3.drop(columns = ['car_links'])
d3 = d3.drop(columns = ['new_car_detail'])
d3['Location'] = 'Jaipur'

d3

d4=pd.read_excel("/content/kolkata_cars.xlsx")#read the file
d4.shape #rows,columns

import ast
import pandas as pd

# Assuming 'data' is your DataFrame
collection_name=[]
for i in d4['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['ft'])

d4["fuel type"]=collection_name  #create a new column

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('transmission'))

d4["Transmission type"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('bt'))

d4["Body type"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('km'))

d4["Kilometers driven"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('ownerNo'))

d4["Number of previous owners"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('owner'))

d4["Ownership details"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('oem'))

d4["Original Equipment Manufacturer"] = collection_name


collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('model'))

d4["Car model"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('modelYear'))

d4["Year of car manufacture"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('centralVariantId'))

d4[" Central variant ID"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('variantName'))

d4["Variant name"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('price'))

d4["Price of the used car"] = collection_name


collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceActual'))

d4["Actual price"] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceSaving'))

d4["Price saving "] = collection_name

collection_name = []
for i in d4['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceFixedText'))

d4["Fixed price details"] = collection_name

d4 = d4.drop(columns = ['new_car_overview','new_car_feature','new_car_specs'])
d4 = d4.drop(columns = ['car_links'])
d4 = d4.drop(columns = ['new_car_detail'])
d4['Location'] = 'Kolkata'

d4

d5=pd.read_excel("/content/bangalore_cars.xlsx")#read the file
d5.shape #rows,columns

import ast
import pandas as pd

# Assuming 'data' is your DataFrame
collection_name=[]
for i in d5['new_car_detail'].values:
  if i == i:
    collection_name.append(ast.literal_eval(i)['ft'])

d5["fuel type"]=collection_name  #create a new column

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('transmission'))

d5["Transmission type"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('bt'))

d5["Body type"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('km'))

d5["Kilometers driven"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('ownerNo'))

d5["Number of previous owners"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('owner'))

d5["Ownership details"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('oem'))

d5["Original Equipment Manufacturer"] = collection_name


collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('model'))

d5["Car model"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('modelYear'))

d5["Year of car manufacture"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('centralVariantId'))

d5[" Central variant ID"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('variantName'))

d5["Variant name"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('price'))

d5["Price of the used car"] = collection_name


collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceActual'))

d5["Actual price"] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceSaving'))

d5["Price saving "] = collection_name

collection_name = []
for i in d5['new_car_detail'].values:
    if i == i:
        collection_name.append(ast.literal_eval(i).get('priceFixedText'))

d5["Fixed price details"] = collection_name

d5 = d5.drop(columns = ['new_car_overview','new_car_feature','new_car_specs'])
d5 = d5.drop(columns = ['car_links'])
d5 = d5.drop(columns = ['new_car_detail'])
d5['Location'] = 'Bangalore'

d5

import pandas as pd

# Assuming 'data' and 'd1' are your DataFrames

# Concatenate vertically (along rows)
cardekho = pd.concat([data, d1,d2,d3,d4,d5], ignore_index=True)

# concatenated_table now contains both data from 'data' and 'd1' stacked vertically.

cardekho

cardekho.info()

# Remove commas from values in the "Kilometers driven" column and then convert to int64
cardekho['Kilometers driven'] = cardekho['Kilometers driven'].str.replace(',', '').astype('int64')

cardekho['Year of car manufacture'] = pd.to_datetime(cardekho['Year of car manufacture'], format='%Y')

# Assuming 'cardekho' is your DataFrame

# Drop the last column using iloc
cardekho = cardekho.iloc[:, :-1]

# Display the DataFrame
print(cardekho)

cardekho

cardekho.isnull().sum()

# Assuming 'cardekho' is your DataFrame

# Drop the column named "fixed price"
cardekho = cardekho.drop(columns=['Fixed price details'])

mean_central_variant_id = cardekho['Central variant ID'].mean()

# Fill NaN values in the "Central variant ID" column with the mean
cardekho['Central variant ID'].fillna(mean_central_variant_id, inplace=True)

cardekho.isnull().sum()

cardekho.drop_duplicates()

final_df = cardekho.copy()            # Creating copy of created dataframe
#droping unnecessary features

final_df.head()

# Assuming 'cardekho' is your DataFrame

# Create a new variable 'Current_Year'
cardekho['Current_Year'] = pd.Timestamp('2024-01-01')

# Convert 'Year of car manufacture' to datetime if it's not already
cardekho['Year of car manufacture'] = pd.to_datetime(cardekho['Year of car manufacture'], format='%Y')

# Calculate how old the car is and create a new feature "No_of_Years"
cardekho['No_of_Years'] = cardekho['Current_Year'].dt.year - cardekho['Year of car manufacture'].dt.year

final_df = cardekho.copy()            # Creating copy of created dataframe
         #droping unnecessary features

final_df.head()

import seaborn as sns
sns.pairplot(data= final_df, hue= 'fuel type', diag_kind= 'kde')

cat_col = list(final_df.columns[3:7])

fig = plt.figure(figsize= (16,16))
plt.suptitle('Categorical features value counts', fontsize = 24)
k=0
for i in range(1,5):
    ax = fig.add_subplot(2,2,i)
    cat_order = final_df[cat_col[k]].value_counts()
    sns.countplot(data = final_df, x = cat_col[k], order = cat_order.index, ax= ax)
    plt.xlabel(cat_col[k], fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.title('{} Value Counts'.format(cat_col[k]), fontsize=18)

    for j in range(cat_order.shape[0]):
        count = cat_order[j]
        strt='{}'.format(count)
        plt.text(j,count+0.1,strt,ha='center', fontsize=16)
    k=k+1

plt.figure(figsize=(10,8))
sns.countplot(data= final_df, x= 'No_of_Years')
plt.xlabel('Number of Years', fontsize=14)
plt.ylabel('Counts', fontsize=14)
plt.title('Number of Years Value Counts', fontsize=18)

final_df = pd.get_dummies(final_df, drop_first=True)
final_df.head()

plt.figure(figsize=(12,10))
sns.heatmap(data = final_df.corr(), annot= True, cmap= 'plasma', vmin= -1 , vmax= 1, linecolor='white', linewidths=2)

