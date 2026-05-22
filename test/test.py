import os
import turtle
print("сак")

def draw_it():
    # Настройки экрана и скорости
    screen = turtle.Screen()
    screen.setup(600, 600)
    t = turtle.Turtle()
    t.speed(10)  # Максимальная скорость отрисовки
    t.pensize(5)

    # Левое яичко
    t.penup()
    t.goto(-40, -100)
    t.pendown()
    t.circle(40)

    # Правое яичко
    t.penup()
    t.goto(40, -100)
    t.pendown()
    t.circle(40)

    # Ствол (поднимаемся вверх)
    t.penup()
    t.goto(-40, -20)
    t.pendown()
    t.left(90)
    t.forward(150)  # Высота

    # Шляпка (полукруг наверху)
    t.right(90)
    t.circle(-40, 180)

    # Спускаемся обратно вниз
    t.forward(150)

    # Прячем черепашку, чтобы не мешала обзору
    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    draw_it()
