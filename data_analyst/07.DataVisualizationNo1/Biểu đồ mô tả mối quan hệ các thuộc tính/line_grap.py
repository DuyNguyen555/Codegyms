import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [3, 5, 9, 7, 13, 15, 20, 17, 18, 13]
    y2 = [2, 7,12, 17, 14, 17,18, 23, 22, 28]
    plt.plot(x, y1, linewidth=3, marker="o", markersize=8, color='r', linestyle='--', label="line 1")
    plt.plot(x, y2, linewidth=3, marker="s", markersize=7, color='c', linestyle=':', label='line 2')
    plt.show()