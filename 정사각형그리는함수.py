import turtle
t=turtle.Turtle()
t.shape("turtle")
length=int(turtle.textinput("","한변의 길이:"))
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
square(length)
    
