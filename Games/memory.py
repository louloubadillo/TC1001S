"""Memory, puzzle game of number pairs.
Team
Martha del Río
Edgar Rostro
Lourdes Badillo
Exercises:
1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

#decreased the number of total tiles, from 64 to 16
car = path('car.gif')
tiles = list(range(8)) * 2
#add score and tap states
state = {'mark': None, 'score': 0, 'tap': 0}
hide = [True] * 16
counter = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#centered board (4x4)
def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 100) // 50 + ((y + 100) // 50) * 4)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 4) * 50 - 100, (count // 4) * 50 - 100


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    #increment taps
    state['tap'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        #increment score
        state['score'] += 1


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
        

    update()
    ontimer(draw, 100)
    
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
#print final score and total taps
print("Total Taps: ")
print(state["tap"])
print("Final Score: ")
print(state["score"])
#prints a winning banner if the game is completed
if state["score"] == 8:
    print("Ganaste, ¡wuuu!")
