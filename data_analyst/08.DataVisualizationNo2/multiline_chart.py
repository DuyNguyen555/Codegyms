import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def vd1():
    y1 = np.random.normal(200, 30, size=100)
    y2 = np.random.normal(100, 80, size = 100)
    df = pd.DataFrame({'y1': y1, 'y2': y2, 'index': pd.date_range('1/1/2021', periods=100)})
    
    plt.plot(df.index, df['y1'], 'r-', label = 'line 1', linewidth=2)
    plt.plot(df.index, df['y2'], 'b-', label='line 2', linewidth=2)
    plt.legend(fontsize=12, loc=2)
    
    plt.xticks(fontsize = 12, rotation = 'horizontal')
    plt.yticks(fontsize=14)
    plt.title('multiline chart', fontsize =16)
    plt.xlabel('X axis', fontsize=12)
    plt.ylabel('Y axis', fontsize=12)
    plt.grid()
    plt.show()

def vd2():
    y1 = np.random.normal(1200, 30, size=20)
    y2 = np.random.normal(100, 10, size=20)
    df = pd.DataFrame({'y1': y1, 'y2': y2, 'index': pd.date_range('1/1/2021', periods=20)})
    
    plt.plot(df.index, df.y1, 'r', label='line 1', linewidth=2)
    axis1 = plt.gca()
    axis2 = axis1.twinx()
    axis2.plot(df.index, df.y2, 'b', label='line 2', linewidth=2)
    
    axis1.set_xlabel('X axis', fontsize=22)
    axis1.set_ylabel('Y axis 1', fontsize=20)
    axis2.set_ylabel('Y axis 2', fontsize=20)
    plt.legend(fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.title('A multiline chart with different Y axis', fontsize = 16)
    plt.show()

def vd3():
    x = ['Day 1','Day 2','Day 3','Day 4','Day 5','Day 6','Day 7','Day 8','Day 9','Day 10']
    y1 = [12.2, 16.3, 20.5, 25.4, 31.2, 24.2, 18, 13.5, 17.1, 21.7]
    y2 = [20.3, 27.6, 31.4, 33.7, 39.2, 33.4, 29.2, 25.7, 31.2, 36]
    y3 = [16.3, 17.6, 24.4, 26.7, 33.2, 29.4, 27.2, 24.7, 27.2, 32]
    
    fig, ax =plt.subplots(3, 1)
    ax[0].plot(x, y1, 'r',label = 'Object 1')
    ax[1].plot(x, y2, 'c',label ='Object 2')
    ax[2].plot(x, y3, 'm',label ='Object 3')
    
    ax[0].set_ylabel('Y axis 1')
    ax[1].set_ylabel('Y axis 2')
    ax[2].set_ylabel('Y axis 3')
    ax[2].set_xlabel('X axis')
    
    ax[0].legend(fontsize=10, loc ='lower right')
    ax[0].tick_params(axis='y', size=14)
    ax[0].set_xticklabels([])

    ax[1].legend(fontsize=10, loc='lower right')
    ax[1].tick_params(axis='y', size=14)
    ax[1].set_xticklabels([])
    
    ax[2].legend(fontsize=10, loc='lower right')
    ax[2].tick_params(axis='x', size=14)
    ax[2].tick_params(axis='y', size=14)
    
    plt.show()

if __name__ == '__main__':
    # vd1()
    # vd2()
    vd3()