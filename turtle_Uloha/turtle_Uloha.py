import turtle

from random import random, randrange

t = turtle.Turtle()

def stvorec(velkost_strany):
    t.pendown()
    t.color('blue')
    t.pensize(3)
    for i in range(4):
        t.fd(velkost_strany)
        t.right(90)
def trojuholnik(velkost_strany):
    t.pendown()
    t.color('green')
    t.pensize(3)
    for j in range(3):
        t.fd(velkost_strany)
        t.right(120)
def mnohouholnik(velkost_strany, pocet_vrcholov):
    uhol = 360 / pocet_vrcholov
    if pocet_vrcholov < 3:
        return
    else:
        t.pendown()
        t.color('red')
        t.pensize(3)
        for j in range(pocet_vrcholov):
            t.fd(velkost_strany)
            t.right(uhol)


pocet_tvarov = randrange(1, 15)
for f in range(pocet_tvarov):
    t.penup()
    pozicia_X = randrange(-200 , 201)
    pozicia_Y = randrange(-200, 201)
    t.setpos(pozicia_X, pozicia_Y)
    uhol_otocenia = randrange(0, 360)
    t.setheading(uhol_otocenia)
    randomTvar = randrange(0, 3)
    randomVelkost = randrange(1, 100)
    if randomTvar == 0:
        stvorec(randomVelkost)
    elif randomTvar == 1:
        trojuholnik(randomVelkost)
    else:
        randomVrcholy = randrange(3,10)
        mnohouholnik(randomVelkost, randomVrcholy)
turtle.exitonclick()