def GetEmployeeInformation(id):
    if id in employee_database:
        result = True
        return employee_database[id]
    else:
        print(f"{id} doesn't exist")
        result = False

def GetEmployeeDepartment(dept):
    if dept in department_database:
        return department_database[dept]
    else:
        return "doesn't exist"

def DisplayEmployData(data):
    for key, value in data.items():
        if key == 'dept':
            print(f"{key} : {GetEmployeeDepartment(value)}")
        else:
            print(f"{key} : {value}")
            

if __name__ == '__main__':
    # Thông tin nhân viên cho trước
    employee_database = { 
    1000: dict(name="Alex",   doj='01-10-89', dept=103),
    1001: dict(name="Mary",   doj='01-11-88', dept=101),
    1002: dict(name="John",   doj='01-10-87', dept=104),
    1003: dict(name="David",  doj='01-06-89', dept=105),
    1004: dict(name="Anne",   doj='01-01-86', dept=106),
    1005: dict(name="Samson", doj='01-02-89', dept=101),
    1006: dict(name="Anrex",  doj='01-05-85', dept=None)
    }
    
    # Phòng làm của nhân viên hiện tại
    department_database = {
      101 : 'HRD',
      102 : 'FINANCE',
      103 : 'ACCOUNTS',
      104 : 'SALES',
      105 : 'ENGINEERING',
      106 : 'SUPPORT'
     }

    id_employee = int(input('Please enter employee ID: '))
    
    employee_data = GetEmployeeInformation(id_employee)
    print(employee_data)
    
    if employee_data:
        DisplayEmployData(employee_data)