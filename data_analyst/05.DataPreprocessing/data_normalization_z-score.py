import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


if __name__ == '__main__':
    # tạo các cột theo các phần phối khác nhau
    df = pd.DataFrame({ 
    'beta': np.random.beta(5, 1, 1000) * 60,        # beta
    'exponential': np.random.exponential(10, 1000), # exponential
    'normal_p': np.random.normal(10, 2, 1000),      # normal platykurtic
    'normal_l': np.random.normal(10, 10, 1000),     # normal leptokurtic
})
    
    first_half = np.random.normal(20, 3, 500) 
    second_half = np.random.normal(-20, 3, 500) 
    bimodal = np.concatenate([first_half, second_half])
    df['bimodal'] = bimodal
    # sns.kdeplot(data=df)
    df.describe()

    normal_big = np.random.normal(1000000, 10000, (1000,1))  # normal distribution of large values
    df['normal_big'] = normal_big
    # sns.kdeplot(data=df)

    df.boxplot()
    plt.show()
    
    s_scaler = StandardScaler()

    df_s = s_scaler.fit_transform(df)
    col_names = list(df.columns)
    df_s = pd.DataFrame(df_s, columns=col_names)
    # sns.kdeplot(data=df_s)
    df_s.boxplot()
    plt.show()
    
    