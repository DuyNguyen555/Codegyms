import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('01.overview/data/subset-covid-data.csv', encoding = 'utf-8')

    # print(data.head())

    # data.info()
    # print(data.shape)

    # Tìm hiểu xem dữ liệu được thống kê cho những ngày nào
    # print(data.date.value_counts())

    # lọc dữ liệu nhiễu:
    cleaned_data = data[data.date == '2020-04-12']
    # print(cleaned_data)

    # Vẽ biểu đồ phân bố số lượng ca mắc mới ở các quốc gia
    print ("trung bình số ca mắc mới: " + str(cleaned_data.cases.mean()))
    print ("trung vị của số ca mắc mới: "+ str(cleaned_data.cases.median()))
    # plt.hist(cleaned_data.cases, bins = 200)
    # plt.title("Phân bố số ca mắc mới")
    # plt.xlabel("số ca mắc mới")
    # plt.ylabel("Số lượng quốc gia")
    # plt.show()
    
    print ("5 quốc gia có số ca nhiễm mới cao nhất")
    data = data.sort_values('cases',ascending = False)
    print(data.head(5))
    
    print ("5 quốc gia có số ca tử vong cao nhất")
    data = data.sort_values('deaths',ascending = False)
    print(data.head(5))
    
    print("tổng số ca nhiễm và số ca của các châu lục")
    print(cleaned_data.groupby(['continent'])['cases', 'deaths'].sum())