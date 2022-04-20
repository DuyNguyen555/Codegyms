import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('01.Overview\data\FoodPrice_in_Turkey.csv')
    column, row = df.shape
    print("Số cột của dữ liệu là: ", row)
    print("Số hàng của dữ liệu là: ", column)
    df.info()
    # print(df.head())
    df = df.groupby(['ProductName'])['Price'].mean()
    print(df)