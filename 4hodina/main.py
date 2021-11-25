import turtle
from random import randrange
t = turtle.Turtle

def stvorec(dlzka_stvorca):
    t.penup()
    t.fd(dlzka_stvorca)
    t.rt(90)
stvorec(20)
exitonclick()