#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     random turtle
#
# Filename:     5-1
# Date:  9/21/2021
#-------------------------------------------------------------------------------

#defines the turtle and create the window
def main():
    import turtle
    wn = turtle.Screen()
    wn.bgcolor("black")
    karin = turtle.Turtle()
    karin.shape("turtle")
    karin.pensize(5)
    random_moves(karin)
    wn.exitonclick()

#Makes the turtle move randomly and changes the colors of the line
def random_moves(k):
    import random
    for i in range(50):
        randomi = random.randrange(-100,100)
        if randomi < 0:
            k.pencolor("magenta")
        else:
            k.pencolor("blue")
        k.forward(randomi)
        k.left(randomi)

main()
