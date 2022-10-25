from turtle import Screen
from Exercises.day20and21.snake_game.class_Snake import Snake
from Exercises.day20and21.snake_game.class_Food import Food
from Exercises.day20and21.snake_game.class_Scoreboard import Scoreboard
import time
SNAKEHEAD_LIM = 290
######################################################################################################
#setting up the main window
window = Screen()
window.setup(width=600,height=600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)
######################################################################################################
#initializing snake,food,scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()
######################################################################################################
#control the snake
window.listen()
window.onkey(snake.orientUp,"Up")
window.onkey(snake.orientDown,"Down")
window.onkey(snake.orientLeft,"Left")
window.onkey(snake.orientRight,"Right")
######################################################################################################
game_is_on = True

# game loop
while game_is_on:
    window.update()
    time.sleep(0.1)
    snake.moveForward()

    # update pos of food after success
    if snake.head.distance(food) < 15:
        scoreboard.incScore()
        #scoreboard.incHighestScore()
        print("eaten")
        food.update()
        snake.extend()

    #detect if a wall is hitten by the head
    if abs(snake.head.ycor()) >= SNAKEHEAD_LIM or abs(snake.head.xcor()) >= SNAKEHEAD_LIM:
        scoreboard.resetSb()
        snake.resetSnake()


    #colission check of snake with itself method 1, worked sometimes, and sometimes not
    #for seg_i in range(len(snake.segments)-1,1,-1):
        #if snake.segments[seg_i].ycor() == snake.head.ycor()+10 and snake.segments[seg_i].xcor() == snake.head.xcor()+10:
            #game_is_on = False
            #scoreboard.printGameOver()

    #colission check of snake with itself method 2
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10: #compare distance from tail to a seg
            scoreboard.resetSb()
            snake.resetSnake()


######################################################################################################
window.exitonclick()
