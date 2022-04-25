import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv("03.PandasNo2\data\GDPlist.csv", )
    # print("Số dòng là:", df.shape[0], "\n Số cột là: ", df.shape[1])
    # df_gdp = df.loc[:, "GDP (millions of US$)"]
    # print("Giá trị lớn nhất của GDP: ", df_gdp.max())
    # print("Giá trị nhỏ nhất của GDP: ", df_gdp.min())
    # print("Xu hướng phân bố GDP: ", df_gdp.mode())
    
    # df_chauluc = df.loc[:, 'Continent']
    # print("Châu lục xuất hiện nhiều nhất là:", df_chauluc.mode())
    
    df_sum = df.loc[:, ['Continent', 'GDP (millions of US$)']]
    
    # df_2 = df.groupby(["Country"])['GDP (millions of US$)'].sum()
    # df_3 = df.groupby(["Country"])['GDP (millions of US$)'].mean()
    # print(df_2)
    # df_3 = df.merge(df_2, df_3, on='Country')