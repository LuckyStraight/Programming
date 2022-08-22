#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Spiral
#
# Filename:     4-3
# Date:  9/7/2021
#-------------------------------------------------------------------------------

#Draw spiral patterns by python turtle
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
chad = turtle.Turtle()
chad.speed(0)
chad.pensize(2)

#main function imports turtle, defines turtle and screen objects and properties; call the spiral function
colors = ["red", "green", "blue", "orange", "magenta", "cyan"]

def draw_spiral(length, angle, step, min_length): #parameters based on the presented algoritm above
    while(length > min_length): #loop through until the predefine minimum length
        chad.color(colors[length % 6]) #use changes of length as an index of the color
        chad.forward(length) #draw side(s) of the pattern
        chad.left(angle) #turn left an amount of "angle"
        length = length - step #then, reduce the length and get a new length in each time

#call to test the function above with the necessary parameters
def main():
    draw_spiral(length = 250, angle = 150, step = 2, min_length = 20)
    wn.mainloop()

main()
