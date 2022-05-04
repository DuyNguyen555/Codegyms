import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pd.read_csv('05.DataPreprocessing\data\OnlineRetail.csv', encoding='ISO-8859-1')
    # df.info()
    # print(df.describe())
    # print(df.isna())
    # Không hẵn là cần xóa tất cả các dòng không có giá trị vì những dòng ấy có thể không liên quan đến các phép tính như là thông tin của sản phẩm đó
    # df.boxplot()
    # plt.show()
    
    # Thay thế giá trị NaN của thuộc tính Description bằng Not Know
    df['Description'].fillna("Not Know")
    
    df2 = df[(df['Quantity'] >= 0) & (df['UnitPrice'] != 0)]
    
    # sns.boxplot(data=df['Quantity'])
    # plt.show()
    # sns.boxplot(data=df2['Quantity'])
    # plt.show()

    # sns.boxplot(data=df['UnitPrice'])
    # plt.show()
    # sns.boxplot(data=df2['UnitPrice'])
    # plt.show()
    
    print(df2.describe())