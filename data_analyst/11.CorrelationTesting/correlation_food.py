import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('11.CorrelationTesting\data\FoodPrice_in_Turkey.csv')

    # lọc dữ liệu gạo bán lẻ
    df_rice = df[(df.ProductName == "Rice - Retail") & (df.Place == "National Average")]
    df_rice['time'] = pd.to_datetime(df_rice['Year'].astype(str) + "/" + df_rice["Month"].astype(str))

    sns.set(style='darkgrid', palette='twilight')
    plt.plot(df_rice['time'], df_rice['Price'], 'b-*', lw=2, ms=10, mfc='r')
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Price', fontsize=14)

    plt.show()
    
    df_rice['time_processed'] = df_rice.Month + (df_rice.Year - 2013)*12
    plt.plot(df_rice['time_processed'], df_rice['Price'], 'c-*', lw=2, ms=12, mfc='r', mec='k')
    plt.show()
    
    print("Hệ số tương quan và pvalue tương ứng là:\n", stats.pearsonr(df_rice.time_processed, df_rice.Price))