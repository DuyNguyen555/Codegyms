import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sympy import rotations

def milk_gas(data):
    data.plot(x='x', y=['y1', 'y2'], kind='bar')
    
    plt.xlabel("Place", fontsize=12)
    plt.ylabel("Price", fontsize=12)
    plt.title("Milk and Gas Price in 12/2019", fontsize=14, color='r')
    plt.show()

def milk_gas_NA(d):
    d11 = d[(d['Place'] == 'National Average') & (d['Year'] == 2016) & (d['ProductName'] == 'Milk (powder, infant formula) - Retail')]
    d12 = d[(d['Place'] == 'National Average') & (d['Year'] == 2016) & (d['ProductName'] == 'Fuel (gas) - Retail')]

    d21 = d[(d['Place'] == 'National Average') & (d['Year'] == 2018) & (d['ProductName'] == 'Milk (powder, infant formula) - Retail')]
    d22 = d[(d['Place'] == 'National Average') & (d['Year'] == 2018) & (d['ProductName'] == 'Fuel (gas) - Retail')]
    
    d31 = d[(d['Place'] == 'National Average') & (d['Year'] == 2019) & (d['ProductName'] == 'Milk (powder, infant formula) - Retail')]
    d32 = d[(d['Place'] == 'National Average') & (d['Year'] == 2019) & (d['ProductName'] == 'Fuel (gas) - Retail')]

    fig, ax = plt.subplots(3,2)
    
    ax[0][0].plot(d11['Month'], d11['Price'], "c-o", lw=2, label='Milk')
    ax[0][0].plot(d12['Month'], d12['Price'], "m-s", lw=2, label='Gas')
    ax[0][0].set_ylabel("Price")
    ax[0][0].set_title("2016")
    ax[0][0].set_xticklabels([])
    ax[0][0].legend()
    
    ax[1][0].plot(d21['Month'], d21['Price'], "c-o", lw=2)
    ax[1][0].plot(d22['Month'], d22['Price'], "m-s", lw=2)
    ax[1][0].set_ylabel("Price")
    ax[1][0].set_title("2018")
    ax[1][0].set_xticklabels([])
    
    ax[2][0].plot(d31['Month'], d31['Price'], "c-o", lw=2)
    ax[2][0].plot(d32['Month'], d32['Price'], "m-s", lw=2)
    ax[2][0].set_ylabel("Price")
    ax[2][0].set_title("2019")
    ax[2][0].set_xlabel("Month")
    
    ax[0][1].scatter(d11['Price'], d12['Price'], color = 'violet')
    ax[0][1].set_title("2016")
    ax[0][1].set_xticklabels([])
    
    ax[1][1].scatter(d21['Price'], d22['Price'], color = 'violet')
    ax[1][1].set_title("2018")
    ax[1][1].set_xticklabels([])
    
    ax[2][1].scatter(d31['Price'], d32['Price'], color = 'violet')
    ax[2][1].set_title("2019")
    ax[2][1].set_xlabel("Gas")
    plt.show()

if __name__ == '__main__':
    d = pd.read_csv('08.DataVisualizationNo2\data\FoodPrice_in_Turkey.csv')
    
    d_milk = d[(d['Year'] == 2019) & (d["ProductName"] == "Milk (powder, infant formula) - Retail") & (d["Month"] == 12)].reset_index()
    d_gas = d[(d['Year'] == 2019) & (d["ProductName"] == "Fuel (petrol-gasoline) - Retail") & (d["Month"] == 12)].reset_index()
    data1 = pd.DataFrame({"x":d_milk["Place"],
                          "y1": d_milk["Price"],
                          "y2": d_gas["Price"]})
    
    # milk_gas(data1)
    milk_gas_NA(d)