from random import randrange
from collections import namedtuple
from blessed import Terminal


# Define the basic data structures for the game.
Point = namedtuple('Point', ['y', 'x'])  # Represents a point on the screen.
Snake = [Point(5, 5), Point(5, 6), Point(5, 7)]  # Initial snake position
Food = Point(randrange(10), randrange(10))  # Initial food position
Direction = namedtuple('Direction', ['y', 'x'])  # Represents a direction.
direction = Direction(0, 1)  # Initial direction: right
