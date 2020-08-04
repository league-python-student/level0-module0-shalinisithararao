import random
import turtle

colors = ('#FFCCE5','#FFE5CC','#FFFFB5','#CCFFCC','#CCE5FF','#EDD8FF')
def getNextColor(i):
    return colors[i % len(colors)]
# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

def screenClicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    
    # 6. Call the turtle .penup() method
    bob.penup()
    # 7. Move the turtle to a new location using .goto(x, y)

def turtleClicked(x, y):
    print('turtle clicked!')
    
    # 8. Make a for loop to run the next instructions 3 times
    for i in range(18):
        # 9. Make the turtle spin 360 degrees using the .right() method
        bob.right(360)
        # 10. Use the .color() method and getRandomColor() function to change
        # the color of the turtle,hu
        # myTurtle.color(getRandomColor())
        bob.color(getNextColor(i))
        bob.speed(2)
if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(width=0.75, height=0.8, startx=0, starty=0)
    turtle.bgcolor('#FFFFFF')
    # 1. Make a new turtle
    bob = turtle.Turtle()
    # 2. Make your turtle's shape 'turtle', .shape('turtle')
    bob.shape('turtle')
    # 3. Set your turtle's color using .color('green') and .pencolor('blue')
    bob.color('#FFCCE5')
    # 4. Set and new width, length, and outline of our turtle
    #    myTurtle.turtlesize(stretch_wid=10, stretch_len=10, outline=4)
    bob.turtlesize(stretch_wid=8, stretch_len=8, outline=4)
    # 5. Uncomment the following line and replace 'myTurtle' with your turtle
    #myTurtle.onclick(turtleClicked)
    bob.onclick(turtleClicked)
# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screenClicked)
    turtle.done()
