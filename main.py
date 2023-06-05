from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

with open("data.txt",mode="r+") as file:
    score = file.read()
print(score)
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
x_position = 0
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard(score)
game_is_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
       scoreboard.increase_score()
       food.refresh()
       snake.extend()
    # detect collision with wall

    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        scoreboard.reset_scoreboard()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
          scoreboard.reset_scoreboard()



screen.exitonclick()