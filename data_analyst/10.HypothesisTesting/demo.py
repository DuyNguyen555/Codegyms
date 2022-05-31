from scipy.stats import ttest_1samp

def ex1():
    x =  [21.5, 24.5, 18.5, 17.2, 14.5, 23.2, 22.1, 20.5, 19.4, 18.1, 24.1, 18.5]
    tscore, pvalue = ttest_1samp(x, popmean=20)
    print(tscore, pvalue)

    tscore, pvalue = ttest_1samp(x, popmean=20, alternative='less')
    print(tscore, pvalue)


    tscore, pvalue = ttest_1samp(x, popmean=20, alternative='greater')
    print(tscore, pvalue)
    
if __name__ == '__main__':
    ex1()