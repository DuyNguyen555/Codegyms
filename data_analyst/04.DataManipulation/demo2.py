import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("04.DataManipulation\data\shopeep_koreantop_clothing_shop_data.csv")
    # print(df.shape)
    
    df2 = df.groupby(['name'])['follower_count'].mean()
    print(df2)
    df3 = df.groupby(['name'])['rating_normal'].sum()
