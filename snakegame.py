from random import randrange
from collections import namedtuple
from blessed import Terminal


# Define the basic data structures for the game.
Point = namedtuple('Point', ['y', 'x'])  # Represents a point on the screen.
Snake = [Point(5, 5), Point(5, 6), Point(5, 7)]  # Initial snake position
Food = Point(randrange(10), randrange(10))  # Initial food position
Direction = namedtuple('Direction', ['y', 'x'])  # Represents a direction.
direction = Direction(0, 1)  # Initial direction: right


def move_snake(snake, direction):
    """
    Moves the snake in the specified direction.
    Adds a new head to the snake in the direction
    of movement and removes the tail.
    """
    head = snake[-1]
    new_head = Point(head.y + direction.y, head.x + direction.x)
    snake.append(new_head)
    snake.pop(0)


def check_food(snake, food):
    """
    Checks if the snake's head is at the same location as the food.
    Returns True if the snake has eaten the food.
    """
    if snake[-1] == food:
        return True
    return False
