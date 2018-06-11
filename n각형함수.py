import turtle
t = turtle.Turtle()
t.shape("turtle")

def angle(x):
    for i in range(x):
        t.fd(100)
        t.left(360/x)
x = int(turtle.textinput("","원하는 n각형을 적으시오:"))
angle(x)
