# [SNAKE GAME](https://snake-eat-food-game-b47e36d72bf2.herokuapp.com)

This is a simple terminal based snake game implemented in Python. which runs in the Code Institue mock terminal on Heroku. The games features a fun and interactive rendition of the classic snake game we all know and love. Dive into a nostalgic experience as you navigate the snake through the game, avoiding walls and yourself.

![screenshot](documentation/mockup.png)

## User Stories

### New Users
- As a new user, I would like to easily understand how to play the game, so that I can start playing without confusion.
- As a new user, I would like to see the game rules, so that I can learn the gameplay mechanics quickly.
- As a new user, I would like to view the leaderboard, so that I can see high scores and feel motivated to play.
- As a new user, I would like to play the game without creating an account, so that I can quickly engage with the game.
- As a new user, I would like to have a simple and intuitive interface, so that I can navigate the game easily.

### Returning Users
- As a returning user, I would like to see my previous high scores, so that I can track my progress over time.
- As a returning user, I would like to have new challenges or levels, so that I can keep the gameplay interesting.
- As a returning user, I would like to submit my high score, so that I can compete with other players.
- As a returning user, I would like to receive updates about new features, so that I can stay engaged with the game.
- As a returning user, I would like to have the option to provide feedback, so that I can contribute to the game's improvement.

## Flowchart

