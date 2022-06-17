import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

def impute_median(series):
    """Define function to impute series with it's median"""
    return series.fillna(series.median())

if __name__ == '__main__':
    df = pd.read_csv('12.LinearRegression\data\AmesHousing.csv')
    # print(df.head())
    # print(df.shape)
    #Since Regression needs numerical features,convert categorical columns into dummy variables
    df1 = pd.get_dummies(df)
    # print(df1.head())
    # print(df.shape)
    
    # print(df1.columns[df1.isna().any()].tolist())
    # print(df1.isna().sum())
    # print(df1)
    
    lis = df1.columns[df1.isna().any()].tolist()
    for i in lis:
        if i == 'Garage Yr Blt':
            continue
        df1[i] = df1[i].transform(impute_median)
    
    
    df2 = df1.drop('Garage Yr Blt', axis=1)
    y = df2['SalePrice'].values
    
    X = df2.drop('SalePrice', axis=1).values
    
    # print(X.shape)
    # print(y.shape)
    y = y.reshape(-1,1)

    #Split the arrays into training and testing data sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    #Create a regressor object
    LR= LinearRegression()

    #Fit training set to the regressor
    LR.fit(X_train,y_train)

    #print("Mô hình hồi quy tuyến tính đã được huấn luyện, có các tham số:")
    #print("Intercept =", LR.intercept_)
    #print("Coefficients:", LR.coef_)
    
    y_prediction = LR.predict(X_test)
    
    # Caculate R2-score
    score = r2_score(y_test, y_prediction)
    print("R2-score:", score)
    print("Mean_sqrd_error is ==", mean_squared_error(y_test, y_prediction))
    print('Root_mean_squared error of is == ',np.sqrt(mean_squared_error(y_test,y_prediction)))