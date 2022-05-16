from statistics import median
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_excel('07.DataVisualizationNo1\data\house_price_dống-da.xlsx')
    df.dropna(subset=['price', 'land_certificate', 'toilet', 'bedroom', 'area'], inplace=True)
    df = df[(df['toilet'] > 0) & (df['bedroom'] > 0) & (df['price'] > 0) & (df['area'] > 0)]
    
    # Dataframe no1
    df_price=df.sort_values(by='price')
    
    # Dataframe no2
    df_type = df.loc[::, ['type_of_land', 'area']]
    df_mean = df_type.groupby(by=['type_of_land']).mean()
    ls_mean = [list(round(group, 3)) for name, group in df_mean.items()]
    ls_mean = ls_mean[0]
    ls_type = ['Bán nhà mặt phố', 'Bán nhà mặt phố\n', 'Bán nhà riêng', 'Bán nhà riêng\n',
                'Bất động sản khác', 'Bất động sản khác\n', 'Chung cư', 'Tập thể, cư xá']
    
    # print(ls_mean)
    # print(ls_type)
    
    # for i, n in df_mean.items():
    #     print(n)
    
    # Dataframe no3
    df_tl = df.loc[::,['type_of_land']]
    dic_tl =df_tl['type_of_land'].value_counts().to_dict()
    ls_key = [i for i in dic_tl.keys()]
    ls_value = [i for i in dic_tl.values()]
    
    # Dataframe no4
    df_mb = df.loc[::, ['area', 'price', 'bedroom']]
    df_mb['1/m^2'] = df_mb['price'] * df_mb['area']
    gr_mb = df_mb.groupby(by='bedroom')['1/m^2'].mean()
    ls_bed = [name for name, group in gr_mb.items()]
    ls_m = [group for name, group in gr_mb.items()]
    
    # Vẽ biểu đồ phân tích mối liên hệ giữa diện tích với giá nhà, giữa số phòng ngủ với giá nhà, giữa số toilet với giá nhà.
    plt.plot(df_price['toilet'], df_price['price'], c='b', label='Toilet', linestyle='--', linewidth=3)
    plt.legend()
    plt.show()
    
    plt.plot(df_price['bedroom'], df_price['price'], c='brown', label='Bedroom', linestyle='-.', linewidth=3)
    plt.legend()
    plt.show()
    
    plt.plot(df_price['area'], df_price['price'], c='violet', label='Area', linestyle=':', linewidth=3)
    plt.legend()
    plt.show()
    
    # Vẽ biểu đồ so sánh giá nhà trung bình trên 1 m2 giữa các hình thức nhà (type_of_land).
    rect = plt.bar(ls_type, ls_mean, color='m', ec='k', linewidth='3', width=0.5)
    plt.bar_label(rect, padding=3)
    plt.xlabel("Type of land", fontsize=15, color='y', fontweight=800)
    plt.ylabel("1/(m^2)", fontsize=15, color='violet', fontweight=800)
    plt.title("average house price per square meter", fontsize=20, fontweight=1000, color='r')
    plt.show()
    
    # Vẽ biểu đồ thể hiện tỉ lệ % bài đăng (bản ghi) giữa các hình thức nhà (type_of_land).
    plt.pie(ls_value, labels=ls_key, autopct='%1.2f%%', pctdistance=0.8)
    plt.show()
    
    # Vẽ biểu đồ thể hiện sự thay đổi giá nhà trung bình trên 1m2 theo số lượng phòng ngủ.
    rect2 = plt.bar(ls_bed, ls_m, color='c', ec='k', linewidth='3', width=0.5)
    plt.bar_label(rect2, padding=3)
    plt.xlabel('Number of bedroom', fontsize=15, color='violet', fontweight=800)
    plt.ylabel('Price of mean in 1/m^2', fontsize=15, color='m', fontweight=800)
    plt.title('Price house', fontsize=20, fontweight=1000, color='r')
    plt.show()