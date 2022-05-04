from sklearn.preprocessing import LabelEncoder
import pandas as pd

if __name__ == '__main__':
    
    # Mã hóa bằng sklearn
    encoder = LabelEncoder()
    lb = encoder.fit_transform(['red', 'red', 'yellow', 'green', 'yellow'])
    print(lb)
    
    # Mã hóa bằng python
    s = pd.Series(['red', 'red', 'yellow', 'green', 'yellow'])
    print(s.astype('category').cat.codes)
    