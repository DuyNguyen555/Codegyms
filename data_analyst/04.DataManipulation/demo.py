import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("04.DataManipulation\data\shopeep_koreantop_clothing_shop_data.csv")
    
    df1 = df.filter(['shop_location'])
    # df1 = df['shop_location']
    # print(df1)
    # df4=df.filter(['pk_shop','rating_bad','rating_good'])[:8]
    # print(df4)
    # df5 = df[df['join_month']=='April']
    # print(df5)
    # df6 = df[(df['join_year'] == 2021) & (df['follower_count'] >= 10000)]
    # print(df6)
    # df7 = df[df['join_month']=='April'].filter(['response_time', 'response_rate'])
    # print(df7)
    df8 = df.query('(join_year == 2021) and (follower_count >= 10000)').filter(["shop_location"])
    print(df8)