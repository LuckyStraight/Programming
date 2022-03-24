#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Tess Again
#
# Filename:     10-1
# Date:  10/27/2021
#--------------------------------------------------------------------------------

import turtle

turtle.setup(500,500) # Determine the window size
wn = turtle.Screen() # Get a reference to the window
wn.title("Handling keypresses!") # Change the window title
wn.bgcolor("black") # Set the background color
ciara = turtle.Turtle() # Create our favorite turtle
ciara.color("white") # base color of turtle is white
ps = 1 

# The h1-h4 functions are our "event handlers".
def h1():
     ciara.forward(30)

def h2():
    ciara.left(45)

def h3():
    ciara.right(45)

def red(): # Makes the turtle red
    ciara.color("red")

def green(): # Makes the turtle green
    ciara.color("green")

def blue(): # Makes the turtle blue
    ciara.color("blue")

def increase(): # increases the pensize ofthe turtle by 1 to having a max size of 21
    global ps
    if ps < 20:
        ps +=1
    wn.title("pensize {}" .format(ps)) # shows the count of the pensize on the window title
    ciara.pensize(ps)

def decrease(): # decreases the pensize of the turtle by 1 to having the min size of 1
    global ps
    ps -= 1
    if ps == 0:
        ps +=1
    wn.title("pensize {}" .format(ps)) # shows the count of the pensize on the window title
    ciara.pensize(ps)

def h4():
    wn.bye() # Close down the turtle window

# These lines "wire up" keypresses to the handlers we’ve defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.onkey(increase, "+") # must hit + to increase pensize of the turtle
wn.onkey(decrease, "-") # must hit - to decrease pensize of the turtle

# pressing either r,g ,b changes the color of the turtle
wn.onkey(red, "r")
wn.onkey(green, "g")
wn.onkey(blue, "b")

wn.listen() #allows the key inputs to effect the turtle
wn.mainloop()