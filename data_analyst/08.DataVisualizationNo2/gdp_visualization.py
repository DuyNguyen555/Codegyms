import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv('08.DataVisualizationNo2\data\GDPlist.csv')

    df1 = df[(df['Country']=='Vietnam')]
    df2 = df[(df['Country']=='Thailand')]
    df3 = df[(df['Country']=='Indonesia')]
    df4 = df[(df['Country']=='Cambodia')]
    df5 = df[(df['Country']=='Malaysia')]
    color=['orange', 'c', 'm', 'red', 'blue']
    data = pd.concat([df1, df2, df3, df4, df5], axis=0)
    
    
    fig, ax = plt.subplots(1, 2)
    rect = ax[0].bar(data['Country'], data['GDP (millions of US$)'], color=color, ec = 'k', lw=2, label=data['Country'])
    ax[0].bar_label(rect, padding=4)
    ax[1].pie(data['GDP (millions of US$)'], labels=data['Country'], autopct='%1.2f%%', colors=color, radius=1.3)

    ax[0].set_xlabel('Country', fontsize=14)
    ax[0].set_ylabel('GDP', fontsize=14)
    
    plt.show()