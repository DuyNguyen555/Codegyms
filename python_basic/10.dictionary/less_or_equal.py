def PriceOfTheProduct(product, price) :
    for i in product:
        if product[i] <= price:
            print(i, ":", product[i])

if __name__ == '__main__':
    # Đề bài cho sẵn
    products = {
                'SMART WATCH': 550,
                'PHONE' : 1000,
                'PLAYSTATION': 500,
                'LAPTOP' : 1550,
                'MUSIC PLAYER' : 600,
                'TABLET' : 400 
            }

    # Nhập
    price = int(input('Enter the price: '))
    PriceOfTheProduct(products, price)