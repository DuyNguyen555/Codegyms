import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Vẽ biểu đồ so sánh phân phối giá (triệu đ/m2) giữa nhà Phố và Nhà ngõ
# Kiểm định giả thuyết giá (triệu đ/m2) nhà mặt phố cao hơn giá nhà trong ngõ với mức ý nghĩa 5%
# Giá của những căn nhà không có thông tin về giấy tờ pháp lý thấp hơn giá nhà những căn có thông tin về giấy tờ pháp lý với mức ý nghĩa 5%

if __name__ == '__main__':
    df = pd.read_excel('10.HypothesisTesting\data\house_price_dống-da.xlsx')
    # print(df.describe())

    # Preprocessing
    df.dropna(subset=['area', 'price'], inplace=True)
    values = {'land_certificate': "Không có"}
    df.fillna(value=values, inplace=True)
    df['million/m^2'] = df['area'] * df['price']
    
    # Vẽ biểu đồ so sánh phân phối giá (triệu đ/m2) giữa nhà Phố và Nhà ngõ
    df1 = df[['type_of_land', 'million/m^2']]
    df1 = df1.loc[(df.type_of_land.isin(['Bán nhà riêng', 'Bán nhà mặt phố']))]
    
    sns.violinplot(x='type_of_land', y='million/m^2', data=df1)
    # plt.show()
    
    # Kiểm định giả thuyết giá (triệu đ/m2) nhà mặt phố cao hơn giá nhà trong ngõ với mức ý nghĩa 5%
    df11 = df1[(df1['type_of_land'] == 'Bán nhà riêng')]
    df12 = df1[(df1['type_of_land'] == 'Bán nhà mặt phố')]
    
    # H0: n2 - n1 = 0
    # H1: n2 - n1 > 0
    print(stats.ttest_ind(df12['million/m^2'], df11['million/m^2'], equal_var=False))
    # --> s>0, p>5% -> Chấp nhận H0, Bác bỏ H1
    # ==> Kết luận: Không có căn cứ chứng minh nhà mặt phố cao hơn giá nhà trong ngõ.
    
    # Giá của những căn nhà không có thông tin về giấy tờ pháp lý thấp hơn giá nhà những căn có thông tin về giấy tờ pháp lý với mức ý nghĩa 5%
    df2 = df[['land_certificate', 'million/m^2']]
    
    df21 = df2[(df2['land_certificate'])=='Sổ đỏ']
    df22 = df2[(df2['land_certificate'])=='Không có']
    
    # H0: n2 - n1 == 0
    # H1: n2 - n1 < 0
    print(stats.ttest_ind(df22['million/m^2'], df21['million/m^2'], equal_var=False))
    # s>0, p>0.05 --> Chấp nhận H0, bác bỏ H1
    # Kết luận: Không có căn cứ chứng minh giá của những căn nhà không có thông tin về giấy tờ pháp lý thấp hơn giá nhà những căn có thông tin về giấy tờ pháp lý.