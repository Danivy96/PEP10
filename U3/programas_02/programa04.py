import turtle


def dibujar():
    dibujo = turtle.Screen()
    dibujo.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)
    t.pensize(2)

    # Donde empieza para dibujar el cuadrado
    t.penup()
    t.goto(-150, 0)
    t.pendown()

    t.color("red")
    for _ in range(4):
        t.forward(100)
        # Angulo de girto
        t.left(90)

    # Donde empieza para dibujar el circulo
    t.penup()
    t.goto(150, 0)
    t.pendown()

    t.color("black", "green")
    t.begin_fill()
    # tamaño
    t.circle(100)
    t.end_fill()


dibujar()
