import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Giữa giá gạo ở National Average và thời gian có mối liên hệ với nhau hay không
if __name__ == '__main__':
    df = pd.read_csv('11.CorrelationTesting\data\FoodPrice_in_Turkey.csv')
    print(df.describe())
    
    # lọc dữ liệu gạo bán lẻ
    df_rice = df[(df.ProductName == "Rice - Retail") & (df.Place == "National Average")]
    df_rice['time'] = pd.to_datetime(df['Year'].astype(str) + "/" + df['Month'].astype(str))
    df_rice['time_processed'] = df_rice.Month + (df_rice.Year - 2013)*12
    
    # H0: r = 0
    # H1: r # 0
    print("Hệ số tương quan và pvalue tương ứng là:\n", stats.pearsonr(df_rice['time_processed'], df_rice['Price']))
    # Vì pvalue <, hệ số tương quan=0.88 nên giữa giá gạo và thời gian có tương quan với nhau
    
    sns.set(style='darkgrid')
    fig, ax = plt.subplots(2,1)
    ax[0].plot(df_rice['time'], df_rice['Price'], 'c-*', lw=3, ms=11, mfc='r', mew=1, mec='b')
    ax[1].plot(df_rice['time_processed'], df_rice['Price'], 'm-*', lw=3, ms=11, mfc='r', mew=1, mec='k')
    
    plt.show()