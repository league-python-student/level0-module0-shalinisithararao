import random
import turtle

# Returns a random color!
#def getRandomColor():
#    return "#%06X" % (random.randint(0, 0xFFFFFF))


def getNextColor(i):
    colors = ('#FFCCE5', '#FFE5CC', '#FFFFB5', '#CCFFCC', '#CCE5FF', '#EDD8FF')
    return colors[i % len(colors)]

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')


    # Make a new turtle
    window = turtle.Screen()
    bob=turtle.Turtle()
    # This code sets our shape to a turtle
    bob.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    bob.speed(6)
    # Set your turtle's color using .color('green')
    bob.color('teal')
    # Use a loop to repeat a the code below 50 times
    for i in range(100):
        # Set the turtle color to a random color




        bob.color(getNextColor(i))
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        bob.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        bob.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        bob.width(i)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
