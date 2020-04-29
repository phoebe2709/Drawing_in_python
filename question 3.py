import turtle
turtle.bgcolor("black")

turtle.color("black", "brown")

turtle.begin_fill()
for i in range(3):
    turtle.forward(200)
    turtle.left(120)
turtle.end_fill()

turtle.color("black", "red")
turtle.begin_fill()
for i in range(4):
    turtle.forward(200)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.setx(10)
turtle.sety(-20)
turtle.pendown()

turtle.color("black", "pink")
turtle.begin_fill()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.setx(130)
turtle.sety(-20)
turtle.pendown()

turtle.color("black", "pink")
turtle.begin_fill()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.setx(70)
turtle.sety(-120)
turtle.pendown()

turtle.color("black", "grey")
turtle.begin_fill()

turtle.forward(50)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(80)
turtle.end_fill()

turtle.penup()
turtle.setx(85)
turtle.sety(-160)
turtle.pendown()

turtle.color("black", "black")
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()

turtle.penup()
turtle.setx(-30)
turtle.sety(150)
turtle.pendown()

turtle.color("black", "silver")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()



turtle.done()

