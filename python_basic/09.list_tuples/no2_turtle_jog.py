import turtle as t
import no1_turtle_jog

def TurtleRace():
    global full_turtle, name_turtle, way_turtle
    no1_turtle_jog.AllTurtle()
    # chuyển list của biến all_turtle thành full_turtle
    full_turtle = no1_turtle_jog.all_turtle
    # Gọi tên rùa theo màu sắc
    name_turtle = no1_turtle_jog.color_turtle
    no1_turtle_jog.TurtleRunning(full_turtle)
    # quãng đường rùa đi được
    way_turtle = no1_turtle_jog.finish

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
    print("Finish time: %.3f sec" %(no1_turtle_jog.finish_time))
    t.exitonclick()
    
if __name__ == '__main__':
    main()