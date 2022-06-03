import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def IQR(data, x):
    Q1 = data[x].quantile(0.25)
    Q3 = data[x].quantile(0.75)
    IQR = Q3 - Q1
    
    data = data[~((data[x]<(Q1-IQR*1.5)) | (data[x]>(Q3+IQR*1.5)))]
    return data
    
def request1(data):
    fig, ax = plt.subplots(1,3)
    
    ax[0].scatter(data.area, data.price, c='c', alpha=0.5)
    ax[0].set_ylabel('Price', fontsize=14, labelpad=20)
    ax[0].set_xlabel('Area', fontsize=14, labelpad=15)
    ax[0].tick_params(axis='y', size=10)
    
    ax[1].scatter(data.bedroom, data.price, c='m', alpha=0.5)
    ax[1].set_xlabel('Bedroom', fontsize=14, labelpad=15)
    ax[1].set_yticklabels([])
    
    ax[2].scatter(data.toilet, data.price, c='brown', alpha=0.5)
    ax[2].set_xlabel('Toilet', fontsize=14, labelpad=15)
    ax[2].set_yticklabels([])
    plt.show()

def request2(data):
    data_land = data.groupby(by='type_of_land')['1/m^2'].sum()
    x = [name for name, group in data_land.items()]
    y = [group for name, group in data_land.items()]
    fig, ax = plt.subplots(1, 2)
    
    rect = ax[0].bar(x, y)
    ax[0].bar_label(rect, padding=4)
    ax[0].set_xlabel('Type of land', fontsize=14)
    ax[0].set_ylabel('1/m^2', fontsize=14)
    ax[0].grid()

    ax[1].pie(y, labels=x, autopct="%1.2f%%", radius=1.3)
    
    plt.show()

def request3(data):
    fig, ax = plt.subplots(1, 3)
    
    ax[0].scatter(data['area'], data['1/m^2'], c='c', alpha=0.5)
    ax[0].set_ylabel('1/m^2', fontsize=14, labelpad=15)
    ax[0].set_xlabel('Area', fontsize=14, labelpad=15)
    ax[0].tick_params(axis='y', size=10)
    
    ax[1].scatter(data['bedroom'], data['1/m^2'], c='m', alpha=0.5)
    ax[1].set_xlabel('Bedroom', fontsize=14)
    
    ax[2].scatter(data['toilet'], data['1/m^2'], c='brown', alpha=0.5)
    ax[2].set_xlabel('Toilet', fontsize=14)
    ax[2].set_yticklabels([])
    
    plt.show()

if __name__ == '__main__':
    df = pd.read_excel('08.DataVisualizationNo2\data\house_price_dống-da.xlsx')

    # Filter the data
    df.dropna(subset=['area', 'toilet', 'bedroom'] ,inplace=True)
    values = {'floor': 1}
    df.fillna(value=values ,inplace=True)
    df['1/m^2'] = df['area'] * df['price']
    data = df[['area', 'price', 'toilet', 'bedroom', '1/m^2', 'type_of_land']]
    data = IQR(data, 'price')
    
    # Visualization
    request1(data)
    request2(data)
    request3(data)
    