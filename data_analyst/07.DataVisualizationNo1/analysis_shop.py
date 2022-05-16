import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('07.DataVisualizationNo1\data\shopeep_koreantop_clothing_shop_data.csv')
    # Dataframe no1
    df1 = df.loc[::, ['join_year', 'item_count']]
    gr1 = df1.groupby(by='join_year')['item_count'].count()
    ls_year = [year for year, item in gr1.items()]
    ls_items = [item for year, item in gr1.items()]

    # Dataframe no2
    df2 = df.loc[::,['response_rate', 'rating_good']]
    
    # Dataframe no3
    df3 = df.loc[::, ['response_time', 'rating_bad']]
    print(df3)
    
    # Vẽ biểu đồ so sánh số lượng shop gia nhập theo các năm.
    # rect = plt.bar(ls_year, ls_items, width=0.5, color='c', ec='k', linewidth=3)
    # plt.bar_label(rect, padding=3)
    # plt.xlabel('Year', fontsize=15, color='b', fontweight=800)
    # plt.ylabel('Items', fontsize=15, color='m', fontweight=800)
    # plt.title('Number of item in year', fontsize=18, color='r', fontweight=1000)
    # plt.show()
    
    # Vẽ biểu đồ thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt.
    # plt.scatter(df2['response_rate'], df2['rating_good'])
    # plt.show()
    
    # Vẽ biểu đồ thể hiện mối quan hệ giữa thời gian phản hồi (đơn vị giây) với số lượt khách hàng đánh giá xấu.
    
    
    # Vẽ biểu đồ thể hiện phân bố của điểm đánh giá trung bình.
    # plt.hist(df['rating_normal'], bins=12)
    # plt.show()