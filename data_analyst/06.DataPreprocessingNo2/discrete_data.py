import pandas as pd
import numpy as np

if __name__ == '__main__':
    ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
    bins = [18, 25, 35, 60, 100]

    # thực hiện rời rạc hóa
    categorical = pd.cut(ages, bins)
    print(categorical)
    print("-"*80)

    # lấy ra index của nhóm tương ứng với các phần tử
    print(categorical.codes)
    print("-"*80)
    
    # lấy ra các nhóm
    print(categorical.categories)
    print("-"*80)
    
    # thống kê số lượng phần tử ở mỗi nhóm
    # print(categorical.value_counts())
    print(pd.value_counts(categorical))
    print("*"*80)
    
    print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))
    print("*"*80)
    
    # danh sách nhãn
    group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
    print(pd.cut(ages, bins, labels=group_names))
    
    data = np.random.rand(20)
    print(data)
    
    cut_data = pd.cut(data, 4, precision=2)
    print(cut_data)
    print()
    
    print(pd.value_counts(cut_data))
    print()
    
    # sinh ngẫu nhiễn 1000 điểm dữ liệu
    data = np.random.randn(1000)
    
    # thực hiện hàm qcut trên dữ liệu vừa sinh ra
    cats = pd.qcut(data, 4)
    print(cats)
    print()
    
    print(pd.value_counts(cats))
    print()

    print(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))