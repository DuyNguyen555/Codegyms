# Nhập vào một chuỗi ký tự
# Kiểm tra nếu chuỗi đó bằng "python" thì dừng

string = "python"
text = str(input("Nhập vào một chuỗi ký tự: "))

while True:
    text_ = text.lower()
    if string in text_:
        print("True")
        break
    elif text_ == "close":
        print("Close")
        break
    else:
        text = str(input("Nhập lại: "))
