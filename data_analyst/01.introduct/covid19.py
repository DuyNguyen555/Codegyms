import pandas as pd

data = pd.read_csv('subset-covid-data.csv', encoding = 'utf-8')

print(data.head(20))