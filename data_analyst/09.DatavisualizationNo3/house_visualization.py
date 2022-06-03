import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def request1(data):
    """
    Vẽ biểu đồ xu hướng phân tích mối quan hệ giữa giá nhà với diện tích,
    giá nhà với số lượng phòng ngủ.
    """
    sns.set(style='darkgrid', palette='muted')
    sns.lmplot(data=data, y='area',x='price')
    plt.show()
    sns.lmplot(data=data, x='bedroom', y='price')
    plt.show()
    
def request2(data):
    """
    Vẽ biểu đồ phân bố thể hiện phân bố của giá nhà theo các hướng.
    """
    sns.set(style='darkgrid', palette='Set1')
    sns.violinplot(x='house_direction', y='price', data=data)
    plt.show()

def request3(data):
    """
    Vẽ biểu đồ tần số để đếm số nhà ở mỗi hướng nhà.
    """
    sns.set(style='whitegrid', palette='twilight')
    sns.countplot(x='house_direction', data=data)
    plt.show()
    
def request4(data):
    sns.set(style='whitegrid', palette='Blues')
    data2 = data.groupby(['house_direction']).count()
    sns.boxplot(x=data2.index, y=data2.area)
    plt.show()

if __name__ == '__main__':
    df = pd.read_excel('09.DatavisualizationNo3\data\house_price_dống-da.xlsx')
    
    # Preprocessing
    df.dropna(subset=['toilet', 'bedroom', 'area', 'price'] ,inplace=True)
    values = {'floor': 1, 'house_direction':'Đông-Nam'}
    df.fillna(value=values ,inplace=True)
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.27)
    IQR = Q3 - Q1
    df = df[~((df['price'] < (Q1-IQR*1.5)) | (df['price'] > (Q3+IQR*1.5)))]
    
    # Visualizaion
    data = df[['area','price', 'house_direction', 'bedroom']]
    request1(data)
    request2(data)
    request3(data)
    request4(data)