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

### Imports

I've used the following Python packages and/or external imported packages.

- `os`: used for adding a `clear()` function
- `gspread`: used with the Google Sheets API
- `re`: used regular expressions
- `google.oauth2.service_account`: used for the Google Sheets API credentials
- `simple_term_menu`: used for including color in the terminal

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
