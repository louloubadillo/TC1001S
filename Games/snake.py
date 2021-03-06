"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

Edgar Rostro
Lulú Badillo
Martha del Río
"""

from turtle import *
from random import randrange
from freegames import square, vector
from random import choice

food = vector(0, 0)
aimf = vector(0, 10)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    bgcolor('lightblue')
    head = snake[-1].copy()
    head.move(aim)
    
    # make the snake go around the edges
    if  head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    #left edge
    if head.x < -200:
        head.x = 190

    #upper edge
    if head.y > 190:
        head.y = -200

    #right edge
    if head.x > 190:
        head.x = -200

    #lower edge
    if head.y < -200:
        head.y = 190 

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()
    
    for body in snake:
        square(body.x, body.y, 9, 'black')

    #change color of food, so it looks like a disco ball
    value = randrange(0, 3)
    colors = ['blue', 'orange', 'green', 'yellow']
    square(food.x, food.y, 9, colors[value])

    #change position of food 
    options = [
        vector(10, 0),
        vector(-10, 0),
        vector(0, 10),
        vector(0, -10),
    ]
    plan = choice(options)
    aimf.x = plan.x
    aimf.y = plan.y
    food.move(aimf)

    # for positionf, aimf in food:
    #     #change color of food, so it looks like a disco ball
    #     value = randrange(0, 3)
    #     colors = ['blue', 'orange', 'green', 'yellow']
    #     square(positionf.x, positionf.y, 9, colors[value])
        
    #     #change position of food 
    #     options = [
    #         vector(10, 0),
    #         vector(-10, 0),
    #         vector(0, 10),
    #         vector(0, -10),
    #     ]
        
    #     plan = choice(options)

    #     aimf.x = plan.x
    #     aimf.y = plan.y
    #     positionf.move(aimf)

    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# arrow keys functionality
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

