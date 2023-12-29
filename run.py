import gspread
import os
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open("snake-game-scoreboard")


def clear():
    """
    Clears the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_scoreboard():
    """
    Get the scoreboard from the spreadsheet
    """
    scoreboard = SHEET.worksheet("scoreboard")

    data = scoreboard.get_all_values()

    return data


def start_game():
    clear()
    # Logic to start the game
    print("Game starting...")


def show_instructions():
    clear()
    # Logic to show game instructions
    print("\033" +
          "================= Instructions for Snake Game =================" +
          "\033")
    print("\n\033[1mGameplay:\033[0m")
    print("Your goal is to control the snake and help it eat as many food")
    print("items as possible. The game continues until the snake either")
    print("runs into the wall or into itself.")
    print("Be careful not to run into the walls or the snake's own tail.")
    print("\033[1mControls:\033[0m")
    print("- Use the arrow keys to control the direction of the snake.")
    print("- Press 'P' to pause the game.")
    print("- Press 'Q' to quit the game and return to the main menu.")
    print("\n\033" +
          "===============================================================" +
          "\033")
    print("\nPress 'Enter' to return to the main menu.")
    while True:
        user_input = input()
        if user_input == "":
            break
        else:
            break
    main()
