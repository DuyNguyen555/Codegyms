import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_excel('10.HypothesisTesting\data\Coca_cola_use.xlsx')
    # print(df.describe())
    
    # Tiến hành kiểm định
    # a1: Ohio
    # a2: Atlanta
    # Giả thuyết H0: a1 - a2 = 0
    # Giả thuyết H1 a1 - a2 > 0
    print(stats.ttest_ind(df['Ohio'], df['Atlanta'], equal_var=False, alternative='greater'))
    # statistic>0, pvalue>0.05 ==> Chấp nhận H0 và bác bỏ H1
    # ==> Kết luận: Không đủ căn cứ để kết luận rằng lượng tiêu thụ coca trung bình ở Ohio lớn hơn ở Atlanta