import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

if __name__ == '__main__':
    df = pd.read_csv('06.DataPreprocessingNo2.py\data\FoodPrice_in_Turkey.csv')
    # print(df.shape)
    # print(df.head())
    # print(df.describe())
    # print(df.info())
    
    df1 = df.dropna()
    # print(df1.shape)
    
    # sns.boxplot(x=df1['Price'])
    # plt.show()
    
    # IQR score
    Q1 = df1['Price'].quantile(0.25)
    Q3 = df1['Price'].quantile(0.75)
    IQR = Q3 - Q1
    
    df2 = df1
    df2['outlier'] = ~((df1['Price'] < (Q1 - 1.5*IQR)) | (df1['Price'] > (Q3 + 1.5*IQR)))
    df2 = df2[df2['outlier'] == True]
    # print(df2.describe())
    # sns.boxplot(x=df2['Price'])
    # sns.kdeplot(data=df2['Price'])
    # plt.show()
    
    # Chuẩn hóa dữ liệu với min-max score
    scaler = MinMaxScaler()
    mms = scaler.fit_transform(pd.DataFrame(df2['Price']))
    # print(pd.DataFrame(mms).describe())
    # sns.boxplot(x=mms)
    # plt.show()
    
    # print(df2['ProductName'].unique())
    
    # mã hóa cột ProductName với One-hot encoder
    encoder = OneHotEncoder()
    encoded_data = encoder.fit_transform(np.asarray(df2['ProductName']).reshape(-1,1))
    # print(encoded_data)
    # print(encoded_data.todense())
    # print(pd.get_dummies(df2['ProductName']))
    
    # Mã hóa cột ProductName với label encoder
    encoder = LabelEncoder()
    encoded_data = encoder.fit_transform(np.asarray(df2['ProductName']).reshape(-1,1))
    # print(encoded_data)
    # print(df2['ProductName'].astype('category').cat.codes)
    # print(df2.head())
    
    
    # Rời rạc dữ liệu
    cats = pd.qcut(df2['Price'], 5)
    # print(cats)
    # print(pd.value_counts(cats))