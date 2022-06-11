import pandas as pd
from scipy import stats

def population_order(population):
    global q1, q2, q3
    if population < q1:
        return 1
    elif population>=q1 and population <q2:
        return 2
    elif population>=q2 and population <q3:
        return 3
    else: 
        return 4

if __name__ == '__main__':
    df = pd.read_csv('11.CorrelationTesting\data\subset-covid-data.csv')
    
    # Có mối tương quan nào giữa dân số và số ca nhiễm bệnh hay không
    df1 = df.filter(['cases','population'])
    df1.dropna(inplace=True)
    
    print("Hệ số tương quan và pvalue tương ứng giữa dân số và số ca nhiễm bệnh là:\n", stats.pearsonr(df1['cases'], df1['population']))
    # Vì pvalue<0.05 và hệ số tương quan là 0.17 -> Giữa dân số và số ca nhiễm bệnh có sự tương quan yếu
    
    # Có mối tương quan nào giữa số ca mắc (cases) và số ca tử vong (deaths) hay không
    df2 = df.filter(['cases', 'deaths'])
    df2.dropna(inplace=True)
    
    print("Hệ số tương quan và pvalue tương ứng giữa số ca mắc và số ca tử vong là:\n", stats.pearsonr(df2['cases'], df2['deaths']))
    # Vì pvalue<0.05 và hệ số tương quan là 0.9 -> Giữa số ca mắc và số ca tử vong có sự tương quan mạnh
    
    # tiến hành tính các khoảng tứ phân vị của population
    q1, q2, q3  = df1.population.quantile(0.25), df1.population.quantile(0.5), df1.population.quantile(0.75)
    
    # tiến hành biến đổi population
    df1['population_ordinal']=df1.population.apply(population_order)
    
    # print(df1)
    r, pvalue = stats.spearmanr(df1.cases, df1.population_ordinal)
    print()
    print ("r: ", r, "; pvalue: ", pvalue)
    # Pvalue ~0, và r~0.5 chứng tỏ giữa thuộc tính population_ordinal và số ca nhiễm bệnh có tương quan với nhau.