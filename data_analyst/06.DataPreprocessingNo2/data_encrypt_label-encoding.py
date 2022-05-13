from sklearn.preprocessing import LabelEncoder
import pandas as pd

if __name__ == '__main__':
    
    # Mã hóa bằng sklearn
    encoder = LabelEncoder()
    lb = encoder.fit_transform(['red', 'red', 'yellow', 'green', 'yellow'])
    # print(lb)
    
    # Mã hóa bằng pandas
    s = pd.Series(['red', 'red', 'yellow', 'green', 'yellow'])
    # print(s.astype('category').cat.codes)
    
    data = ["red","yellow","green","red"]
    label_enc = LabelEncoder()
    label_enc = label_enc.fit(data)

    transform = label_enc.transform(data)

    print(transform)