import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('04.DataManipulation\data\house_price_dống-da.xlsx')
    # print(df.head())
    
    df_p = df[(df['ward_name'] == 'Phường Khâm Thiên') | (df['ward_name'] == 'Phường Trung Liệt')]
    df_p = df_p[(df['land_certificate'] == "Sổ đỏ") & (df["bedroom"] >= 3)]
    df_pr = df_p.groupby(df['type_of_land'])['price'].mean()
    print(df_pr)
    df_p['room_average'] = (df_p['toilet'] + df['bedroom'] + df['floor'])/3
    df_p.reset_index(drop=True, inplace=True)
    print(df_p.head())
    df_p.to_excel("04.DataManipulation\data\house_no2.xlsx")