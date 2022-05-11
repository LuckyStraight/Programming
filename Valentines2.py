import turtle

wn = turtle.Screen()
wn.bgcolor("pink")
wn.title("Happy Valentines Day")

heart = turtle.Turtle()
heart.color("red")
heart.pensize(8)
heart.shape("turtle")
heart.goto(0,-10)

heart.begin_fill()
heart.left(140)
heart.forward(180)
heart.circle(-90,200)
heart.setheading(60)
heart.circle(-90,200)
heart.forward(178)
heart.end_fill()

heart.penup()
heart.goto(-65,130)
heart.pendown()

heart.color("purple")
heart.write("I Love You",align = "left", font = ("Papyrus",24,"bold") )
heart.hideturtle()

wn.mainloop()