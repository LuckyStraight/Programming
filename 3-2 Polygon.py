#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Draw a Polygon
#
# Filename:     3-2
# Date:  9/1/2021
#-------------------------------------------------------------------------------

#number of sides from the user
sides_of_shape = int(input("Enter the number of sides of the shape: "))

#set up screeen and turtle objects
import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Chad Adventure")


#set up screen and turtle properties
Chad = turtle.Turtle()
Chad.color("green")
Chad.pensize(3)
Chad.shape("turtle")

#create a loop to create polygon using inputted sides and turtle object
for i in range(sides_of_shape):
    Chad.forward(50)
    Chad.left(360/sides_of_shape)

wn.mainloop()