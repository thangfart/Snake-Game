from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle") #make a circle shaped "food", 20pix*20pix normally
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #10pix * 10pix circle
        self.color("blue")
        self.speed("fastest")
        self.update()

    def update(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)






