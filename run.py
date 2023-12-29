import gspread
import os
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu
from snakegame import game_loop


# Google Sheets API setup
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
    Clears the terminal screen for both Windows ('cls') and Unix ('clear').
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_scoreboard():
    """
    Retrieves the current leaderboard from the Google Sheets spreadsheet.
    """
    scoreboard = SHEET.worksheet("leaderboard")

    data = scoreboard.get_all_values()

    return data


def show_leaderboard():
    """
    Retrieves and displays the top 10 leaderboard entries.
    """
    clear()
    scores = get_scoreboard()
    formatted_scores = format_leaderboard(scores)
    print("Leaderboard (Top 10):")
    print(formatted_scores)
    print("\nPress 'Enter' to return to the main menu.")
    while True:
        user_input = input("\n")
        if user_input == "":
            break
        else:
            break
    main()


def format_leaderboard(data):
    """
    Formats the leaderboard data into a readable table format.
    """
    header = "\033[1m{:<30} {:<15}\033[0m".format("Name", "Score")
    divider = "-" * 47
    formatted_data = [header, divider]

    top_ten = data[1:11]
    for name, score in top_ten:
        formatted_data.append("{:<30} {:<15}".format(name, score))

    return "\n".join(formatted_data)


def update_scoreboard(name, score):
    """
    Updates the 'scoreboard' worksheet in Google Sheets with
    the player's name and score.
    """
    worksheet = SHEET.worksheet("scoreboard")
    worksheet.append_row([name, score])


def is_score_a_highscore(player_score, leaderboard):
    """
    Determines if the player's score qualifies as a high score.
    Checks if the score is higher than the lowest score in the top 10.
    """
    if len(leaderboard) < 10:
        return True
    lowest_highscore = min(int(entry[1]) for entry in leaderboard[1:])
    return player_score > lowest_highscore


def start_game():
    """
    Starts the snake game, checks the final score,
    and updates the leaderboard if necessary.
    """
    clear()
    final_score = game_loop()
    game_loop()
    clear()

    leaderboard = get_scoreboard()
    if is_score_a_highscore(final_score, leaderboard):
        print(f"\nFinal score: {final_score}")
        print("\nCongratulations, you made it to the leaderboard!")
        player_name = input("Enter your name:\n")
        update_scoreboard(player_name, final_score)
        exit()
    else:
        print("You didn't make it to the leaderboard. Better luck next time!")
        print(f"Final score: {final_score}")
        exit()


def show_instructions():
    """
    Displays the game instructions and waits for
    the user to return to the main menu.
    """
    clear()
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
        user_input = input("\n")
        if user_input == "":
            break
        else:
            break
    main()


def main():
    """
    Main function to run the terminal-based menu.
    Allows users to start the game, view instructions,
    see the leaderboard, or quit.
    """
    clear()
    print("\033" +
          "================================================================")
    print("                     Welcome to Snake Game!")
    print("===============================================================" +
          "\033")
    print("\nPlease select an option:")
    options = ["Start", "Instructions", "Leaderboards", "Quit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    choice = options[menu_entry_index]

    if choice == "Start":
        start_game()
    elif choice == "Instructions":
        show_instructions()
    elif choice == "Leaderboards":
        show_leaderboard()
    elif choice == "Quit":
        print("Exiting game. Thanks for playing!")
        exit()


if __name__ == "__main__":
    main()
