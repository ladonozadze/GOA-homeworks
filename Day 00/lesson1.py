from turtle import*
#we want to paint a house

#step 1: draw a square
speed(10)
width(6)
color("blue")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#drawing a dor


forward(70)
color("green")
begin_fill()
left(90)

forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#paint a window
color("blue")
begin_fill()
left(30)
forward(50)
color("brown")
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#2window
penup()
goto(200,200)
pendown()
left(90)
color("blue")
forward(50)
right(90)

color("brown")
begin_fill()
forward(50)

left(90)
forward(50)
left(90)
forward(50)
end_fill()






exitonclick()

