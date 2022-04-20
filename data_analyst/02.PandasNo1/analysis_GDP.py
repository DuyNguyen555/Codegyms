import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('02.PandasNo1\data\GDPlist.csv')
    column, row = df.shape
    print("Số dòng là:", column, ", số cột là:", row)
    df.info()
    # Thay đổi tên cột của bảng
    df.rename(columns ={"Country": "Nuoc", "Continent": "ChauLuc", "GDP (millions of US$)": "GDP (trieu $)"}, inplace=True)
    
    # Thêm cột thanh pho
    nuoc = df.loc[:, 'Nuoc']
    df.insert(1, "Thanhpho", nuoc)
    
    # Thay các dữ liệu bên trong cột thanh pho thành "Hanoi"
    temp = df.iloc[:,1]
    for i in temp:
        df['Thanhpho'].replace(i ,"Hanoi", inplace=True)
    
    # Xóa các châu lục là Asia
    lis = df.loc[df.ChauLuc == 'Asia'].index
    df.drop(lis, axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    # Xóa GDP dưới 300000
    lis = df.loc[df['GDP (trieu $)'] < 300000].index
    df.drop(lis, axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    print(df.head())
    