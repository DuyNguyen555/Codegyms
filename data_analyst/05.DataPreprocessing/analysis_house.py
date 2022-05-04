import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

if __name__ == '__main__':
    df = pd.read_excel('05.DataPreprocessing\data\house_price_dống-da.xlsx')
    # print(df.info())
    # print(df.describe())
    
    # Xóa dữ liệu khuyết thiếu khi thuộc tính price không có giá trị
    df.dropna(subset=['price'],inplace=True)
    
    lis_row = ['house_direction', 'balcony_direction', 'toilet', 'bedroom', 'floor']
    lis_mode = []
    for i in lis_row:
        lis = list(df[i].mode())
        lis_mode.append(lis)
    
    # print(lis_mode)
    
    values = {}
    for i in range(len(lis_row)):
        value = {lis_row[i]: lis_mode[i][0]}
        values.update(value)
    
    df = df.fillna(value=values)
    
    df = df[(df['type_of_land'] == "Bán nhà riêng")]
    
    # Tính 1 m thì bao nhiêu tiền
    df['price1m'] = df['price'] / df['area']

    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1

    df2 = df[~((df < Q1-1.5*IQR) | (df > Q3+1.5*IQR)).any(axis=1)]
    
    # # Chuẩn hóa dữ liệu
    # # min-max scaling
    # scaler = MinMaxScaler()
    # mms = scaler.fit_transform(pd.DataFrame(df['price1m']))
    # mms_new = scaler.fit_transform(pd.DataFrame(df2['price1m']))
    # sns.kdeplot(data=mms)
    
    # # Robust scaling
    # scaler = RobustScaler()
    # rbs = scaler.fit_transform(pd.DataFrame(df['price1m']))
    # rbs_new = scaler.fit_transform(pd.DataFrame(df2['price1m']))
    
    # # Z-score scaling
    # scaler = StandardScaler()
    # zss = scaler.fit_transform(pd.DataFrame(df['price1m']))
    # zss_new = scaler.fit_transform(pd.DataFrame(df2['price1m']))
    
    
    # sns.kdeplot(data=mms_new)
    # plt.show()
    
    # sns.kdeplot(data=zss_new)
    # plt.show()
    
    # sns.kdeplot(data=zss_new)
    # plt.show()