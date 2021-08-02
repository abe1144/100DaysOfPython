# import colorgram
# colors = colorgram.extract('dot.jpg', 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

import turtle as t
import random
color_list = [(239, 229, 87), (194, 10, 72), (205, 159, 100), (112, 179, 206), (165, 170, 31), (25, 117, 172), (213, 137, 168), (162, 72, 36), (8, 35, 83), (31, 136, 73), (240, 224, 3), (121, 182, 139), (236, 67, 39), (214, 82, 128), (81, 19, 78), (12, 59, 35), (238, 162, 190), (177, 46, 91), (15, 43, 126), (122, 37, 22), (7, 102, 62), (21, 168, 199), (6, 87, 98), (146, 207, 219), (159, 210, 185),
              (80, 159, 83)]

# 10 by 10 spots
# 20 diameter, spacing 50 in between
t.colormode(255)
x = t.Turtle()
x.speed("fastest")
x.penup()
x.setpos(-240, -300)

for _ in range(10):
    x.setx(-240)
    vertical = x.ycor()
    new_vertical = vertical + 50
    x.sety(new_vertical)
    for _ in range(9):
        x.color(random.choice(color_list))
        x.dot(20)
        horizontal = x.xcor()
        new_horizontal = horizontal + 50
        x.setx(new_horizontal)
        x.dot(20)

screen = t.Screen()
screen.exitonclick()
