import turtle

screen = turtle.Screen()
screen.bgcolor("yellow")
screen.title("Catch The Turtle")
font = ("Arial",15,"bold")
#score turtle

score_turtle = turtle.Turtle()
score_turtle.color("dark blue")
score_turtle.write(arg="Score: 0", move=False, align="center", font=font)








turtle.mainloop()