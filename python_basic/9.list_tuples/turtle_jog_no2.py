import turtle as t
import turtle_jog_no1

def TurtleRace():
    global full_turtle, name_turtle, way_turtle
    turtle_jog_no1.AllTurtle()
    # chuyển list của biến all_turtle thành full_turtle
    full_turtle = turtle_jog_no1.all_turtle
    # Gọi tên rùa theo màu sắc
    name_turtle = turtle_jog_no1.color_turtle
    turtle_jog_no1.TurtleRunning(full_turtle)
    # quãng đường rùa đi được
    way_turtle = turtle_jog_no1.finish

def finish():
    global ranking, way_sort
    ranking = {}
    # Ép thành dictionary để gọi tên
    for name, way in zip(name_turtle, way_turtle):
        ranking[way] = name
    # Sắp xếp lại ai chạy xa hơn
    way_sort = sorted(way_turtle)

def main():
    TurtleRace()
    finish()
    first = way_sort[-1]
    print(f"Winner: {ranking[first]} turtle")
    t.exitonclick()

if __name__ == '__main__':
    main()