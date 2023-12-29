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


def draw_food(food, term):
    """
    Draws the food on the terminal using a yellow color.
    """
    with term.location(food.x, food.y):
        print(term.on_yellow(' '), end='')


def check_collision_with_wall(head, term):
    """
    Checks if the snake's head has collided with the wall
    (boundary of the terminal).
    Returns True if a collision occurred.
    """
    return (
    head.x < 0 or head.x >= term.width or 
    head.y < 0 or head.y >= term.height
)



def check_collision_with_self(head, snake):
    """
    Checks if the snake's head has collided with any part of its body.
    Returns True if a collision occurred.
    """
    return head in snake[:-1]


def game_loop():
    """
    The main game loop.
    Handles key inputs, updates the game state, draws the game,
    and checks for game over conditions.
    Returns the final score when the game is over.
    """
    term = Terminal()
    global Snake, Food, direction

    score = 0
    base_speed = 0.1
    speed_increase_factor = 0.005

    with term.cbreak(), term.hidden_cursor():
        while True:
            speed = max(0.05, base_speed - speed_increase_factor * score)
            key = term.inkey(timeout=speed)
            if key.is_sequence:
                direction = get_direction(key, direction)

            head = Snake[-1]
            next_head = Point(head.y + direction.y, head.x + direction.x)

            Snake.append(next_head)
            if next_head == Food:
                Food = generate_food(Snake, term)
                score += 10
            else:
                Snake.pop(0)

            print(term.home + term.clear)
            draw_snake(Snake, term)
            draw_food(Food, term)

            print(f"{score}")

            if (check_collision_with_wall(next_head, term) or 
            check_collision_with_self(next_head, Snake)):
                return score



if __name__ == '__main__':
    game_loop()
