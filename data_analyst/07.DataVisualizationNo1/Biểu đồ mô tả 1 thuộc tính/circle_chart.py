import matplotlib.pyplot as plt

if __name__ == '__main__':
    labels = ['Gạo', 'Gas', 'Thịt', 'Trứng', 'Sữa']
    sizes = [443, 292, 231, 110, 20]
    plt.pie(sizes, labels=labels, autopct='%1.2f%%')
    plt.title('Sản lượng xuất khẩu năm 2021', fontsize = 10)
    plt.show()