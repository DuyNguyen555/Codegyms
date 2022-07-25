import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv('12.LinearRegression\data\Advertising.csv')
    
    fig, ax = plt.subplots(3, 1)
    ax[0].scatter(df['Sales'], df['TV'], color='m')
    ax[0].set_ylabel('TV', fontsize=14)
    
    ax[1].scatter(df['Sales'], df['Radio'], color='c')
    ax[1].set_ylabel('Ratio', fontsize=14)
    
    ax[2].scatter(df['Sales'], df['Newspaper'], color='skyblue')
    ax[2].set_ylabel('Newspaper', fontsize=14)
    ax[2].set_xlabel('Sales', fontsize=14)
    
    # plt.show()
    
    y = df['Sales'].values
    y = y.reshape(-1, 1)
    X = df.drop('Sales', axis=1).values

    X_train, X_test,y_train, y_test= train_test_split(X,y,test_size=0.3,random_state=42)
    
    #Create a regressor object
    LR = LinearRegression()

    # Xây dựng mô hình hồi quy tuyến tính đa biến với biến dự báo là lượng hàng bán ra, các biến đầu vào là chi phí cho cả 3 loại hình quảng cáo. Đánh giá mô hình.
    
    #Fit training set to the regressor
    LR.fit(X_train,y_train)
    
    print("Intercept:", LR.intercept_)
    print("Coefficients:", LR.coef_)
    
    y_prediction = LR.predict(X_test)
    score = r2_score(y_test,y_prediction)
    
    print('R2-score:',score)
    print('Mean_sqrd_error:',mean_squared_error(y_test, y_prediction))
    print('Root_mean_squared error:', np.sqrt(mean_squared_error(y_test, y_prediction)))