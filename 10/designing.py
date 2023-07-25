import turtle

t = turtle.Turtle()

t.pensize(20)

t.pencolor('blue')
t.fillcolor('white')

t.begin_fill()


t.forward(200)
t.right(120)
t.forward(200)
t.right(120)
t.forward(200)

t.penup()
t.goto(100 , 50)
t.pendown()

t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)

t.end_fill()

turtle.done()
