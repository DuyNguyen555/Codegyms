import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def HeatMap():
    uniform_data = np.random.rand(10,12)
    # print(uniform_data)
    sns.heatmap(uniform_data, vmin=0, vmax=1)
    plt.show()

def BoxPlot(tips):
    sns.set(style="darkgrid")
    # Vẽ box plot theo chiều dọc được nhóm theo một biến phân loại:
    # sns.boxplot(x="day", y="total_bill", data=tips)
    
    # Vẽ box plot theo chiều dọc được nhóm theo hai biến phân loại:
    # sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set3")

    # Vẽ box plot theo chiều dọc được nhóm theo hai biến phân loại khi một số nhóm bị thiếu:
    sns.boxplot(x="day", y="total_bill", hue="time", data=tips, linewidth=2)
    
    plt.show()

def PairPlot(tips):
    sns.set(style="darkgrid")
    # sns.pairplot(tips, hue="sex")
    sns.pairplot(tips, hue="day")
    
    plt.show()
    
if __name__ == '__main__':
    tips = sns.load_dataset("tips")
    # HeatMap()
    # BoxPlot(tips)
    PairPlot(tips)