import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("data/FoodPrice_in_Turkey.csv")
    print(df.head())
    
    # df.rename(columns={'Place':'Địa điểm','ProductName':'Tên SP'},inplace=True)
    
    # df['new_column'] = 'NaN'
    df['Giảm giá'] = pd.Series('10%', index=df.index)
    
    print(df.head())