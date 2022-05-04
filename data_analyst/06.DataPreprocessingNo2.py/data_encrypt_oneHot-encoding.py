from numpy import asarray
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

if __name__ == '__main__':
    # Mã hóa bằng numpy
    data = asarray([['red'], ['red'], ['yellow'], ['green'], ['yellow']])
    print(data)
    encoder = OneHotEncoder(sparse=False)
    encoder = encoder.fit(data)
    print(encoder.categories_)
    onehot = encoder.transform(data)
    print(onehot)
    
    print("-"*50)
    
    # Mã hóa bằng pandas
    s = pd.Series(['red', 'red', 'yellow', 'green', 'yellow'])
    onehot2 = pd.get_dummies(s)
    print(onehot2)