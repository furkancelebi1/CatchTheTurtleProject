import turtle
import random

screen = turtle.Screen()
screen.bgcolor("yellow")
screen.title("Catch The Turtle")
font = ("Arial",15,"bold")
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
grid_size = 15
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]
score = 0
game_over = False
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
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="left", font=font)

    t.onclick(handle_click)
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
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.ht()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setposition(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="left", font=font)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over", move=False, align="left", font=font)

turtle.tracer(0)
setup_turtles()
hide_turtles()
setup_score_turtle()
countdown(10)
turtle.tracer(1)
show_turtles_randomly()
turtle.mainloop()