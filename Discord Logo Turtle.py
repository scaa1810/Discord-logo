#TASK 1
#DISCORD LOGO
from turtle import *

hideturtle()
speed(5)
width(1)
shape("circle")
bgcolor("black")
shapesize(2.7,2.3,5)

fd(226)
lt(90)

#circle
color("#7289DA")
begin_fill()
circle(227,360)
end_fill()

#actual logo design
color("white")
begin_fill()
penup()
goto(54,-80)
pendown()
rt(150)
fd(32)
lt(80)
circle(350,14)
lt(50)
circle(249,41)
lt(30)
circle(225,17)
lt(80)
fd(18)
rt(85)
circle(150,26)
rt(80)
fd(20)
lt(80)
circle(225,17)
lt(25)
circle(249,40)
lt(50)
circle(310,16)
lt(79)
fd(32)
lt(100)
fd(15)
rt(10)
fd(15)
rt(120)
fd(10)
rt(60)
circle(150,60)
rt(90)
fd(7)
rt(90)
fd(15)

goto(54,-80)
end_fill()

color("#7289DA")

penup()
#right inner circle
goto(48,-10)
seth(0)
stamp()
#left inner circle
bk(97)
stamp()

done()
