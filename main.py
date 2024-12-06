import turtle

screen = turtle.Screen()
screen.bgcolor("yellow")
screen.title("Catch The Turtle")
font = ("Arial",15,"bold")
score_turtle = turtle.Turtle()
#score turtle

def setup_score_turtle():
    score_turtle.color("dark blue")
    score_turtle.ht()
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setposition(0,y)
    score_turtle.write(arg="Score: 0", move=False, align="left", font=font)
setup_score_turtle()
turtle.mainloop()