import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
from sklearn.metrics import r2_score
import pickle # thư viện  giúp lưu trữ mô hình

if __name__ == '__main__':
    dataset = pd.read_csv('12.LinearRegression\data\salary_data.csv')
    dataset.plot(x='SoNamKinhNghiem', y='Luong', style='o')
    plt.title('Số năm kinh nghiệm - lương')
    plt.xlabel('Số năm kinh nghiệm')
    plt.ylabel("Lương")
    plt.show()
    
    df_keToan = dataset[dataset["NganhNghe"] == "KeToan"]
    df_hcnh = dataset[dataset["NganhNghe"] == "HCNS"]
    df_sale = dataset[dataset["NganhNghe"] == "Sale"]

    print ("Kết cấu bộ dữ liệu")
    print ("Số lượng mẫu nhân viên kế toán: " + str(df_keToan.shape[0]))
    print ("Số lượng mẫu nhân viên HCNH: " + str(df_hcnh.shape[0]))
    print ("Số lượng mẫu nhân viên SALE: " + str(df_sale.shape[0]))
    
    n_by_nganhNghe = dataset.groupby("NganhNghe")["Luong"].mean()
    print(n_by_nganhNghe)
    
    # plt.boxplot(df_keToan['Luong'])
    # plt.show()
    
    # Xây dựng model dự đoán tiền lương theo số năm kinh nghiệm
    X = dataset['SoNamKinhNghiem'].values.reshape(-1,1)
    Y = dataset['Luong'].values.reshape(-1,1)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    
    # Khai báo mô hình hồi quy tuyến tính
    regressor = LinearRegression()
    
    # Huấn luyện mô hình
    regressor.fit(X_train, y_train)
    
    print("Mô hình hồi quy sẽ có dạng: Lương = a + b * số năm kinh nghiệm \nvới các hệ số a và b lần lượt là:")
    print(regressor.intercept_)
    # For retrieving the slope
    print(regressor.coef_)
    
    # Đánh giá mô hình
    
    y_pred = regressor.predict(X_test) # dự đoán trên số năm kinh nghiệm của bộ dữ liệu test
    
    # Tính toán R2 của model
    r2_train = r2_score(y_train, regressor.predict(X_train))
    print("R2 trên tập huấn luyện của model là: " + str(r2_train))
    r2_test = r2_score(y_test, y_pred)
    print("R2 trên tập kiểm tra của model là:" + str(r2_test))
    
    df = pd.DataFrame({'số năm kinh nghiệm': X_test.flatten(), 'Lương Thực tế': y_test.flatten(), 'Lương Dự báo': y_pred.flatten()})
    print()
    print("Đánh giá năng lực dự báo trung bình trên tập test")
    print("Sai số dự báo trung bình:", metrics.mean_absolute_error(y_test, y_pred))
    
    plt.scatter(X_test, y_test,  color='gray')
    plt.plot(X_test, y_pred, color='red', linewidth=2)
    plt.show()
    
    # lưu trữ mô hình vào máy tính
    filename = '12.LinearRegression\model.sav'
    pickle.dump(regressor, open(filename, 'wb'))

    # Some time later.....
    # sử dụng mô hình
    #loaded_model = LinearRegression()
    loaded_model = pickle.load(open(filename, 'rb'))
    x = [[1],[2],[4]]
    y_pred = loaded_model.predict(x)
    print(y_pred)