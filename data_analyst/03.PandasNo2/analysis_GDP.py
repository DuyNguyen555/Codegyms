import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv("03.PandasNo2\data\GDPlist.csv", )
    print("Số dòng là:", df.shape[0], "\n Số cột là: ", df.shape[1])
    df_gdp = df.loc[:, "GDP (millions of US$)"]
    print("Giá trị lớn nhất của GDP: ", df_gdp.max())
    print("Giá trị nhỏ nhất của GDP: ", df_gdp.min())
    # print("Xu hướng phân bố GDP: ", df_gdp.mode())
    
    # df_chauluc = df.loc[:, 'Continent']
    # print("Châu lục xuất hiện nhiều nhất là:", df_chauluc.mode())
    
    df_3 = df.loc[:,['Continent', "GDP (millions of US$)"]]    
    # df_sum = df.pivot_table(values="GDP (millions of US$)", index="Continent", aggfunc=np.sum)
    # df_av = df.pivot_table(values="GDP (millions of US$)", index="Continent", aggfunc="mean")
    
    # df2 = df.merge(df_sum, df_av, on="Continent")
    # print(df2)