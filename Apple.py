from ntpath import join
import turtle

wn = turtle.Screen()
wn.title("Apple Logo")
wn.bgcolor("gray")

Jobs = turtle.Turtle()
Jobs.shape("turtle")
Jobs.pensize(8)
Jobs.speed(0)
Jobs.goto(0,0)



Jobs.begin_fill()
Jobs.fillcolor("black")
Jobs.left(134)

for i in range(30):
    Jobs.forward(1)
    Jobs.left(1)
Jobs.right(5)

for i in range(35):
    Jobs.forward(1)
    Jobs.left(1)
Jobs.left(5)
Jobs.forward(30)

for i in range(15):
    Jobs.forward(.7)
    Jobs.right(3)
Jobs.forward(25)
Jobs.left(5)

for i in range(50):
    Jobs.forward(1)
    Jobs.left(1)
Jobs.right(3)

for i in range(50):
    Jobs.forward(1)
    Jobs.left(1)
Jobs.right(5)

for i in range(45):
    Jobs.forward(2)
    Jobs.left(1)
Jobs.right(5)

for i in range(40):
    Jobs.forward(2)
    Jobs.left(1)
Jobs.left(5)

for i in range(20):
    Jobs.forward(1)
    Jobs.left(2)
Jobs.left(5)
Jobs.forward(15)

for i in range(9):
    Jobs.forward(2)
    Jobs.right(3)
Jobs.forward(1)

for i in range(15):
    Jobs.forward(1)
    Jobs.right(1)
Jobs.right(4)
Jobs.forward(4.5)

for i in range(27):
    Jobs.forward(1)
    Jobs.left(2)
Jobs.left(8)
Jobs.forward(5)

for i in range(25):
    Jobs.forward(2)
    Jobs.left(1)
Jobs.right(3)
Jobs.forward(10)
Jobs.left(83)

for i in range(75):
    Jobs.forward(1.3)
    Jobs.right(1)
Jobs.right(4)

for i in range(24):
    Jobs.forward(1.3)
    Jobs.right(1)
Jobs.forward(9.66)
Jobs.end_fill()
Jobs.penup()

Jobs.left(132)
Jobs.forward(100)
Jobs.right(96)
Jobs.pendown()

Jobs.begin_fill()
Jobs.fillcolor("black")

for i in range(60):
    Jobs.forward(.8)
    Jobs.right(1)
Jobs.right(120)

for i in range(60):
    Jobs.forward(.8)
    Jobs.right(1)

Jobs.hideturtle()
Jobs.end_fill()
Jobs.pendown()

Jobs.penup()
Jobs.goto(-65,130)
Jobs.pendown()

Jobs.color("black")
Jobs.write("Think Differently", align = "center", font = ("Papyrus",24,"bold"))

Jobs.hideturtle()
Jobs.end_fill()


wn.mainloop()