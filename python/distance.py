import turtle

x1, y1 = eval(input("Enter a value for x1, y1: ")) # p1
x2, y2 = eval(input("Enter a value for x2, y2: ")) # p2

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print("Distance:", distance)

# Draw the distance between p1 & p2
turtle.penup()
turtle.goto(x1, y1) # start at the top
turtle.pendown()
turtle.write("Point 1")
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2) # go to midpoint of p1 & p2
turtle.write(distance)
turtle.goto(x2, y2)
turtle.write("Point 2")
turtle.done()
