import turtle

import turtle

wn = turtle.Screen()
wn.bgcolor("pink")
wn.title = ("Happy Valentines Day")

sarah = turtle.Turtle()
sarah.color("red")
sarah.pensize(2)
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
   sarah.forward(111.65)
   sarah.end_fill()

heart()
sarah.hideturtle()

def write():

    dhamini = turtle.Turtle()
    dhamini.color("maroon")
    dhamini.write("Will You Be My Valentines?", align = "center", font = ("Papyrus",24,"bold"))
    dhamini.hideturtle()

write()


wn.mainloop()