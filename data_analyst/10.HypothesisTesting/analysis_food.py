import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    df = pd.read_csv('10.HypothesisTesting\data\FoodPrice_in_Turkey.csv')
    df_rice = df.loc[(df.ProductName=='Rice - Retail') & (df.Year == 2019)]
    df_wheat = df.loc[(df.ProductName== 'Wheat flour - Retail') & (df.Year == 2019)]
    
    # 1. Với mức ý nghĩa 5% hay kiểm định giả thuyết: giá bán lẻ gạo trung bình năm 2019 là 9.5 (Lira)/1 kg Turkish Lira
    # Giả thuyết không H0: Giá gạo trung bình = 9.5
    # Giả thuyết đối H1: Giá gạo trung bình != 9.5
    print(stats.ttest_1samp(df_rice.Price, 9.5))
    # Vì pvalue = 0.24 > 5% nên chấp nhận giả thuyết H0 bác bỏ H1
    # Kết luận: Giá gạo trung bình năm 2019 là 9.5 (lira)/kg
    
    # 2. Với mức ý nghĩa 5% hãy kiểm định giả thuyết: Giá bột mỳ và giá gạo ở Turkey năm 2019 là bằng nhau
    # Giả thuyết không H0: Giá bột mỳ == Giá gạo
    # Giả thuyết đối H1: Giá bột mỳ != Giá gạo
    price = {'rice': list(df_rice["Price"]), 'wheat': list(df_wheat['Price'])}
    print(stats.ttest_ind(price['rice'], price['wheat'], equal_var=False))
    # Vì pvalue = 7*11*10^-55 < 5% nên bác bỏ giả thuyết H0 và chấp nhận H1
    # Kết luận: giá bột mỳ và giá gạo trung bình năm 2019 là khác nhau

    del (df_rice, df_wheat, price)
    
    # 3. Vẽ biểu đồ sự biến đổi giá gạo trung bình từ năm 1/2014 đến năm 1/2019 và tìm mối liên hệ giữa giá Trà và giá Cà phê
    df['time'] = pd.to_datetime(df['Year'].astype(str) + "/" + df['Month'].astype(str))
    df_tea = df.loc[(df.ProductName == 'Tea - Retail')]
    df_coffee = df.loc[(df.ProductName == 'Coffee - Retail')]
    
    gr_tea = df_tea.groupby('time')['Price'].mean()
    gr_coffee = df_coffee.groupby('time')['Price'].mean()
    
    plt.plot_date(gr_tea.index, gr_tea.values, 'c-o')
    plt.plot_date(gr_coffee.index, gr_coffee.values, 'm-o')
    
    plt.show()
    
    df_tea_and_coffee = df.loc[(df.ProductName.isin(['Tea - Retail', 'Coffee - Retail']))]
    df_tea_and_coffee['time-place'] = df_tea_and_coffee['time'].astype(str) + '-' + df_tea_and_coffee['Place'].astype(str)

    df1 = df_tea_and_coffee[df_tea_and_coffee.ProductName == 'Tea - Retail'].filter(['time-place', 'Price'])
    df1.rename(columns={'Price': 'Tea - Retail'}, inplace=True)
    
    df2 = df_tea_and_coffee[df_tea_and_coffee.ProductName == 'Coffee - Retail'].filter(['time-place', 'Price'])
    df2.rename(columns={'Price': 'Coffee - Retail'}, inplace=True)
    processed_data = pd.merge(df1, df2, on='time-place')
    
    # Tiến hành kiểm định: Thực hiện kiểm định wilcoxon 1 phía với giả thuyết như sau
    # Giả thuyết không: giá cà phê bằng giá trà công thêm 15 Lira ở mọi thời điểm
    # Giả thuyết đối: Giá giá cà phê luôn hơn giá trà 15 Lira ở mọi thời điểm
    
    d = processed_data['Coffee - Retail'] - processed_data['Tea - Retail'] - 15
    print(stats.wilcoxon(d, alternative='greater'))