import pandas as pd

if __name__ == '__main__':
    df=pd.read_csv(filepath_or_buffer = 'data/FoodPrice_in_Turkey.csv', sep = ',')
    print(df.head())
    df.to_csv('data\sub_1.csv')
    