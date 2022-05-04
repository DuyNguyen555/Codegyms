from sklearn.preprocessing import OrdinalEncoder

if __name__ == '__main__':
    enc = OrdinalEncoder()
    X = [['Male', 1], ['Female', 3], ['Female', 4], ['Female', 2], ['Male', 5]]
    
    arr = enc.fit(X)
    print(arr.categories_)
    
    matrix = enc.transform(X)
    print(matrix)
    
    print(enc.inverse_transform([[1, 0], [0, 1], [0,2]]))