import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv('08.DataVisualizationNo2\data\FoodPrice_in_Turkey.csv')
    
    df_milk = df[(df['Year'] == 2019) & (df['ProductName'] == 'Milk (powder, infant formula) - Retail')].reset_index()
    
    df_gas = df[(df['Year'] == 2019) & (df['ProductName'] == 'Fuel (gas) - Retail')].reset_index()

    data1 = pd.DataFrame({'x': df_milk['Place'], 'y1': df_milk['Price'], 'y2': df_gas['Price']})
    
    data_loc = data1.loc[::,[df]]
    
    data1.plot(x='x', y = ['y1', 'y2'], kind='bar')
    plt.title('Milk and Gas Price in 12/2019', fontsize = 16, color = 'r')
    plt.xlabel('Place', fontsize=14)
    plt.ylabel('Price', fontsize=14)
    
    plt.show()