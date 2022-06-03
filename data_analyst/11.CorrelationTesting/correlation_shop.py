import pandas as pd
from scipy import stats

if __name__ == '__main__':
    df= pd.read_csv('11.CorrelationTesting\data\shopeep_koreantop_clothing_shop_data.csv')
    
    # Giữa rating_star và follower_count
    df1 = df.filter(['rating_star', "follower_count"])
    df1.dropna(inplace=True)
    print(stats.pearsonr(df1.rating_star, df1.follower_count))
    # --> Do p value > 5% nên không có đủ cơ sở bác bỏ giả thuyết không
    # ==> Kết luận: giữa rating_star và follower_count không có mối tương quan tuyến tính
    
    # Giữa rating_star và số lượng sản phẩm (item_count)
    df2 = df.filter(['rating_star', 'item_count'])
    df2.dropna(inplace=True)
    print(stats.pearsonr(df2.rating_star, df2.item_count))
    # --> Do p value > 5% nên không có đủ cơ sở bác bỏ giả thuyết không
    # ==> Kết luận: giữa rating_star và item_count không có mối tương quan tuyến tính

    # Giữa is_shopee_verified và việc có cửa hàng trưng bày (is_official_shop)
    df3 = df.filter(['is_shopee_verified', 'is_official_shop'])
    df3.dropna(inplace=True)
    print(stats.pearsonr(df3.is_shopee_verified, df3.is_official_shop))
    # --> Do p value > 5% nên không có đủ cơ sở bác bỏ giả thuyết không
    # ==> Kết luận: giữa is_shopee_verified và item_count không có mối tương quan tuyến tính