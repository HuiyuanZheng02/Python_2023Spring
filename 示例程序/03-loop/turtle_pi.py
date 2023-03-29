#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import turtle
import math
import random

def montecarlo_pi(tries=1000000):
    pen = turtle.Turtle()
    win = turtle.Screen()
    win.setup(600, 600)
    win.setworldcoordinates(-1,-1,1,1)
    pen.speed(0)
    pen.hideturtle()
    if tries > 200:
        win.tracer(100)

    pen.up()
    pen.goto(1, 0)
    pen.down()
    pen.setheading(90)
    pen.circle(1,360, steps=360)
    pen.up()

    hits = 0
    for i in range(tries):
        randx = random.random()
        randy = random.random()

        x = randx * 2 - 1
        y = randy * 2 - 1
        pen.goto(x, y)

        if x * x + y * y <= 1:
            pen.dot(8,'red')
            hits += 1
        else:
            pen.dot(8,'blue')

    win.exitonclick()
    pi = 4 * hits / tries
    return pi


if __name__ == '__main__':
    pi = montecarlo_pi(2000)
    print('pi =', pi)
