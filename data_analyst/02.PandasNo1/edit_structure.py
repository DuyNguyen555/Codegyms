import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv("01.Overview\data\FoodPrice_in_Turkey.csv")
    print(df.head())
    
    df.rename(columns={'Place':'Địa điểm','ProductName':'Tên SP'}, inplace=True)
    
    df['new_column'] = pd.Series(np.nan, index = df.index)
    df['Giảm giá'] = pd.Series('10%', index=df.index)
    df.insert(10, 'Giảm giá 2', pd.Series('12%', index = df.index))
    df = df.append({'Địa điểm':'NA','ProductId':'RR','Tên SP':'Rice','UmId':10,'UmName':'KG','Month':6,'Year':2021,'Price':84.3785,'Giảm giá':'10%','Giảm giá 2':'12%'}, ignore_index=True)
    
    # print(df.head())
    print(df.tail())
    
    del df['new_column']
    # print(df.head())
    df.pop('Giảm giá 2')
    df.drop("Giảm giá", axis=1, inplace=True)
    df.drop(['Year', 'Price'], axis=1, inplace=True)
    df.drop(1, axis=0, inplace=True)
    df.drop([2,3], axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    print(df.head())