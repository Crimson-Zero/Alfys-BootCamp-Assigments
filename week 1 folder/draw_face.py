import turtle

def draw_square():
    side = 100
    
    turtle.forward(side)
    turtle.left(90)
    
    turtle.forward(side)
    turtle.left(90)
    
    turtle.forward(side)
    turtle.left(90)
    
    turtle.forward(side)
    turtle.left(90)
    
    turtle.left(90)
    turtle.forward(100)


def draw_big_circle():
    
    radius = 40
    turtle.circle(radius)

def draw_small_circle():
    
    radius = 20
    turtle.circle(radius)

def draw_eye():
    
    radius = 10
    turtle.circle(radius)

def triangle(edge=10):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)

def draw_nose():
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    triangle()
    
draw_square()

turtle.right(90)
turtle.forward(10)

draw_big_circle()
draw_small_circle()

turtle.forward(90)

draw_big_circle()
draw_small_circle()
draw_nose()

turtle.pendown()
turtle.right(90)
turtle.right(90)

turtle.penup()
turtle.forward(50)

turtle.left(90)
turtle.forward(30)

turtle.left(90)

turtle.forward(30)
turtle.pendown()
draw_eye()

turtle.penup()

turtle.forward(50)

turtle.pendown()
draw_eye()

turtle.penup()

turtle.forward(20)

turtle.left(90)
turtle.forward(80)

turtle.left(90)
turtle.forward(50)

turtle.left(90)
turtle.penup()
turtle.forward(30)
turtle.right(90)
turtle.forward(20)

turtle.right(90)

turtle.pendown()
turtle.circle(-20,180)



