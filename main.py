import turtle
import random

screen = turtle.Screen()
screen.bgcolor("yellow")
screen.title("Catch The Turtle")
font = ("Arial",15,"bold")
score_turtle = turtle.Turtle()
grid_size = 15
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]

#turtle list
turtle_list = []



#score turtle
def setup_score_turtle():
    score_turtle.color("dark blue")
    score_turtle.ht()
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setposition(0,y)
    score_turtle.write(arg="Score: 0", move=False, align="left", font=font)

def make_turtle(x,y):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("red")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
       t.hideturtle()

def show_turtles_randomly():
    random.choice(turtle_list).showturtle()

turtle.tracer(0)
setup_turtles()
hide_turtles()
setup_score_turtle()
turtle.tracer(1)
show_turtles_randomly()
turtle.mainloop()