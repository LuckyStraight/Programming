#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     spiral modification
#
# Filename:     3-3
# Date:  9/1/2021
#-------------------------------------------------------------------------------
import turtle
window = turtle.Screen()
window.bgcolor("orange")
chad = turtle.Turtle()
chad.shape("circle")
chad.color("white")
turtle.setup(800,800) #changes size of the screen

chad.penup()  # This is new
size =  5
for i in range(70):
    chad.stamp()   # Leave an impression on the canvas
    size = size + 1   # Increase the size on every iteration
    chad.forward(size)    # Move tess along
    chad.right(45)    # ... and turn her

chad.hideturtle()
wn.mainloop()