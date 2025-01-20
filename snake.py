from tkinter.constants import RIGHT
from turtle import Turtle
MOVES=[(-40,0),(-20,0),(0,0)]
MOVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in MOVES:
            self.add_segment(position)

    def add_segment(self,position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def moving(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE)

    def move_left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)

    def move_down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)