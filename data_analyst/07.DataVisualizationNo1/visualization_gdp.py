import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__=='__main__':
    df =pd.read_csv('07.DataVisualizationNo1\data\GDPlist.csv')
    df_sa = df[(df['Continent']=='South America')]
    df_sa.reset_index(inplace=True)
    df_as = df[(df['Continent']=='Asia')]
    
    condition = [df_as['Country'] == 'Vietnam',
                df_as['Country'] == 'Indonesia',
                df_as['Country'] == 'Cambodia',
                df_as['Country'] == 'Thailand',
                df_as['Country'] == 'Malaysia']
    
    df_as['Southeast Asia'] = np.select(condition,[1,1,1,1,1], default=0)
    df_as = df_as[(df_as['Southeast Asia']==1)]
    
    
    # GDP of South America
    rect = plt.bar(df_sa['Country'], df_sa['GDP (millions of US$)'], label=df_sa['Country'],
                   width=0.5, color='c', ec='k', linewidth=2)
    
    plt.bar_label(rect, padding=5)
    plt.xlabel("Country", fontsize=15, fontweight=800, color='b')
    plt.ylabel("GDP(millions of US$)", fontsize=15, fontweight=800, color='m')
    plt.title("GDP of South America", fontsize=20, fontweight=1000, color='r')
    plt.show()
    """Cho thấy mức trung bình GDP của Brazil cao nhất so với mức trung bình GDP của các nước còn lại.
    Paraguay có GDP thấp nhất, kế tiếp lần lượt là Uruguay, Ecuador.
    Các nước còn lại đều có mức GDP tương đối nhau"""
    
    # GDP of Southeast Asia
    rect1 = plt.bar(df_as['Country'], df_as['GDP (millions of US$)'], label=df_as['Country'],
                    color='violet', ec='k', linewidth=2, width=0.5)
    
    plt.bar_label(rect1, padding=5)
    plt.xlabel("Southeast Asia countries", fontsize=15, fontweight=800, color='r')
    plt.ylabel("GDP (millions of US$)]", fontsize=15, fontweight=800, color='b')
    plt.title("GDP of five Southeast Asia countries",fontsize=20, fontweight=1000, color='y')
    plt.show()
    """Cho thấy Việt Nam thấp thứ nhì so với GPD trong 5 nước"""