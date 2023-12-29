import gspread
import os
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu


SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('snake-game-scoreboard')


def clear():
    """
    Clears the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_scoreboard():
    """
    Get the scoreboard from the spreadsheet
    """
    scoreboard = SHEET.worksheet('scoreboard')

    data = scoreboard.get_all_values()

    return data

def start_game():
    clear()
    # Logic to start the game
    print("Game starting...")

