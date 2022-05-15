import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('07.DataVisualizationNo1\data\FoodPrice_in_Turkey.csv')
    fig, ax = plt.subplots()

    # Column chart
    data = df[(df['Year'] == 2019) & (df['Month'] == 12) &(df['ProductName'] == 'Rice - Retail')]
    cl = ["m","c","b","brown"]
    d_place = data.groupby(by='Place')
    ls_place = [name for name,group in d_place]
    ls_price = [list(group['Price'])[0] for name, group in d_place]
    count = len(ls_place)
    
    rect = ax.bar(ls_place, ls_price, label=ls_place, color=cl, ec='black', lw=2, width=0.5)
    ax.bar_label(rect, padding=3)
    plt.xlabel("Place", fontsize=10)
    plt.ylabel("Price", fontsize=10)
    plt.title('Rice Price in 12/2019', fontsize = 18)
    plt.show()
    
    # Line grap
    # data2 = df[(df['Place'] == 'National Average') & (df['Year'] == 2019) & (df['ProductName'] == 'Rice - Retail')]
    # rect2 = ax.plot(data2['Month'], data2['Price'], linewidth=2, marker="o", markersize=5, c='r', linestyle='--', label='Price')
    
    # ax.legend()
    # plt.xlabel("Month", fontsize=10, fontweight=1000)
    # plt.ylabel("Price", fontsize=10, fontweight=1000)
    # plt.title("'Rice Price of National Average in 2019'", fontsize=20)
    # plt.show()
    
    # Scatter
    # x = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Year'] == 2019)]
    # y = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Rice - Retail') & (df['Year'] == 2019)]

    # ax.scatter(x['Price'], y['Price'], s=50, alpha=0.5)

    # plt.xlabel("Gas", fontsize=10, color='brown')
    # plt.xlabel("Rice", fontsize=10, color='y')
    # plt.title('Relationship between Rice Price and Gas Price', fontsize=15, color='b')
    # plt.show()