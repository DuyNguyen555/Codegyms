import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def request1(data):
    data_y = data.groupby(by=['join_year']).count()
    # print(data_y.index)
    month = data['join_month'].unique()
    # print(month)
    # print(month[0])

    num_month = {'January': 1, 'February': 2, 'March': 3, 'April': 4,'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    
    conditions = [(data['join_month'] == name) for name, num in num_month.items()]
    choice = [num for name, num in num_month.items()]
    data['num_month'] = np.select(conditions, choice, default=0)
    
    d15 = data[(data['join_year'] == 2015)]
    d16 = data[(data['join_year'] == 2016)]
    d17 = data[(data['join_year'] == 2017)]
    d18 = data[(data['join_year'] == 2018)]
    d19 = data[(data['join_year'] == 2019)]
    d20 = data[(data['join_year'] == 2020)]
    d21 = data[(data['join_year'] == 2021)]
    
    dm15 = d15.groupby(by=['num_month']).count()
    dm16 = d16.groupby(by=['num_month']).count()
    dm17 = d17.groupby(by=['num_month']).count()
    dm18 = d18.groupby(by=['num_month']).count()
    dm19 = d19.groupby(by=['num_month']).count()
    dm20 = d20.groupby(by=['num_month']).count()
    dm21 = d21.groupby(by=['num_month']).count()    
    
    fig, ax = plt.subplots(2,4)
    rect = ax[0][0].bar(data_y.index, data_y.name, color='c', ec='k', lw=2)
    ax[0][0].bar_label(rect, padding=4)
    ax[0][0].set_xlabel('Year', fontsize=14, loc='left')
    ax[0][0].set_ylabel('Shop', fontsize=14)
    
    ax[0][1].plot(dm15.index, dm15.name, '-o', color='deepskyblue')
    ax[0][1].set_title('2015')
    
    ax[0][2].plot(dm16.index, dm16.name, '-o', color='deepskyblue')
    ax[0][2].set_title('2016')

    ax[0][3].plot(dm17.index, dm17.name, '-o', color='deepskyblue')
    ax[0][3].set_title('2017')

    ax[1][0].plot(dm18.index, dm18.name, '-o', color='deepskyblue')
    ax[1][0].set_ylabel('Number of participating stores', fontsize=12)
    ax[1][0].set_xlabel('Month', fontsize=14)
    ax[1][0].set_title('2018')

    ax[1][1].plot(dm19.index, dm19.name, '-o', color='deepskyblue')
    ax[1][1].set_title('2019')

    ax[1][2].plot(dm20.index, dm20.name, '-o', color='deepskyblue')
    ax[1][2].set_title('2020')

    ax[1][3].plot(dm21.index, dm21.name, '-o', color='deepskyblue')
    ax[1][3].set_title('2021')

    
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('08.DataVisualizationNo2\data\shopeep_koreantop_clothing_shop_data.csv')
    
    # Filter the data
    df.dropna(inplace=True)
    data1 = df[['name', 'join_year', 'join_month']]
    # Visualization
    request1(data1)