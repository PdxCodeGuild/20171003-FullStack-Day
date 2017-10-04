"""
Lab 1: Turtle
draw a stick figure using Turtle
"""


from turtle import *

scale = 100


# draw arms
left(180)
penup()
forward(scale/2)
left(180)
pendown()
forward(scale)
left(180)
penup()
forward(scale/2)
left(90)

# draw body
pendown()
forward(scale)

# draw legs
right(45)
forward(scale/2)
right(180)
penup()
forward(scale/2)
right(90)
pendown()
forward(scale/2)
right(180)
penup()
forward(scale/2)
right(45)
pendown()
forward(scale+scale/10) # a little extra for the head
right(90)

# draw the head
i = 0
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1

done()


