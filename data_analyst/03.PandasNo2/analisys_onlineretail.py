import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv("03.PandasNo2\data\OnlineRetail.csv")
    # print(df.head(20))
    
    print(df.pivot_table(values='Quantity', index='InvoiceNo', columns='Country', aggfunc="mean"))
    print(df.pivot_table(values='Quantity', index='CustomerID', columns='StockCode', aggfunc="max"))
    print(df.pivot_table(values='Quantity', index='StockCode', aggfunc=[np.sum, np.mean]))
    print(df.pivot_table(values='Quantity', index='InvoiceDate', aggfunc=np.sum))