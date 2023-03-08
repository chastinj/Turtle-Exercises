# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
# num_sides = 5

colors = ["PaleGreen", "MediumBlue", "Purple", "PowderBlue", "orange2", "OliveDrab4", "LightSteelBlue", "OrangeRed1",
          "NavyBlue","CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
          "SeaGreen"]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


'''for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


tim.clear()'''

tim.pensize(10)
speeds = [2, 4, 5, 6, 7, 3, 10, 7, 5, 6, 8]
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


# for i in range(200):
#     tim.forward(40)
#     tim.speed(random.choice(speeds))
#     tim.pencolor(random_color())  # or tim.color(random.choice(colors))
#     tim.setheading(random.choice(directions))

# tim.clear()

# Draw a Spirograph
tim.pensize(3)
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.left(size_of_gap)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
