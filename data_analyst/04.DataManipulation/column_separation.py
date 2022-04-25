import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('04.DataManipulation\data\shopeep_koreantop_clothing_shop_data.csv')
    df = df[['date_collected','shop_location','response_time']]
    
    df['District'] = df['shop_location'].str.split(',').str[0]
    df['City'] = df['shop_location'].str.split(',').str[1]
    
    df['Day'] = pd.to_datetime(df['date_collected'], format='%Y-%m-%d').dt.day
    df['Month'] = pd.to_datetime(df['date_collected'], format='%Y-%m-%d').dt.month
    df['Year'] = pd.to_datetime(df['date_collected'], format='%Y-%m-%d').dt.year
    
    df['Hour'] = pd.to_datetime(df['response_time'],   format=' %H:%M:%S').dt.hour
    df['Minute'] = pd.to_datetime(df['response_time'], format=' %H:%M:%S').dt.minute
    df['Second'] = pd.to_datetime(df['response_time'], format=' %H:%M:%S').dt.second
    print(df.head(20))