import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv('04.DataManipulation\data\OnlineRetail.csv', encoding='ISO-8859-1')
    # print("Số dòng là:", df.shape[0],"/nSố cột là:",df.shape[1])
    # print("Các thuộc tính trong bảng là: ")
    # print(df.dtypes)

    # Previous 1
    cd_1 = (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 1) | (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 2) | (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 3)
    
    # Previous 2
    cd_2 =  (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 4) | (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 5) | (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 6)
    
    # Previous 3
    cd_3 = (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 7) | (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 8) | (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 9)
    
    # Previous 4
    cd_4 = (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 10) | (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 11) | (pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.month == 12)
    
    conditions_previous = [cd_1, cd_2, cd_3, cd_4]
    
    choice_previous = [1, 2, 3, 4]
    
    # Add new row: Previous
    df['Previous'] = np.select(conditions_previous, choice_previous, default=0)
    
    # Add new row: Amount
    df['Amount'] = df.Quantity * df.UnitPrice
    
    conditions_discount = [(df['Country'] == 'United Kingdom') & (df['Previous'] == 4), (df['Country'] == 'France')]
    choice = [10,5]
    
    # Add new row: Discount
    df['Discount'] = np.select(conditions_discount, choice, default = 0)
    
    # Add new row: Total
    df['Total'] = df.Amount - df.Discount
    
    print(df.head())
