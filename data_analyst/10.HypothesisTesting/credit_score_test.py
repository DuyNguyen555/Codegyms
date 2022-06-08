import pandas as pd
from scipy import stats

# Có phải những khách hàng không có người phụ thuộc sẽ có thu nhập trung bình theo tháng (MonthlyIncome) nhỏ hơn những khách hàng có người phụ thuộc không (với mức ý nghĩa 10%)

# Có phải trung bình số lượng khoản vay (NumberOfOpenCreditLinesAndLoans) những khách hàng gặp khó khăn trong vòng 2 năm trở lại đây (SeriousDlqin2yrs =1) thì sẽ cao hơn những khách hàng không gặp khó khăn không với mức ý nghĩa 10%

if __name__ == '__main__':
    df = pd.read_csv('10.HypothesisTesting\data\Credit_Scoring.csv')
    
    # Có phải những khách hàng không có người phụ thuộc sẽ có thu nhập trung bình theo tháng (MonthlyIncome) nhỏ hơn những khách hàng có người phụ thuộc không (với mức ý nghĩa 10%)
    df1 = df[['MonthlyIncome', 'NumberOfDependents']]
    values={'NumberOfDependents': 0}
    df1.fillna(value=values, inplace=True)
    df1.dropna(inplace=True)
    
    # không có người phụ thuộc
    df11 = df1[(df1['NumberOfDependents'] == 0)]
    
    # có người phụ thuộc
    df12 = df1[(df1['NumberOfDependents'] != 0)]

    # H0: n1 - n2 = 0
    # H1: n1 - n2 < 0
    print(stats.ttest_ind(df11['MonthlyIncome'], df12['MonthlyIncome'], equal_var=False))
    # s<0, p<10% --> Bác bỏ H0, chấp nhận H1
    # Kết luận ==> Những khách hàng không có người phụ thuộc sẽ có thu nhập trung bình theo tháng (MonthlyIncome) nhỏ hơn những khách hàng có người phụ thuộc