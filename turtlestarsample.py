import turtle

wn = turtle.Screen()
tur = turtle.Turtle()
tur.shape("turtle")
tur.showturtle()


def drawstar(size):
    for i in range(5):
        tur.forward(10 + 20 * size)
        tur.left(144)  # turn left 144 degrees


drawstar(1)
drawstar(2)
drawstar(3)
drawstar(4)
drawstar(5)
turtle.mainloop()  # make screen show
