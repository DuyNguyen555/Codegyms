import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

if __name__ == '__main__':
    df = pd.read_csv('05.DataPreprocessing\data\Credit_Scoring.csv')
    # df.info()
    # print(df.describe())
    # print(df.isna())
    
    # Xóa dữ liệu khuyết thiếu
    df1 = df.dropna()
    # print(df1)
    # print("data=", 100*df1.shape[0]/df.shape[0], "%")
    # sns.kdeplot(data = df1['MonthlyIncome'])
    # plt.show()
    
    # Thay thế dữ liệu khuyết thiếu
    df2 = df.interpolate(axis=1)
    # print(df2.isna())
    # df2.boxplot()
    # sns.boxplot(df2['MonthlyIncome'])
    # plt.show()
    
    # Lọc dữ liệu ngoại lai
    Q1 = df2.quantile(0.25)
    Q3 = df2.quantile(0.75)
    IQR = Q3 - Q1
    df3 = df2[~((df2 < Q1-1.5*IQR) | (df2 > Q3+1.5*IQR)).any(axis=1)]
    # df3.boxplot()
    # sns.boxplot(df3["MonthlyIncome"])
    # plt.show()
    # print(df3.describe())
    
    # Chuẩn hóa dữ liệu trên cột MonthlyIncome
    sns.kdeplot(data=df3['MonthlyIncome'])
    plt.show()
    
    # Chuẩn hóa dữ liệu với MinMaxScaler
    scaler = MinMaxScaler()
    mms = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
    sns.kdeplot(data=mms)
    plt.show()
    
    # Chuẩn hóa dữ liệu với RobustScaler
    scaler = RobustScaler()
    rbs = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
    sns.kdeplot(data=rbs)
    plt.show()
    
    # Chuẩn hóa dữ liệu với StandarScaler
    scaler = StandardScaler()
    sds = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
    sns.kdeplot(data=sds)
    plt.show()
