import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

"""Xây dựng mô hình dự báo giá bán nhà mặt phố của HN trong quận Hoàng Mai"""

if __name__ == '__main__':
    df = pd.read_csv('00.Test\data\RoadSurfaceHouseTrading.csv')
    
    # Tiền xử lý dữ liệu
    df = df[df['ten_quan'] == 'Quận Hoàng Mai']
    feature = ['dien_tich', 'phong_ngu','so_tang', 'gia', 'gia_m2', 'mat_tien']
    df = df[feature]
    # print(df)
    
    # df.dropna(subset = ['dien_tich', 'phong_ngu', 'gia', 'gia_m2'], inplace=True)
    # values = {'so_tang': 1}
    # df.fillna(value=values, inplace=True)
    # print(df)
    
    df = pd.get_dummies(df)
    df.reset_index(drop = True, inplace=True)

    # Xét tương quan
    # print(df)
    print(df.corr()) # Loại bỏ các biến không liên quan
    # print(df)
    
    # Xử lý dữ liệu
    X = df.drop('gia', axis=1).values
    Y = df['gia'].values
    Y = Y.reshape(-1,1)
    
    # Chia dữ liệu
    X_train, X_test, y_train, y_test= train_test_split(X, Y, test_size=0.3, random_state=42)
    
    # Huấn luyện mô hình
    reg = LinearRegression().fit(X_train, y_train)
    # print(reg.coef_)
    # print(reg.intercept_)
    y_predict=reg.predict(X_test)
    # print(y_predict.shape)
    # print(X_test.shape)
    # print(y_test.shape)
    
    # Đánh giá mô hình
    mse = mean_squared_error(y_test, np.array(y_predict))
    mae = mean_absolute_error(y_test, np.array(y_predict))
    score = r2_score(y_test, y_predict)
    
    print("MSE(trung bình bình phương sai số):", mse)
    print("MAE(Trung bình của sai số tuyệt đối):", mae)
    print(score)
    
    # Dự đoán
    # plt.plot(y_predict, color='m', lw=2)
    # plt.xticks(())
    # plt.yticks(())
    # plt.show()