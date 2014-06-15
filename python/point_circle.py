import turtle
import math

cx, cy = eval(input("Enter the center of a circle x, y: "))
radius = eval(input("Enter the radius of the circle: "))
x, y = eval(input("Enter a point x, y: "))

distance = math.sqrt(((x - cx) ** 2) + ((y - cy) ** 2))
inside = radius >= distance


# Draw the circle & the point
turtle.hideturtle()
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.dot(5, "red")
turtle.penup()
turtle.goto(cx, cy - radius)
turtle.pendown()
turtle.circle(radius)

# Write the remarks
remarks = "The point is " + \
          ("inside" if inside else "outside") + \
          " the circle."
turtle.penup()
turtle.goto(cx, cy - radius - 20)
turtle.write(remarks, align= "center",\
             font= ("Arial", 12, "normal"))
turtle.done()
