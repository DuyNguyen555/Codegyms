def trans(f):
    """chuyển đổi nhiệt độ f (Fehrenheit) sang Celsius"""
    return (f - 32)/1.8

def main():
    print(trans(140))
    
if __name__ == '__main__':
    main()