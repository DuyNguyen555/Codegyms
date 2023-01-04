class student():
    def __init__(self, infor_student):
        self.infor = infor_student
    
    def see_catalog(self):
        """Xem danh mục sinh viên"""
        print("*"*25)
        for i in self.infor:
            infor = self.infor[i]
            print(f"Id: {i}\nName: {infor['name']}\nDate of birth: {infor['date_of_birth']}\nNative land: {infor['native_land']}\nSpecialized: {infor['specialized']}\nClass: {infor['class_student']}")
            print("*"*25)
    
    def add_student(self, id, name, birth, native_land, specialized, class_student):
        """Thêm học sinh"""
        new_student = {id:{"name": name, "date_of_birth": birth, "native_land": native_land, "specialized": specialized, "class_student": class_student}}
        self.infor.update(new_student)
    
    def update_student(self, id):
        """Cập nhật thông tin sinh viên"""
        if id in self.infor:
            while True:
                print("Update information of student:\n"
                      "0: Close\n"
                      "1: Name\n"
                      "2: Date of birth\n"
                      "3: Native land\n"
                      "4:specialized\n"
                      "5:class_student"
                      )
                option = input("Choose: ")
                if option == "0":
                    break
                elif option == "1":
                    self.infor[id]["name"] = input("New name of student: ")
                elif option == "2":
                    self.infor[id]["date_of_birth"] = input("New student's date of birth: ")
                elif option == "3":
                    self.infor[id]["native_land"] = input("New student's native land: ")
                elif option == "4":
                    self.infor[id]["specialized"] = input("New student's specialized: ")
                elif option == "5":
                    self.infor[id]["class_student"] = input("New student's class student: ")
    
    def delete_student(self, id = None):
        """Xóa thông tin sinh viên"""
        if id == None:
            name =input("Enter delete name of student: ")
            for i in self.infor:
                if self.infor[i]["name"] == name:
                    del self.infor[i]
                    break
            else:
                print("No name of student in catalog")
        elif id  in self.infor:
            del self.infor[id]
        else:
            print("No id in catalog")
    
    def find_student(self, id = None):
        if id == None:
            name =input("Enter find name of student: ")
            for i in self.infor:
                if self.infor[i]["name"] == name:
                    print("+"*20,
                        f"\nId: {i}\nName: {self.infor[i]['name']}\nDate of birth: {self.infor[i]['date_of_birth']}\nNative land: {self.infor[i]['native_land']}\nSpecialized: {self.infor[i]['specialized']}\nClass: {self.infor[i]['class_student']}\n",
                        "+"*20)
                    break
            else:
                print("No name of student in catalog")
        elif id in self.infor:
            print("+"*20,
                f"\nId: {id}\nName: {self.infor[id]['name']}\nDate of birth: {self.infor[id]['date_of_birth']}\nNative land: {self.infor[id]['native_land']}\nSpecialized: {self.infor[id]['specialized']}\nClass: {self.infor[id]['class_student']}")
        else:
            print("No id in catalog")

    def sort_student(self):
        dict1 = {}
        for i in sorted(self.infor):
            dict1[i] = self.infor[i]
        del self.infor
        self.infor = dict1

if __name__ == "__main__":
    s1 = {
        124:{"name": "C", "date_of_birth": "03/01/2002", "native_land": "Ha Noi"  , "specialized" : "CNTT", "class_student" : "CT3"},
        123:{"name": "B", "date_of_birth": "02/01/2001", "native_land": "Sai Gon" , "specialized" : "CNTT", "class_student" : "CT2"},
        122:{"name": "A", "date_of_birth": "01/01/2000", "native_land": "Da Nang" , "specialized" : "CNTT", "class_student" : "CT1"},
        125:{"name": "D", "date_of_birth": "04/01/2003", "native_land": "Hue"     , "specialized" : "CNTT", "class_student" : "CT4"}
        }
    s = student(s1)
    s.add_student(126, "E", "05/01/2000", "Vinh Tau", "CNTT", "CT5")
    s.update_student(123)
    s.delete_student()
    s.find_student()
    s.sort_student()
    s.see_catalog()