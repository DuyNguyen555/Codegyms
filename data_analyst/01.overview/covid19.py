import pandas as pd

data = pd.read_csv('subset-covid-data.csv', encoding = 'utf-8')

# print(data.head(1))

# data.info()
shape_info = data.shape
print(shape_info[0])