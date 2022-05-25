import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def vd1():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [12.2, 16.3, 20.5, 25.4, 31.2, 14.2, 24, 19.5, 28.1, 21.7]
    y2 = [2000, 4000, 1200, 3200, 5600, 2300, 3600, 2500, 3100, 3000]
    
    plt.bar(x, y2, color='c', label='line 2', ec='k', linewidth=2, width=0.5)
    
    axes1 = plt.gca()
    axes2 = axes1.twinx()
    axes2.plot(x, y2, 'r-o', label='line1', linewidth=2)
    fig = plt.gcf()
    axes3 = fig.add_axes([0.1, 0.7, 0.2, 0.2])
    axes3.plot(x, y2)
    
    axes1.set_xlabel('X axis', fontsize=14)
    axes1.set_ylabel('Y axis 1', fontsize=14)
    axes2.set_ylabel('Y axis 2', fontsize=14)
    
    plt.legend()
    plt.title('This is a Combo Chart', fontsize = 16)
    plt.grid()
    axes2.grid()
    plt.show()



if __name__ == '__main__':
    vd1()