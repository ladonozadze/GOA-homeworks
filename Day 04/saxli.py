from turtle import*

# paint a house

speed(100)
width(1)
color("brown")

forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)

#drawing a dor


forward(40)
color("black")
begin_fill()
left(90)

forward(30)
right(90)
forward(20)
right(90)
forward(30)
end_fill()

#paint a roof

penup()
goto(100,100)
pendown()
color("red")
begin_fill()
right(150)
forward(100)
left(120)
forward(100)
end_fill()

#paint a window
color("maroon")
begin_fill()
left(30)
forward(20)
color("brown")
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()

#2window
penup()
goto(100,100)
pendown()
left(90)
color("blue")
forward(20)
right(90)

color("brown")
begin_fill()
forward(20)

left(90)
forward(20)
left(90)
forward(20)
end_fill()





#paint a house 2
width(2)

penup()
goto(200,200)
pendown()
color("sienna")

forward(110)
left(90)

forward(110)
left(90)

forward(110)
left(90)

forward(110)
left(90)

#door 2

forward(45)
color("gold")
begin_fill()
left(90)

forward(40)
right(90)
forward(20)
right(90)
forward(40)
end_fill()

#paint a roof
penup()
goto(310,310)
pendown()
color("peru")
begin_fill()
right(150)
forward(110)
left(120)
forward(110)
end_fill()

#paint a window
color("blueviolet")
begin_fill()
left(30)
forward(30)
color("brown")
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

# window 2

penup()
goto(310,310)
pendown()
left(90)
color("brown")
begin_fill()
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()





#paint a house 3
width(1.5)
color("slategrey")
penup()
goto(150,-300)
pendown()


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)



#roof 3

penup()
goto(150,-300)
pendown()
begin_fill()

left(90)
forward(200)
color("slateblue")
begin_fill()
right(30)
forward(200)
right(120)
forward(200)
end_fill()

#paint a windowW

right(30)
forward(50)
color("purple")
begin_fill()
right(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

#paint a window 2
begin_fill()


penup()
goto(150,-300)
pendown()
begin_fill()
color("slategrey")

left(90)
forward(150)
color("purple")
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

#draw a door
penup()
goto(150,-300)
pendown()
begin_fill()
color("gray")

right(180)
forward(85)
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
end_fill()


#stars
width(0.5)
penup()
goto(-400,450)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()

#2star

penup()
goto(-300,450)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()

#3star

penup()
goto(-200,450)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()

#4star
penup()
goto(-200,350)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()

#5star

penup()
goto(-100,350)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()


#6star

penup()
goto(-100,450)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()

#7star

penup()
goto(-400,250)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()

#8star

penup()
goto(-600,250)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()

#9star

penup()
goto(-600,350)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()

#10star
penup()
goto(-550,450)
pendown()
begin_fill()
color("midnightblue")
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
end_fill()

#moon


begin_fill()
color("darkslateblue")
penup()
goto(-900,400)
pendown()
radius =70
circle(100)
end_fill()








exitonclick()