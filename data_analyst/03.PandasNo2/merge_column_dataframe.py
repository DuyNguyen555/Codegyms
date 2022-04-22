import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('03.PandasNo2\data\FoodPrice_in_Turkey.csv')
    df1 = df.loc[:4999, :]
    df2 = df.loc[5000:7380,:]
    df3 = df.loc[1000:2000,['ProductId','Place','Month','Year','Price']]
    df4 = pd.concat([df1,df2], axis=0)
    df5=pd.concat([df1,df2,df3], axis=0)
    df6=df1.append(df2)
    print(df6)