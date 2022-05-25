import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ex1(tips):
    """Biểu đồ xu hướng"""
    sns.set(style="whitegrid",  palette="magma")
    # sns.lmplot(x="total_bill",y="tip", hue="smoker", data=tips)
    # sns.lmplot(x="total_bill",y="tip", col="smoker", data=tips)
    sns.lmplot(x="total_bill", y="tip", row="sex", col="time", data=tips)
    plt.show()

def ex2(tips):
    """Biểu đồ phân bố"""
    sns.set(style="whitegrid")
    
    # Vẽ biểu đồ phân bố cho thuộc tính total_bill:
    # sns.violinplot(y=tips["total_bill"], palette="coolwarm")
    
    # Vẽ violin plot được nhóm theo biến 1 biến phân loại là ngày:
    # ax = sns.violinplot(x="day", y="total_bill", data=tips)
    
    # Vẽ violin plot được nhóm theo biến 2 biến phân loại:
    # ax = sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips, palette="muted")
    
    # Vẽ violin plot được chia 2 phần để so sánh giữa các biến:
    # ax = sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips, palette="muted", split=True)
    
    # Kiểm soát thứ tự các violin plot bằng cách truyền một thứ tự nhãn cụ thể:
    ax = sns.violinplot(x="time", y="tip", data=tips, order=["Dinner", "Lunch"])
    
    plt.show()

def ex3(tips):
    """Biểu đồ tần số"""
    sns.set(style="darkgrid")
    
    # Hiển thị tần số của mỗi loại giới tính trong bộ dữ liệu:
    # sns.countplot(x="sex", data=tips)

    # Hiển thị số lượng giá trị cho hai biến phân loại:
    # sns.countplot(x="sex", data=tips, hue="smoker")
    
    # Vẽ các thanh theo chiều ngang
    sns.countplot(y="sex", data=tips, hue="smoker")
    
    plt.show()
    

if __name__ == '__main__':
    tips = sns.load_dataset("tips")
    # ex1(tips)
    # ex2(tips)
    ex3(tips)
    