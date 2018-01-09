import turtle
wn = turtle.Screen()
tur = turtle.Turtle()
tur.shape("turtle")
tur.showturtle()

Bold = False
tur.left(90)
Color = "blue"


def drawj(sizej, Bold, Color):
    for i in range(1):
        if Bold == True:
            tur.pensize(3)
            sizej = sizej + 1
        if Bold == False:
            tur.pensize(1)
        if Color == "red":
            tur.color("red")
        tur.right(90)
        tur.penup()
        tur.backward(35 * sizej)
        tur.forward(1)
        tur.pendown()
        tur.right(90)
        tur.forward(10 * sizej)
        tur.left(90)
        tur.forward(20 * sizej)
        tur.left(90)
        tur.forward(60 * sizej)
        tur.left(90)
        tur.forward(20 * sizej)
        tur.back(40 * sizej)
        tur.penup()
        tur.left(90)
        tur.forward(60 * sizej)
        tur.left(90)
        tur.forward(15 * sizej)
        tur.left(90)
        tur.pendown()


def drawr(sizer):
    tur.forward(100 * sizer)
    for i in range(18):
        tur.right(15 * sizer)
        tur.forward(7 * sizer)
    tur.left(110)
    tur.forward(80 * sizer)
    tur.left(70)
    tur.forward(20)


drawj(sizej = 1, Bold = True, Color = "red")
drawr(sizer = 1)

turtle.mainloop()  # make screen show
