import turtle
wn = turtle.Screen()
tur = turtle.Turtle()
tur.shape("turtle")
tur.showturtle()
Fast = False
stop = False
Bold = False
tur.left(90)
tur.penup()
tur.back(90)
tur.pendown()
Color = "blue"


def drawj(sizej, Bold, Color, Fast, turtle):
    for i in range(1):
        if Fast == True:
            tur.speed(0.50)
        if Bold == True:
            tur.pensize(3)
            sizej = sizej + 1
        if Bold == False:
            tur.pensize(1)
        if Color == "blue":
            tur.color("blue")
        tur.right(90)
        tur.penup()
        tur.backward(60 * sizej)
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
        tur.forward(10 * sizej)
        tur.left(90)
        tur.pendown()


def drawr(sizer):
    tur.forward(70 * sizer)
    for i in range(18):
        tur.right(15)
        tur.forward(5 * sizer)
    tur.left(110)
    tur.forward(55 * sizer)
    tur.left(65)
    tur.penup()
    tur.forward(30 * sizer)
    tur.left(95)
    tur.pendown()

def drawslash(sizes):
    tur.color("red")
    tur.forward(35 * sizes)
    for i in range(8):
        tur.left(15)
        tur.forward(40 * sizes)
    for i in range(7):
        tur.left(15)
        tur.forward(25 * sizes)
    for i in range(9):
        tur.left(10)
        tur.forward(30 * sizes)
    tur.left(100)
    tur.forward(250 * sizes)
troll = turtle.Turtle
drawj(turtle = troll, sizej = 1, Bold = True, Color = "blue", Fast = False)
drawr(sizer = 1)
drawr(sizer = 1)
drawslash(sizes = 1)
turtle.mainloop()  # make screen show
