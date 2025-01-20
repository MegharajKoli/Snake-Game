from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
screen=Screen()
screen.setup(width=600,height=600)
screen.title("Snake game by MK")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


game_on=True
while(game_on):
    screen.update()
    time.sleep(0.1)
    snake.moving()

    #detecting collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-280:
        game_on=False
        scoreboard.game_over()

    #detect collision with itself
    for segment in snake.segments[3:]:
        if snake.head.distance(segment)<10:
            game_on=False
            scoreboard.game_over()
screen.exitonclick()