import pandas as pd
from scipy import stats

def price_order(data):
    if data < q1:
        return 1
    elif data >= q1 and data < q2:
        return 2
    elif data >= q2 and data < q3:
        return 3
    else:
        return 4

if __name__ == '__main__':
    df = pd.read_excel('11.CorrelationTesting\data\house_price_dống-da.xlsx')
    
    # Giữa giá nhà và diện tích có tương quan với nhau?
    # H0: a # b
    # H1: a = b
    df1 = df[['area', 'price']]
    df1.dropna(inplace=True)
    print("Area vs price:")
    print(stats.pearsonr(df1['area'], df1['price']))
    # Vì pvalue < 0.05 , hệ số tương quan là 0.16 nên giữa hai thuộc tính giá tiền và diện tích có sự tương quan yếu
    
    # Giữa giá nhà và tọa độ địa lý (lat, long) có tương quan với nhau
    df2 = df[['area', 'lat', 'long']]
    df2.dropna(inplace=True)
    print("Area vs lat, long:")
    print(stats.pearsonr(df2['area'], df2['lat']))
    print(stats.pearsonr(df2['area'], df2['long']))
    # Vì pvalue > 0.05 nên giữa thuộc tính không có tính quan với nhau
    
    # Giữa thuộc tính land_certificate và property_type có tương quan với nhau
    df3 = df.filter(['land_certificate', 'type_of_land'])
    values = {"land_certificate": "Không có"}
    df3.fillna(value=values, inplace=True)
    df3.dropna(inplace=True)
    contingency = pd.crosstab(df3['land_certificate'], df3['type_of_land'])
    # print(contingency)
    c, p, dof, expected = stats.chi2_contingency(contingency)
    print("land_certificate vs type_of_land:")
    print(p)
    # Vì pvalue < 5% nên giữa hai thuộc tính có sự tương quan với nhau
    
    # Hãy  mã hóa lại thuộc tính giá nhà theo đơn vị (nghìn đồng/m2) và sắp xếp giá nhà thành 4 mức tương ứng với các khoảng tứ phân vị. Tiến hành kiểm định tương quan giữa biến giá nhà này với các biến tọa độ vị trí (lat, long)
    df4 = df.filter(['area', 'price', 'lat', 'long'])
    df4.dropna(inplace=True)
    df4['million/1^m'] = df4.area * df4.price
    q1, q2, q3 = df4['million/1^m'].quantile(0.25), df4['million/1^m'].quantile(0.5), df4['million/1^m'].quantile(0.75)
    df4['price_order'] = df4['million/1^m'].apply(price_order)
    print("million/1^m vs lat, long:")
    print(stats.spearmanr(df4['million/1^m'], df4['lat']))
    print(stats.spearmanr(df4['million/1^m'], df4['long']))