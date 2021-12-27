def paint():
    import turtle

    shape = input('circle or square: ')
    if shape == 'circle' or shape == 'square':
        colorshape = input(" yellow or red: " )
        if colorshape == 'yellow' or colorshape == 'red':
            turtle.bgcolor('skyblue')
            
            displayshape = turtle.Turtle()
            displayshape.shape(shape)
            displayshape.color(colorshape)
            turtle.exitonclick()
        else:
            print("There's no color.")
    else:
        print("there's no shape.")

def main():
   paint()
   
if __name__ == '__main__':
    main()
