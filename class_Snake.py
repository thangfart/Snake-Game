from turtle import Turtle
STARTING_POINTS = [(0,0),(-20,0),(-40,0),(-60,0)]
MOVE_DIST = 20
NORTH = 90
WEST = 180
SOUTH = 270
EAST = 0

t = Turtle()
t.heading()

class Snake:

    def __init__(self):
        self.segments = []
        self.initializeSnake()
        self.head = self.segments[0]

    def resetSnake(self):
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        self.initializeSnake()
        self.head = self.segments[0]

    def initializeSnake(self):
        for pos in STARTING_POINTS:
            self.addSegment(pos)

    def moveForward(self):
        for seg_nr in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_nr-1].xcor()
            new_y = self.segments[seg_nr-1].ycor()
            self.segments[seg_nr].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

    def orientUp(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def orientDown(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def orientLeft(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def orientRight(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def addSegment(self,position):
        newSegment = Turtle(shape="square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.setpos(position)
        self.segments.append(newSegment)

    def extend(self):
        self.addSegment(self.segments[-1].position())


if __name__ == "__main__":
    s = Snake()
