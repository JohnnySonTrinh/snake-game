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


def get_direction(key, current_direction):
    """
    Changes the snake's direction based on the key pressed.
    Prevents the snake from reversing directly into itself.
    """
    if key.name == "KEY_UP" and current_direction != Direction(1, 0):
        return Direction(-1, 0)
    elif key.name == "KEY_DOWN" and current_direction != Direction(-1, 0):
        return Direction(1, 0)
    elif key.name == "KEY_LEFT" and current_direction != Direction(0, 1):
        return Direction(0, -1)
    elif key.name == "KEY_RIGHT" and current_direction != Direction(0, -1):
        return Direction(0, 1)
    return current_direction


def generate_food(snake, term):
    """
    Generates a new piece of food at a random location
    not occupied by the snake.
    """
    while True:
        new_food = Point(randrange(1, term.height), randrange(1, term.width))
        if new_food not in snake:
            return new_food


def draw_snake(snake, term):
    """
    Draws the snake on the terminal.
    Uses green for the body and red for the head.
    """
    for segment in snake:
        with term.location(segment.x, segment.y):
            print(term.on_green(' '), end='')

    head = snake[-1]
    with term.location(head.x, head.y):
        print(term.on_red(' '), end='')
