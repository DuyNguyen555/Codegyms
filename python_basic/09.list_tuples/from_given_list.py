gadgets = ["Mobile", "Laptop", 100, "Camera",
           310.28, "Speakers", 27.00, "Television",
           1000, "Laptop Case", "Camera Lens"]

def sort(box):
    text = []
    number = []

    for i in box:
        if isinstance(i, str):
            text.append(i)
        else:
            number.append(i)

    print("Sắp xếp list chứa chuỗi theo thứ tự tăng dần:\n", sorted(text), "\n")
    print("Sắp xếp list chứa chuỗi theo thứ tự giảm dần: \n", sorted(text, reverse = True), "\n")
    print("Sắp xếp list chứa số theo thứ tự tăng dần:\n", sorted(number), "\n")
    print("Sắp xếp list chứa số theo thứ tự tăng dần:\n", sorted(number, reverse = True))

def main():
    sort(gadgets)

if __name__ == '__main__':
    main()