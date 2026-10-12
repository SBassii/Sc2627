import turtle
import math
def square(x, y, size, rotation, sides):
    turtle.penup()
    semi_angle = 180/sides
    r = size/(2*(math.sin(math.radians(semi_angle))))
    turtle.goto(x, y - r)
    turtle.circle(r, rotation)
    turtle.pendown()
    turtle.circle(size, 360, sides)
    turtle.exitonclick()

square(50, 70, 100, 3, 3)