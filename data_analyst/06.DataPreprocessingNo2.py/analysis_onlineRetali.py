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
    
    df = df[df['Quantity'] >= 0]
    # print(df.shape)
    
    df1 = df.dropna()
    print(df1.shape)

    df2 = df.dropna(how="all")
    print(df2.shape)
    
    df3 = df.dropna(thresh=7)
    print(df3.shape)

    df4 = df.dropna(subset=["CustomerID"])
    print(df4.shape)
    