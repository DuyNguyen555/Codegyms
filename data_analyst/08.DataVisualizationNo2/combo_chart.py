import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def vd1():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [12.2, 16.3, 20.5, 25.4, 31.2, 14.2, 24, 19.5, 28.1, 21.7]
    y2 = [2000, 4000, 1200, 3200, 5600, 2300, 3600, 2500, 3100, 3000]
    
    plt.bar(x, y2, color='c' ,label='line 2', width= 0.5, ec = 'k', linewidth=2)

    axes1 = plt.gca()
    axes2 = axes1.twinx()

    axes2.plot(x, y1, 'r-o', linewidth = 2)
    
    fig = plt.gcf()
    axes3 = fig.add_axes([0.2, 0.6, 0.25, 0.25])
    axes3.plot(x, y2)
    
    axes1.set_xlabel('X axis', fontsize =14)
    axes1.set_ylabel('Y axis 1', fontsize = 14)
    axes2.set_ylabel('Y axis 2', fontsize = 14)
    plt.legend()
    axes1.grid()
    plt.title('This is a Combo Chart', fontsize = 16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    axes1.tick_params(axis='x', size=10)
    axes1.tick_params(axis='y', size=10)
    axes2.tick_params(axis='y', size=10)
    
    plt.show()

def vd2():
    x = ['P1','P2','P3','P4','P5']
    y1 = [12.2, 16.3, 20.5, 25.4, 31.2]
    y2 = [20.3, 22.6, 31.4, 33.7, 39.2]
    y3 = [16.3, 17.6, 24.4, 26.7, 33.2]

    fig, ax = plt.subplots(2, 2)

    ax[0][0].bar(x, y1, label="Object 1", width=0.5, color='c', ec='k', lw=2)
    ax[1][0].bar(x, y2, label="Object 2", width=0.5, color='m', ec='k', lw=2)
    ax[0][1].pie(y1, labels = x, autopct='%1.2f%%', radius=1.3)
    ax[1][1].pie(y2, labels = x, autopct='%1.2f%%', radius=1.3)

    ax[0][0].set_ylabel('Y axis 1', fontsize=14)
    ax[1][0].set_ylabel('Y axis 2', fontsize=14)
    ax[1][0].set_xlabel('X axis 1', fontsize=14)

    ax[0][0].legend()
    ax[0][0].tick_params(axis='y', size=10)

    ax[1][0].legend()
    ax[1][0].tick_params(axis='y', size=10)

    plt.show()

if __name__ == '__main__':
    vd1()
    vd2()