import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('10.HypothesisTesting\data\FoodPrice_in_Turkey.csv')
    print(df.info())
    df_rice = df.loc[(df.ProductName=='Rice - Retail') & (df.Year == 2019)]
    
    # Giả thuyết không: Giá gạo trung bình = 9.5
    # Giả thuyết đối: Giá gạo trung bình != 9.5
    print(stats.ttest_1samp(df_rice.Price, 9.5))
