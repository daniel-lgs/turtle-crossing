import time
import random
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Player
player = Player()
screen.onkeypress(player.move, "Up")

# Cars
cars = []

# Scoreboard
scoreboard = Scoreboard()

# Game velocity
velocity = 0.1

game_is_on = True
while game_is_on:
    time.sleep(velocity)
    screen.update()

    # Traffic cars volume
    if random.randint(1, 10) == 1:
        new_car = Car()
        cars.append(new_car)

    # Move all cars and detect collision with player
    for car in cars:
        car.move()
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Player level up
    if player.on_finish_line():
        velocity /= 1.5
        scoreboard.update()
        player.go_to_home()

screen.exitonclick()
