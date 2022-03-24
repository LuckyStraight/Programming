import turtle

wn = turtle.Screen()
wn.bgcolor("pink")
wn.title = ("Happy Valentines Day")

sarah = turtle.Turtle()
sarah.color("red")
sarah.pensize(10)
sarah.shape("turtle")
sarah.speed(0)

def curve():
    for i in range(200):
        sarah.right(1)
        sarah.forward(1)

def heart():
   sarah.begin_fill()
   sarah.left(140)
   sarah.forward(111.65)
   curve()

   sarah.left(120)
   curve()
   sarah.forward(113)
   sarah.end_fill()

heart()
sarah.hideturtle()

def write():

    sharda = turtle.Turtle()
    sharda.color("maroon")
    sharda.write("Happy Valentines Day\n I love You Mamas", align = "center", font = ("Papyrus",24,"bold"))
    sharda.hideturtle()

write()

wn.mainloop()