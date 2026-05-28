from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Capstone")
screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_starting_position()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()
