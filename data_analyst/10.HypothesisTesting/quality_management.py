import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_excel('10.HypothesisTesting\data\Quality.xlsx')
    
    # Preprocessing
    sample = list()
    for i in df.columns:
        sample.extend(df[i].tolist())

    df = pd.DataFrame(columns=['sample'], data=sample)
    print(df.describe())
    
    # Tiến hành kiểm định về giá trị trung bình
    # Giả thuyết không: khối lượng trung bình của sản phẩm == 12
    # Giả thuyết đối: Khối lượng trung bình của sản phẩm != 12
    print(stats.ttest_1samp(sample, 12))
    # Kết luận: Tuyên bố của khách hàng về giá trị trung bình là đúng, nhưng tuyên bố về sai số của sản phẩm đang không hợp lý.