To follow best practice, a flowchart was created for the app's logic,
and mapped out before coding began using a free version of
[Miro](https://miro.com/index/).

Below is the [flowchart](https://miro.com/app/board/uXjVN8sQUAI=/?utm_source=showme&utm_campaign=cpa) of the main process of this Python program. It shows the entire cycle of the program.

![screenshot](documentation/flowchart.png)

## Features

- **Start Game:** Jump right into the gameplay.

![screenshot](documentation/feature-start-game.png)

- **View Rules:** Get familiar with the game's rules.

![screenshot](documentation/feature-instruction.png)

- **Leaderboard:** Check out high scores.

![screenshot](documentation/feature-leaderboard.png)

### Future Features

***Level Progression System***

Implement different levels with increasing difficulty, such as faster speeds, more complex maps, or additional obstacles. Each level could have a unique theme and design.

***Customizable Snake Skins***

Allow players to customize their snake's appearance with different skins, colors, and patterns. This feature could include unlockable skins based on achievements or high scores.

***Power-Ups and Special Items***

Introduce power-ups that temporarily give the snake special abilities, like invincibility, speed boosts, or extra points. These could appear randomly on the map.

***Leaderboard Enhancements***

Develop a more robust leaderboard system that tracks and displays more detailed statistics, such as the longest playtime, highest average score, and most games played.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) Utilized for structuring the main content of the site.
- [CSS](https://en.wikipedia.org/wiki/CSS) Employed for styling the website. 
- [JavaScript](http://www.javascript.com) Intergral for creating ineractive elements on the site.
- [Python](http://python.org) Used to develop server-side logic and game functions.
- [Git](http://git-scm.com) A version control system used to track changes in the codebase.
- [GitHub](http://github.com) Provides secure online storage for the project's code.
- [Visual Studio Code](http://code.visualstudio.com) Served as the Intergrated Development Environment (IDE) for the project.
- [Heroku](http://heroku.com) A cloud platform used for hosting the deployed back-end of the site.

### Imports

I've used the following Python packages and/or external imported packages.

- `os`: used for adding a `clear()` function
- `gspread`: used with the Google Sheets API
- `re`: used regular expressions
- `google.oauth2.service_account`: used for the Google Sheets API credentials
- `simple_term_menu`: used for including color in the terminal

### Classes & Functions
The snake game is developed using a procedural programming approach with a focus on functions. Below are the primary functions used in the application.

**Functions**

- `update_variables()`
	- Initializes or resets the game's global variables, including the snake's position, food's position, and the initial direction.
	
- `move_snake(snake, direction)`
	- Moves the snake in the specified direction by adding a new head and removing the tail.

- `check_food(snake, food)`
	- Checks if the snake's head has reached the food's position, indicating that the food has been eaten.

- `get_direction(key, current_direction)`
	- Changes the snake's direction based on the user's key input, ensuring the snake does not reverse into itself.

- `generate_food(snake, term)`
	- Generates a new piece of food at a random location on the terminal that is not occupied by the snake.

- `draw_snake(snake, term)`
	- Renders the snake on the terminal, using different colors for the body and the head.

- `draw_food(food, term)`
	- Draws the food on the terminal using a specific color.

- `check_collision_with_wall(head, term)`
	- Checks if the snake's head has collided with the wall (boundary of the terminal).

- `check_collision_with_self(head, snake)`
	- Determines if the snake's head has collided with any part of its body.

- `game_loop()`
	- The main game loop that handles key inputs, updates the game state, draws the game elements, and checks for game over conditions. It also returns the final score when the game ends.

**Data Structures**

- `Point`
	- A named tuple used to represent a point on the screen, with 'y' and 'x' as its elements.

- `Snake`
	- A list of Point objects representing the initial position of the snake.

- `Food`
	- A Point object representing the initial position of the food.

- `Direction`
	- A named tuple used to represent the direction of movement, with 'y' and 'x' as its elements.

These functions and data structures work together to create the interactive gameplay of the snake game. The game is controlled through the terminal, where the player navigates the snake to eat food while avoiding collisions with the walls or itself.

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://snake-eat-food-game-b47e36d72bf2.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/JohnnySonTrinh/snake-game) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/JohnnySonTrinh/snake-game.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JohnnySonTrinh/snake-game)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JohnnySonTrinh/snake-game)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

**Local Development**

- `Environment Setup:` The local development was carried out in a controlled environment, typically on a personal computer. This setup allowed for quick testing and debugging.

- `Access and Testing:` The game was accessible only on the developer's machine, making it convenient for rapid iterations and immediate feedback during the development process.

- `Debugging Tools:` Local development provided the advantage of using comprehensive debugging tools and IDE features, which facilitated efficient problem-solving and code optimization.

- `Configuration:` The local setup might have included specific configurations and dependencies that were tailored to the developer's machine and might not be present in the production environment.

**Live Deployment**

- `Hosting Platform:` The live version of the game was deployed on Heroku, a cloud platform service that enables developers to build, run, and operate applications entirely in the cloud.

- `Accessibility:` Once deployed, the game became publicly accessible, allowing users from anywhere to interact with it, unlike the local version which was confined to the developer's machine.

- `Environment Consistency:` The deployment on Heroku ensured that the game ran in a consistent environment, which might differ from the local development environment in terms of operating system, available libraries, and other factors.

- `Performance Considerations:` In the live deployment, performance and resource utilization became more critical, as the application needed to be optimized for efficient functioning in the cloud environment.

- `Monitoring and Maintenance:` Post-deployment, the focus shifted to monitoring the application’s performance, fixing bugs, and updating features based on user feedback.

## Credits

This section acknowledges the sources and inspirations that contributed to the development of the Snake Game project. Proper credit is given to the original creators and resources that played a pivotal role in shaping this project.

**Code Inspiration**

`Blessed Library's Worms Game:` The game logic for the Snake Game was significantly inspired by the Worms game example from the Blessed Python library. The original code can be found at Blessed Worms Game. This example served as a pseudo-code reference, guiding the development of the game mechanics and functionality in the Snake Game.
Additional Resources
Python Documentation: The official Python documentation was frequently consulted for understanding various Python features and libraries used in the project.

`GitHub Community:` The open-source community on GitHub provided valuable insights and code snippets that were instrumental in solving specific coding problems encountered during development.

### Acknowledgements

- I would like to thank my Mentor, [Julia Konovalova](https://github.com/IuliiaKonovalova), for her invaluable support and guidance throughout the development of this project. Her expertise and insights have been crucial in overcoming challenges and enhancing the overall quality of the game.

- Special thanks to my family and friends for their understanding and support during the times when I was fully immersed in the development process. Their encouragement and belief in my abilities have been a constant source of motivation.

- I appreciate the resources and tutorials available online that have helped me acquire new skills and knowledge essential for this project. The open-source community and various educational platforms have been instrumental in my journey as a developer.