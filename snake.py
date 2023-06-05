from turtle import Turtle
MOVE =20
UP =90
DOWN = 270
RIGHT = 0
LEFT=180
class Snake  :
    def __init__(self):
        self.segments = []
        self.x_position =0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(0,3):
            self.add_segment()

        
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
           next_x= self.segments[seg_num-1].xcor()
           next_y= self.segments[seg_num-1].ycor()
           self.segments[seg_num].goto(next_x,next_y)
        self.segments[0].forward(MOVE)


    def add_segment(self):
        newsquare = Turtle(shape="square")
        # newsquare.shapesize(.2, 1, 1)
        newsquare.color("white")
        newsquare.up()
        self.x_position+=newsquare.xcor()-20
        newsquare.goto(x=self.x_position,y=0)
        self.segments.append(newsquare)

        

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment()

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(90)

    
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(0)
    
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(180)
        