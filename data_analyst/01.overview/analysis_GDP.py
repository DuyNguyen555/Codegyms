import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("01.Overview\data\GDPlist.csv", encoding = "ISO-8859-1")
    data.info()
    column, row = data.shape
    print("Số cột là:", row, ",số dòng là:", column)
    
    data.info()
    
    # gdp = data['GDP (millions of US$)']
    # print("GDP của mỗi quốc gia không đồng đều: ")
    # print(gdp)
    
    print('Số lượng các quốc gia trong khu vực có trong bảng: ')
    data['count'] = 1
    total = data.groupby(['Continent'])['count'].sum()
    print(total)
    
    del data['count']
    print('Tổng GPD của các châu lục là: ')
    print(data.groupby(['Continent']).sum())
    
    data = data.sort_values('GDP (millions of US$)', ascending = False)
    print(data.head(10))