from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

if __name__ == '__main__':
    boston = load_boston()
    x = boston.data
    y = boston.target
    columns = boston.feature_names
    
    boston_df = pd.DataFrame(boston.data)
    boston_df.columns = columns
    print(boston_df)
    sns.boxplot(data = boston_df, x = "DIS")
    # plt.show()
    
    # fig, ax = plt.subplots(figsize=(16,8))
    # ax.scatter(boston_df['INDUS'], boston_df['TAX'])
    # ax.set_xlabel('Proportion of non-retail business acres per town')
    # ax.set_ylabel('Full-value property-tax rate per $10,000')
    # plt.show()
    
    # z-score
    z = np.abs(stats.zscore(boston_df))
    z = np.array(z)
    # # print(z)

    # Kiểm tra điểm z-score trên 3
    # threshold = 3
    # print(np.where(z > threshold))
    # print(z[55][1])
    
    # Chọn những dữ liệu có z-score dưới 3
    boston_df_1 = boston_df[(z < 3).all(axis=1)]
    print(boston_df_1)
    
    # IQR
    Q1 = boston_df.quantile(0.25)
    Q3 = boston_df.quantile(0.75)
    IQR = Q3 - Q1
    # print(IQR)
    # print((boston_df < (Q1 - 1.5 * IQR)) | (boston_df > (Q3 + 1.5 * IQR)))
    boston_df_2 = boston_df[~((boston_df < (Q1 - 1.5 * IQR)) | (boston_df > (Q3 + 1.5 * IQR))).any(axis=1)]
    print(boston_df_2)
    