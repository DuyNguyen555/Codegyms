import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def shop_join(data):
    """
    Vẽ biểu đồ tần số số lượng shop gia nhập theo các năm.
    """
    sns.set(style='darkgrid', palette='Oranges')
    data = data.drop_duplicates(subset='pk_shop', keep='first')
    
    # Visualization
    sns.countplot(x='join_year', data=data)
    plt.show()

def response_good(data):
    """
    Vẽ biểu đồ xu hướng thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt.
    """
    sns.set(style='whitegrid', palette='cool')

    # Visualization
    sns.lmplot(x='response_rate', y='rating_good', data=data)
    plt.show()

def response_normal(data):
    """
    Vẽ biểu đồ thể hiện phân bố của điểm đánh giá trung bình.
    """
    sns.set(style='whitegrid', palette='twilight')

    # Visualization
    sns.barplot(y='rating_normal', data=data)
    plt.show()

def official(data):
    """
    Vẽ biểu đồ tần số của cửa hàng chính thức và không chính thức.
    """
    sns.set(style='whitegrid', palette='viridis')
    condition = [(data['is_official_shop'] == 0),(data['is_official_shop'] == 1)]
    choice = ['Unofficial', 'Official']
    data['is_official_shop'] = np.select(condition, choice, default=choice[0])
    
    # Visualization
    sns.countplot(x='is_official_shop', data=data)
    plt.show()

def verified(data):
    """
    Vẽ biểu đồ tần số của cửa hàng được xác thực với chưa xác thực. 
    """
    sns.set(style='whitegrid', palette='crest')
    condition = [(data['is_shopee_verified'] == 0),(data['is_shopee_verified'] == 1)]
    choice = ['Unconfirmed', 'Verified']
    data['is_shopee_verified'] = np.select(condition, choice, default=choice[0])
    
    # Visualization
    sns.countplot(x='is_shopee_verified', data=data)
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv("09.DatavisualizationNo3\data\shopeep_koreantop_clothing_shop_data.csv")

    # Handle missing data
    df.dropna(inplace=True)
    
    # Function
    shop_join(df[['pk_shop', 'join_year']])
    response_good(df[['response_rate','rating_good']])
    response_normal(df[['rating_normal']])
    official(df[['is_official_shop']])
    verified(df[['is_shopee_verified']])
    