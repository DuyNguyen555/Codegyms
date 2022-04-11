
def check(BMI):
    check = "Béo phì cấp độ III" if BMI >= 40 else "Béo phì cấp độ II" if BMI < 40 and BMI >= 35 else "Béo phì cấp độ I" if BMI < 35 and BMI >= 30 else "Thừa cân" if BMI < 30 and BMI >= 25 else "Bình thường" if BMI < 25 and BMI >= 18.5 else "Gầy cấp độ I" if BMI < 18.5 and BMI >= 17 else "Gầy cấp độ II" if BMI < 17 and BMI >= 16 else  "Gầy cấp độ III" if BMI < 16 else 'Error'
    return check
def main():
    height = float(input("Enter the height: "))
    weight = float(input("Enter the weight: "))
    BMI = weight /(height*2)
    print(check(BMI))
if __name__ == '__main__':
    main()