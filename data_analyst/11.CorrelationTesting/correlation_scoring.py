import pandas as pd
from scipy import stats

def MonthlyIncome_order(data):
    if data < q1:
        return 1
    elif data >= q1 and data < q2:
        return 2
    elif data >= q2 and data < q3:
        return 3
    else:
        return 4

if __name__ == '__main__':
    df = pd.read_csv('11.CorrelationTesting\data\Credit_Scoring.csv')

    # Giữa độ tuổi (age) và thu nhập trung bình theo tháng (MonthlyIncome) có tương quan với nhau hay không?
    d1 = df.filter(['age', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans'])
    d1.dropna(inplace=True)
    print("Age vs MonthlyIncome:")
    print(stats.pearsonr(d1['age'], d1['MonthlyIncome']))
    # Vì pvalue > 5% và hệ số tương quan = 0.038 nên giữa hai thuộc tính có sự tương quan yếu
    
    # Giữa số lượng khoản vay (NumberOfOpenCreditLinesAndLoans) và độ tuổi có tương quan với nhau không
    print("NumberOfOpenCreditLinesAndLoans vs age:")
    print(stats.pearsonr(d1['NumberOfOpenCreditLinesAndLoans'], d1['age']))
    
    # Giữa (số lượng người phụ thuộc) NumberOfDependents và thu nhập theo tháng (MonthlyIncome) có tương quan với nhau hay không
    d2 = df.filter(['NumberOfDependents', 'MonthlyIncome'])
    d2.dropna(inplace=True)
    print('NumberOfDependents vs MonthlyIncome:')
    print(stats.pearsonr(d2['NumberOfDependents'], d2['MonthlyIncome']))
    # Vì pvalue < 5% và hệ số tương quan = 0.06 nên giữa hai thuộc tính có sự tương quan yếu
    
    # Mã hóa lại thuộc tính MonthlyIncome thành thuộc tính MonthlyIncome_order theo các khoảng tứ phân vị, giữa thuộc tính mới này và tình trạng nợ xấu trong 2 năm trở lại đây (SeriousDlqin2yrs) có liên quan tới nhau không
    d3 = df.filter(['MonthlyIncome', 'SeriousDlqin2yrs'])
    d3.dropna(inplace=True)
    q1, q2, q3 = d3.MonthlyIncome.quantile(0.25), d3.MonthlyIncome.quantile(0.5), d3.MonthlyIncome.quantile(0.75)
    d3['MonthlyIncome_order'] = d3['MonthlyIncome'].apply(MonthlyIncome_order)
    print("MonthlyIncome_order vs SeriousDlqin2yrs:")
    print(stats.spearmanr(d3['SeriousDlqin2yrs'], d3['MonthlyIncome_order']))
    # Vì pvalue < 0.05 và hệ số tương quan = -0.06 nên giữa hai thuộc tính có sự tương quan yếu
    
    # Giữa thuộc tính MonthlyIncome_order với thuộc tính tỉ lệ số dư tài khoản (RevolvingUtilizationOfUnsecuredLines) có mối liên hệ với nhau không
    d4 = df.filter(['MonthlyIncome', 'RevolvingUtilizationOfUnsecuredLines'])
    d4.dropna(inplace=True)
    q1, q2, q3 = d4.MonthlyIncome.quantile(0.25), d4.MonthlyIncome.quantile(0.5), d4.MonthlyIncome.quantile(0.75)
    d4['MonthlyIncome_order'] = d4['MonthlyIncome'].apply(MonthlyIncome_order)
    print("MonthlyIncome_order vs RevolvingUtilizationOfUnsecuredLines:")
    print(stats.spearmanr(d4['RevolvingUtilizationOfUnsecuredLines'], d4['MonthlyIncome_order']))
    # Vì pvalue < 0.05 và hệ số tương quan = -0.08 nên giữa hai thuộc tính có sự tương quan yếu
    