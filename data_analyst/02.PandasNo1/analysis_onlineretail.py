import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('02.PandasNo1\data\OnlineRetail.csv')
    print('Số cột dòng là:', df.shape[0], 'số cột là:', df.shape[1])
    print(df.head(10))
    
    # Trích xuất dữ liệu
    data_csv = df.loc[:,['Description', 'Quantity']]
    data_xlsx = df.iloc[:1000]
    data_hdf = df.loc[df['Quantity'] >= 10]
    data_hdf.reset_index(drop=True, inplace=True)
    data_json = df.loc[1000:2000, ['Quantity', 'InvoiceDate', 'UnitPrice']]
    data_html = df.loc[df['InvoiceNo'] == 536365]
    
    # Ghi dữ liệu
    data_csv.to_csv('02.PandasNo1\data\OnlineRetail2.csv')
    data_xlsx.to_excel('02.PandasNo1\data\OnlineRetail.xlsx')
    data_hdf.to_hdf('02.PandasNo1\data\OnlineRetail.h5', 'table')
    data_json.to_json('02.PandasNo1\data\OnlineRetail.json')
    data_html.to_html('02.PandasNo1\data\OnlineRetail.html')