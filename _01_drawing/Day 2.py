import turtle

if __name__ == '__main__' :

    window = turtle.Screen()

    bob = turtle.Turtle()
    bob.shape('turtle')
    bob.color('teal')

    for i in range (20):
        bob.forward(100)
        bob.left(90)
        for k in range(4):
            bob.forward(100)
            bob.left(90)





    turtle.done()