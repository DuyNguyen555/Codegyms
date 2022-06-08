import pandas as pd
from scipy import stats

# Kiểm định:
# Trung bình GDP của các quốc gia trên thế giới là 500 tỉ usd/năm
# GDP trung bình ở các quốc gia ở châu Âu cao hơn châu Á không
# GDP trung bình của các quốc gia ở châu Âu và châu Mỹ là bằng nhau

if __name__ == '__main__':
    df = pd.read_csv("10.HypothesisTesting\data\GDPlist.csv")
    # print(df.describe())
    
    # Trung bình GDP của các quốc gia trên thế giới là 500 tỉ usd/năm
    # H0: y==500
    # H1: y!=500
    print(stats.ttest_1samp(df['GDP (millions of US$)'], 500))
    # pvalue < 0.05 -> Bác bỏ H0, chấp nhận H1.
    # Không đủ căn cứ để kết luận trung bình gdp của các quốc gia trên thế giới là 500 tỉ usd/năm
    
    # GDP trung bình ở các quốc gia ở châu Âu cao hơn châu Á không
    # H0: europe - asian = 0
    # H1: europe - asian > 0
    df_asian = df[(df['Continent'] == 'Asia')]
    df_europe = df[(df['Continent'] == 'Europe')]
    print(stats.ttest_ind(df_europe['GDP (millions of US$)'], df_asian['GDP (millions of US$)'], equal_var=False))
    # statistic<0, pvalue>0.05 --> Chấp nhận H0 và bác bỏ H1.
    # ==> Kết luận: Không đủ căn cứ để chứng minh GDP trung bình ở các quốc gia ở châu Âu cao hơn châu Á
    
    # GDP trung bình của các quốc gia ở châu Âu và châu Mỹ là bằng nhau
    df_americas = df.loc[(df.Continent.isin(['South America', 'North America']))]
    # H0: americas - europe == 0
    # H1: americas - europe != 0
    print(stats.ttest_ind(df_americas['GDP (millions of US$)'], df_europe['GDP (millions of US$)'], equal_var=False))
    # statistic>0, pvalue>0.05 --> Chấp nhận H0 và bác bỏ H1.
    # ==> Kết luận: GDP trung bình của các quốc gia ở châu Âu và châu Mỹ là bằng nhau
    
