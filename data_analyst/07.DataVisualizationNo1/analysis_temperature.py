import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('07.DataVisualizationNo1\data\daily-min-temperatures.csv')

    # Histogram
    plt.hist(df['Temp'], bins=45, range = (1, 23), histtype = 'step')
    plt.xlabel('Date', fontsize=10, color='b', fontweight=1000)
    plt.ylabel('Temperature', fontsize=10, color='r', fontweight=1000)
    plt.title('Temperature Histogram', fontsize = 16)
    plt.show()
    
    # Column chart
    df['Date'] = pd.to_datetime(df['Date'])
    bounds = ['1/1/1990', '12/31/1990']
    bounds = pd.to_datetime(bounds)
    d1 = df[(df['Date'] >= bounds[0]) & (df['Date'] <= bounds[1])]
    plt.plot(d1['Date'], d1['Temp'])
    plt.title('Daily Temperature', fontsize = 16)
    plt.xlabel('Date', fontsize = 14)
    plt.ylabel('Temp', fontsize = 14)
    plt.show()