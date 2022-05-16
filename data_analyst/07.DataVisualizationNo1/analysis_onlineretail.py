import pandas as pd
import matplotlib.pyplot as plt
import datetime

if __name__ == '__main__':
    df = pd.read_csv('07.DataVisualizationNo1\data\OnlineRetail.csv', encoding="ISO-8859-1")
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    data = df[["InvoiceNo", "InvoiceDate"]]
    data.drop_duplicates(subset = 'InvoiceNo', keep = 'first', inplace=True, ignore_index=True)
    data1= data.set_index(['InvoiceDate'])
    d2 = data1['2011']
    d2.reset_index(inplace=True)
    d3 = d2.groupby(d2['InvoiceDate'].dt.month).count()
    
    x = d3.index.get_level_values(0)
    plt.bar(x, d3['InvoiceDate'])
    plt.title('Number of Invoices in 2011 (month)', fontsize = 16)
    plt.xlabel('Month', fontsize = 14)
    plt.ylabel('Invoices', fontsize = 14)
    plt.show()