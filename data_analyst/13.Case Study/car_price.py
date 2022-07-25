import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

def normalize(df):
    max_column = df.max()
    min_column = df.min()
    df_nor = (df - df.min()) / (df.max() - df.min())
    
    return max_column, min_column, df_nor

if __name__ == '__main__':
    df = pd.read_csv('13.Case Study\data\Case_study_CarPrice_Assignment.csv')
    # print(df.info())
    feature_process = ['car_ID', 'CarName', 'fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel',
                       'enginelocation', 'enginetype','cylindernumber', 'fuelsystem']
    
    # text -> number
    # for f in feature_process:
    #     data = df_tmp[f].to_list()
    #     uniq = set(data)
    #     for idx, name in enumerate(uniq):
    #         df_tmp[df_tmp[f] == name] = idx
            
    # Đánh giá, lựa chọn
    # pca = PCA(n_components=2)
    # result = pca.fit_transform(df_tmp)
    
    # Chọn lựa các feature
    # print(pd.DataFrame(pca.components_, columns=df_tmp.columns, index=['PC-1', 'PC-2']))
    # print(df.corr())
    # pd.DataFrame(df.corr()).to_csv('13.Case Study\data\Test.csv')

    
    df = df.drop(feature_process, axis=1)
    
    
    # 0-1
    # normalization
    max_column, min_column, df_nor = normalize(df)
    
    df_feature = df.loc[:, df.columns != 'price']
    target = df['price']
    
    # Xây dựng mô hình
    # Chuẩn bị đầu vào x, y
    x = df_nor.values.tolist()
    y = target.values.tolist()
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    
    reg = LinearRegression().fit(X_train, y_train)
    # print(reg.coef_)
    
    a = reg.coef_
    b = reg.intercept_
    
    pred = reg.predict(X_train)
    # print(mean_squared_error(y_train, pred))
    print(a)
    print(b)
    
    # Đánh giá mô hình
    mse = mean_squared_error(y_train, np.array(pred))
    mae = mean_absolute_error(y_train, np.array(pred))
    # print('mse',mse)
    # print('mae', mae)

    
    # Xử lý dữ liệu trc khi training mô hình