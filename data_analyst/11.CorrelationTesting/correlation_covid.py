import pandas as pd
from scipy import stats

if __name__ == '__main__':
    df = pd.read_csv('11.CorrelationTesting\data\subset-covid-data.csv')
    
    # Có mối tương quan nào giữa dân số và số ca nhiễm bệnh hay không
    df1 = df.filter(['cases','population'])
    df1.dropna(inplace=True)
    r, pvalue = stats.pearsonr(df1.cases, df1.population)
    print("r: ", r, ";"," pvalue: ", pvalue)
    