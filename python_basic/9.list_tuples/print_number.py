def number():
    text = ("không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín")
    num = input("Input number: ")
    for i in num:
        print(text[int(i)], end =' ')

def main():
    number()
    
if main():
    main()