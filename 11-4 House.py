#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     House
#
# Filename:     11-4
# Date:  11/16/2021
#-------------------------------------------------------------------------------
 
import turtle

def drawhouse(t):
    directions = [(100,135), (140,135), (100,135), (140,135), (100,-135), (70,-90), (70,-45), (100,135)]
    for x,y in directions:
        t.forward(x)
        t.left(y)




def main():
    jeff = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("green")
    drawhouse(jeff)
    wn.mainloop()

main()



