from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.move_distance = STARTING_MOVE_DISTANCE
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setposition(300, random.randint(-200, 200))

    def move(self):
        self.forward(self.move_distance)

    def increase_movement(self):
        self.move_distance += MOVE_INCREMENT
