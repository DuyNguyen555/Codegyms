import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = ['2017', '2018', '2019', '2020', '2021']
    y = [234, 389, 333, 402, 451]
    plt.bar(x, y, width=0.5, bottom=100, align='center', color=['r', 'y','b','g', 'violet'], edgecolor='black', linewidth=3, tick_label=['Năm 1', 'Năm 2', 'Năm 3', 'Năm 4', 'Năm 5'])
    plt.title("Sản Lượng Vải Xuất Khẩu", fontsize=20, fontweight=100, color= "g")
    plt.xlabel("Năm", fontsize = 15, fontweight=60, color='b')
    plt.ylabel("Sản lượng(tấn)", fontsize = 15, fontweight=60, color='r')
    plt.show()