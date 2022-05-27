import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

if __name__ == '__main__':
    df = pd.read_csv("06.DataPreprocessingNo2\data\Credit_Scoring.csv")

    df1 = df.fillna(0)
    df2 = df.interpolate()

    # sns.boxplot(data=df1)
    # plt.show()

    Q1 = df2['MonthlyIncome'].quantile(0.25)
    Q3 = df2['MonthlyIncome'].quantile(0.75)
    IQR = Q3 - Q1
    df3 = df2[~( (df2['MonthlyIncome'] < (Q1 - IQR * 1.5)) | (df2['MonthlyIncome'] > (Q3 + IQR * 1.5)) )]

    # df_cut1 = pd.qcut(df3['RevolvingUtilizationOfUnsecuredLines'], 4)
    # df_cut2 = pd.qcut(df3['DebtRatio'], 5)
    # df_cut3 = pd.qcut(df3['NumberOfOpenCreditLinesAndLoans'], 6)
    # print(pd.value_counts(df_cut1))
    # print(pd.value_counts(df_cut2))
    # print(pd.value_counts(df_cut3))
    
    bins = [0, 30, 40, 50, 80, 150]
    df_age = pd.cut(df3['age'], bins)
    print(pd.value_counts(df_age))