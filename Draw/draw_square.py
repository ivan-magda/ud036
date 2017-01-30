import turtle


def draw_square(interpreter):
    for i in range(1, 5):
        interpreter.forward(100)
        interpreter.right(90)


def draw_art():
    screen = turtle.Screen()
    screen.bgcolor("black")

    interpreter = turtle.Turtle()
    interpreter.color("white")
    interpreter.speed(10)

    for i in range(1, 37):
        draw_square(interpreter)
        interpreter.right(10)

    screen.exitonclick()


draw_art()
