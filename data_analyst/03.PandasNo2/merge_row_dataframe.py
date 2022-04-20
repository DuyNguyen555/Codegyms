import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('03.PandasNo2\data\FoodPrice_in_Turkey.csv')
    # print(df.head(10))
    df = df.drop_duplicates(['ProductId'], keep = 'last').reset_index(drop=True)
    # print(df.head(10))
    
    df_pro = df.loc[:,['ProductId','ProductName','UmId','UmName']]
    # print(df_pro)
    
    df_pri = df.loc[:,['ProductId','Place','Month','Year','Price']]
    # print(df_pri)
    
    df_pri10 = df.loc[10:20,['ProductId','Place','Month','Year','Price']]
    # print(df_pri10)
    
    # Ghép
    df1 = pd.merge(df_pro, df_pri, on="ProductId")
    # print(df1)
    
    df2 = pd.concat([df_pro, df_pri,df_pri10], axis=1)
    print(df2)