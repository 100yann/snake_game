from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("BIG SNEK")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.addscore()
        snake.extend()

    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False
    #     scoreboard.game_over()
    #     time.sleep(2)
    #     screen.bye()
    if snake.head.xcor() > 280:
        y = snake.head.ycor()
        snake.head.goto(-280, y)
    elif snake.head.xcor() < -280:
        y = snake.head.ycor()
        snake.head.goto(280, y)
    elif snake.head.ycor() > 280:
        x = snake.head.xcor()
        snake.head.goto(x, -280)
    elif snake.head.ycor() < -280:
        x = snake.head.xcor()
        snake.head.goto(x, 280)

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            time.sleep(2)
            screen.bye()