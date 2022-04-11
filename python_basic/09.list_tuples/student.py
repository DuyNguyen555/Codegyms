# def sorted_name(self):
#     return self['name']

# def sorted_age(self):
#     return self['age']

# def sorted_hobby(self):
#     return self['hobby']

# def List():
#     list_table = [
#         {'name' : 'D', 'age' : 22 , 'hobby' : 'H'},
#         {'name' : 'A', 'age' : 23 , 'hobby' : 'E'},
#         {'name' : 'c', 'age' : 21 , 'hobby' : 'L'},
#         {'name' : 'B', 'age' : 25 , 'hobby' : 'L'},
#         {'name' : 'E', 'age' : 25 , 'hobby' : 'O'}
#     ]

#     list_table.sort(key=sorted_name)
#     print('sort by name:' ,list_table)
#     print()
#     list_table.sort(key=sorted_age)
#     print('sort by age:' ,list_table)
#     print()
#     list_table.sort(key=sorted_hobby)
#     print('sort by hobby:' ,list_table)   

# def Tuple():
#     pass


import time
import turtle 
def _ve():
    window = turtle.Screen()
    window.tracer(0)
    player = turtle.Turtle()
    timer_text = turtle.Turtle()
    timer_text.hideturtle()
    start = time.time()
    while time.time() - start < 5:
        player.forward(1)
        player.left(1)
        timer_text.clear()
        timer_text.write(int(time.time()-start),font=('Courier',30))
        window.update()
    turtle.done()

if __name__ == '__main__':
    _ve()