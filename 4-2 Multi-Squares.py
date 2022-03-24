#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Squares in squares
#
# Filename:     4-2
# Date:  9/7/2021
#-------------------------------------------------------------------------------

import turtle

#function to draw square
def drawSquare (t, size):
    for i in range (4):
        t.forward(size)
        t.left(90)

#main function imports turtle, defines turtle and screen objects and properties; call the mansquares function
def main():
    wn = turtle.Screen()
    wn.bgcolor('black')
    pat = turtle.Turtle()
    pat.pensize(2)
    pat.speed(10)
    pat.color('blue')
    space = -10

#function to draw 5 squares
    for i in range(20, 105, 20):
        drawSquare(pat,i)
        pat.up()   #code to raise pen and move SW
        pat.goto(space, space)
        pat.down()
        space = space - 10

    wn.mainloop()

#call the main() function
main()