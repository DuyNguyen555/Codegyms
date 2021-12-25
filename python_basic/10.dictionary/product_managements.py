def condition_id():
    """Hàm này để kiểm tra nhập id đúng mã tùy công ty"""
    while True:
        id_product = input("Id of the product: ")
        if id_product.isdigit() == True:
            id = int(id_product)
            if id >= 1000 and id < 10000:
                break
    return id

def condition_price():
    """Hàm này để kiểm tra tiền có phải dạng số không"""
    while True:                
        price = str(input("Price of the product: "))
        if price.isdigit() == True:
            break
    return price

def add_product(id, item, product):
    """Hàm này để thêm sản phẩm vào kho"""
    if id in product:
        infor = product[id]
        print(f"There is already a product:\nid:{id}; name: {infor['name']}; price: {infor['price']}VND\n")
    else:
        product.update(item)
        print()

def update_product(id, item, product):
    """Hàm này để cập nhật sản phẩm trong kho"""
    if id in product:
        product[id]['name'] = item[id]['name']
        product[id]['price'] = item[id]['price'] 
    else:
        add_product(id, item, product)

def del_product(id, product):
    """Hàm này để xóa sản phẩm trong kho"""
    del product[id]

if __name__ == '__main__':
    # Thông tin hàng cho sẵn
    product={
        1000:dict(name='milk',  price='50000' ),
        1001:dict(name='beef',  price='300000'),
        1002:dict(name='fish',  price='250000'),
        1003:dict(name='rice',  price='350000'),
        1004:dict(name='candy', price='5000'  ),
        1005:dict(name='duck',  price='100000'),
        1006:dict(name='pork',  price='220000')
    }

    # Điều kiện nhập
    condition = ["1", "2", "3", "4"]
    while True:
        while True:
            print("Option:\n"
                "1.Add product\n"
                "2.Update product\n"
                "3.Remove product\n"
                "4.Exit")
            # Chọn điều bạn muốn lằm
            option = str(input('Your select: '))
            if option in condition:
                break
            else:
                print()

        # Thêm sản phẩm
        if option == "1":
            id_product = condition_id()
            name_product = input("Enter name the product you want: ")
            price_product = condition_price()
            items = {id_product: dict(name=name_product, price=price_product)}
            add_product(id_product, items, product)
        # Cập nhật sản phẩm
        elif option == "2":
            id_product = condition_id()
            name_product = input("Enter name the product you want: ")
            price_product = condition_price()
            items = {id_product: dict(name=name_product, price=price_product)}
            update_product(id_product, items, product)
        # Xóa sản phẩm
        elif option == "3":
            id_product = condition_id()
            del_product(id_product, product)
        # Thoát chương trình
        else:
            for i in product:
                infor = product[i]
                print(f"id:{i}; name: {infor['name']}; price: {infor['price']}VND")
            break