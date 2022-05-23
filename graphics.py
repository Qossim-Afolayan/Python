import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

qossim = turtle.Turtle()
qossim.color("blue")
qossim.pensize(3)

tess = turtle.Turtle()
tess.shape("turtle")
tess.up()
tess.stamp()
tess.fd(150)
tess.lt(90)
tess.fd(75)


qossim.fd(150)
qossim.left(90)
qossim.forward(75)
qossim.speed(5)

wn.exitonclick()
