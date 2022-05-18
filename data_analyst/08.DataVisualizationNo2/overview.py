import matplotlib.pyplot as plt

def vd1():
    """Tạo biểu đồ gồm 2 đồ thị đường cùng tỉ lệ trục trên một Axes"""
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [12.2, 16.3, 20.5, 25.4, 31.2, 14.2, 24, 19.5, 28.1, 21.7]
    y2 = [20.3, 40.6, 12.4, 32.7, 56.2, 23.4, 36.2, 25.7, 31.2, 30]
    
    axes1 = plt.plot(x, y1)
    axes2 = plt.plot(x, y2)
    plt.title('This is Two Lines on a Chart')
    plt.show()
    return

def vd2():
    """Tạo biểu đồ đường và biểu đồ cột khác tỉ lệ trục Y trên cùng một Axes"""
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [12.2, 16.3, 20.5, 25.4, 31.2, 14.2, 24, 19.5, 28.1, 21.7]
    y2 = [2000, 4000, 1200, 3200, 5600, 2300, 3600, 2500, 3100, 3000]
    
    plt.bar(x, y2, label='line 2', width=0.5, color='c')
    axes1 = plt.gca()
    axes2 = axes1.twinx()
    axes2.plot(x, y1, label='line 1', linewidth=2, c='r',marker='o')
    
    axes1.set_xlabel('Category', fontsize=14)
    axes1.set_ylabel('Y axis 1', fontsize=14)
    axes2.set_ylabel('Y axis 2', fontsize=14)
    
    plt.legend(fontsize=10)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=10)
    plt.title('This is a Combo Chart', fontsize = 16)
    plt.show()

def vd3():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [12.2, 16.3, 20.5, 25.4, 31.2, 14.2, 24, 19.5, 28.1, 21.7]
    y2 = [2000, 4000, 1200, 3200, 5600, 2300, 3600, 2500, 3100, 3000]
    
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(x, y1, label='line 1', linewidth=2, c = 'r', marker = 'o', linestyle='--')
    ax[1].bar(x, y2, label='line 2', width = 0.5, ec = 'k', linewidth=2, color='m')
    
    ax[0].set_xlabel('Category 1', fontsize = 14)
    ax[0].set_ylabel('Y axis 1', fontsize = 14)
    ax[0].set_title("This is a line chart", fontsize = 14)
    
    ax[1].set_xlabel('Category 2', fontsize = 14)
    ax[1].set_ylabel('Y axis 2', fontsize = 14)
    ax[1].set_title("This is a bar chart", fontsize = 14)
    
    ax[0].legend()
    ax[0].tick_params(axis='x', size = 14)
    ax[0].tick_params(axis='y', size = 14)
    
    ax[1].legend()
    ax[1].tick_params(axis='x', size = 14)
    ax[1].tick_params(axis='y', size = 14)

    plt.show()

if __name__ == '__main__':
    vd3()