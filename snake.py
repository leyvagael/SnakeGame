"""Snake, classic arcade game.

Exercises

(done)
1. How do you make the snake faster or slower?

2. How can you make the snake go around the edges?

3. How would you move the food?
(done)
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

colors = ['plum', 'skyblue', 'lightgreen', 'pink', 'coral']
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

snake_color = choice(colors)

def random_food_color():
    """Generate random color for food."""
    food_color = choice(colors)

    while snake_color == food_color:
        food_color = choice(colors)

    return food_color

food_color = random_food_color()

def move_food():
    """Makes food move every 200ms, checks that new position isn't out of range"""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    step = choice(directions)
    new_x = food.x + step.x
    new_y = food.y + step.y

    if -150 <= new_x <= 140 and -150 <= new_y <= 140:
        food.x = new_x
        food.y = new_y

    ontimer(move_food, 200)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(obj):
    """Return True if object inside boundaries."""
    return -200 < obj.x < 190 and -200 < obj.y < 190

def mouse(x, y):
    """Control snake with mouse clicks."""
    head = snake[-1]

    if abs(x - head.x) > abs(y - head.y):

        if x > head.x:
            change(10, 0)
        else:
            change(-10, 0)

    else:

        if y > head.y:
            change(0, 10)
        else:
            change(0, -10)

def move():
    """Move snake forward one segment."""
    global food_color
    head = snake[-1].copy()
    head.move(aim)


    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        food_color = random_food_color()
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 76)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onscreenclick(mouse)
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()
done()
