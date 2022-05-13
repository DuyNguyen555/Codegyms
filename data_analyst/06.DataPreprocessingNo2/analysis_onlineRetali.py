import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

if __name__ == '__main__':
    df = pd.read_csv("06.DataPreprocessingNo2.py\data\OnlineRetail.csv", encoding = "ISO-8859-1")
    # print(df.shape)
    # print(df.head())
    # df.info()
    
    # print(df[df['Quantity'] < 0])
    df = df[df['Quantity'] >= 0]
    # print(df.shape)
    
    df1 = df.dropna()
    # print(df1.shape)

    df2 = df.dropna(how="all")
    # print(df2.shape)
    
    df3 = df.dropna(thresh=7)
    # print(df3.shape)

    df4 = df.dropna(subset=["CustomerID"])
    # print(df4.shape)
    
    df5 = df
    df5["CustomerID"] = df["CustomerID"].fillna(-1)
    # print(df5[df5["CustomerID"] == -1])
    
    df5['Country'] = df["Country"].fillna(method="ffill")
    # print(df5)
    # sns.boxplot(x=df1['Quantity'])
    # plt.show()
    
    # Xử lý dữ liệu ngoại lai
    Q1 = df1['Quantity'].quantile(0.25)
    Q3 = df1['Quantity'].quantile(0.75)
    IQR = Q3 - Q1
    
    df6 = df1[~((df1['Quantity'] < Q1-1.5*IQR) | (df1['Quantity'] > Q3+1.5*IQR))]
    # print(df6.describe())
    # sns.boxplot(x=df6['Quantity'], color='red')
    # plt.show()
    
    
   # vẽ biểu đồ hộp cho cột Quantity
    # sns.boxplot(df1['Quantity'])
    # plt.show()
    # print(df1.describe())
    
    # Chuẩn hóa dữ liệu với min-max scaling.
    scaler = MinMaxScaler()
    mms = scaler.fit_transform(pd.DataFrame(df1['Quantity']))
    # print(pd.DataFrame(mms).describe())
    # sns.boxplot(x=mms)
    # plt.show()
    
    # Chuẩn hóa dữ liệu với Robust scaling.
    scaler = RobustScaler()
    rbs = scaler.fit_transform(pd.DataFrame(df1['Quantity']))
    # print(pd.DataFrame(rbs).describe())
    # sns.boxplot(x=rbs)
    # plt.show()
    
    # Chuẩn hóa dữ liệu với z-score scaling
    scaler = StandardScaler()
    sds = scaler.fit_transform(pd.DataFrame(df1['Quantity']))
    # print(pd.DataFrame(sds).describe())
    # sns.boxplot(x=sds)
    # plt.show()
    # sns.kdeplot(data=sds)
    # plt.show()
    
    # Rời rạc hóa dữ liệu
    cats = pd.cut(df1['UnitPrice'], 4)
    # print(cats)
    # print(pd.value_counts(cats))
    
    cats = pd.qcut(df1["UnitPrice"], 4)
    # print(cats)
    # print(pd.value_counts(cats))