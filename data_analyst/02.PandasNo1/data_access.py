import pandas as pd

if __name__ == '__main__':
    df=pd.read_csv('02.PandasNo1\data\FoodPrice_in_Turkey.csv')
    print(df.head())
    
    # temp = df.iloc[3]
    # temp = df.iloc[3:8]
    # temp = df.iloc[[3,5,7]]
    # temp = df.iloc[:,4]
    # temp = df.iloc[:,3:8]
    # temp = df.iloc[3,7]
    # temp = df.iloc[3:5, 5:7]
    # temp = df.loc[3]
    # temp = df.loc[:, ['UmName','Month']]
    # temp = df.loc[3,'Price']
    temp = df.loc[df.Year >= 2019]
    print(temp)
    
    df.replace(5, 10, inplace=True)
    df.replace(52, 'RR', inplace=True)
    df['Month'].replace(10, 5, inplace=True)
    print(df.head())