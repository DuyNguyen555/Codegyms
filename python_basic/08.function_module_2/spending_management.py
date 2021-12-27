
def add_item(myTempList, item):
    myTempList.append(item)

def find_index_item(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]['name'] == item_name:
            result = i
    return result

def remove_item(myTempList, item_name):
    if find_index_item(myTempList, item_name) > -1:
        del myTempList[find_index_item(myTempList, item_name)]
    else:
        print(item_name + " not in list")

def main():
    expenses = []
    while True:
        print("What do you want to do? -\n"\
            "1. Add\n"\
            "2. Remove\n"\
            "3. Close")
        option = int(input("Select option 1 or 2: "))
        if option == 3:
            break
        else:
            name_input = input("Item name: ")

        if option == 1:
            cost_input = int(input("Item cost: "))
            date_input = input("Date: ")
            item = {'name': name_input, 'cost':cost_input, 'date':date_input}
            add_item(expenses, item)
            length = len(expenses)
            for i in range(length):
                print(f"Name: {expenses[i]['name']}, spend: {expenses[i]['cost']}, date: {expenses[i]['date']}")

        elif option == 2:
            remove_item(expenses, name_input)
            print("Your expenses: ", expenses)
        else:
            print("Invalid input")

if __name__ == '__main__':
    main()