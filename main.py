import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")
screen.onkey(player.go_left, "a")
screen.onkey(player.go_right, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    car_manager.create_car()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
