import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv("08.DataVisualizationNo2\data\OnlineRetail.csv", encoding = "ISO-8859-1")

    # Biến đổi object về datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    d1 = df[['InvoiceNo', 'InvoiceDate', 'Quantity', 'UnitPrice']] #lấy các cột dữ liệu cần thiết
    # Tính danh thu
    d1['Revenue'] = d1['Quantity'] * d1['UnitPrice']
    d1 = d1.set_index('InvoiceDate')
    d2 = d1['2011']
    d2.reset_index(inplace=True)
    d3 = d2.groupby(by=d2['InvoiceDate'].dt.month).sum()
    
    d4 = d1.drop_duplicates(subset='InvoiceNo', keep='first')
    d5 = d4['2011']
    d5.reset_index(inplace=True)
    d5 = d5.groupby(by=d5['InvoiceDate'].dt.month).count()

    x = d5.index.get_level_values(0)
    
    plt.bar(x, d5['InvoiceNo'], tick_label=x, color='c', ec='k', lw=2, width=0.5, label='Invoice')
    
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax2.plot(x, d3['Revenue'], 'r-o', lw=2.5, label='Revenue')
    
    ax1.set_xlabel('Month', fontsize=12)
    ax1.set_ylabel('#Invoice', fontsize=12)
    ax2.set_ylabel('$', fontsize=12)
    plt.title("Sales report", fontsize=20, fontweight=1000, color='m')
    
    ax1.legend(fontsize=14, loc=2)
    ax2.legend(fontsize=14)
    
    plt.show()
    