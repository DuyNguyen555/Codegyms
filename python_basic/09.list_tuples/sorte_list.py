def list1():
    languages = ["PHP", "Python", "C#", "Java", "Android"]
    languages.sort()
    print(languages)
    languages.sort(reverse=True)
    print(languages)
    languages2 = languages.copy()
    languages.clear()
    print("List 1: " ,languages)
    print("List 2: " ,languages2)
    l3 = languages2.copy()
    del languages2
    # print("List 2: " ,languages2)
    print(l3)
    del_l = input()
    if del_l in l3:
        l3.remove(del_l)
    print(l3)
def myFunc(e):
    return len(e)

def myFunc2(e):
    return e['year']

if __name__ == "__main__":
    cars = ['BMW','Vinfast', 'Mercedes']
    cars2 = [
        {'car':'Ford','year':2005},
        {'car':'Mitsubishi','year':2000},
        {'car':'BMW','year':2021},
        {'car':'Cardilac','year':2019}
    ]
    print('Danh sach truoc khi sap xep')
    print(cars)
    cars.sort(key=myFunc)
    print('Danh sach sau khi sap xep')
    print(cars)
    
    print('Danh sach truoc khi sap xep')
    print(cars2)
    cars2.sort(key=myFunc2)
    print('Danh sach sau khi sap xep')
    print(cars2)
    