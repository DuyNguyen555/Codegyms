import pandas as pd

if __name__ == '__main__':
    data_csv = pd.read_csv('data/FoodPrice_in_Turkey.csv', sep = ',')
    print(data_csv.head())
    
    row = data_csv.iloc[3:6, 5]
    print(row['Year'])

    # data_xlsx = pd.read_excel('data/house_price_dống-da.xlsx', engine = 'openpyxl')
    # print(data_xlsx.head())