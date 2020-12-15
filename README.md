# Project Automator
> Creates your project automatically, from folder creation to linking your project to Github

---
## How It Works
> [Insert text]

---
## Initial Steps
1. `git clone https://github.com/spenpal2000/project_automator.git`
2. `cd project_automator`
3. `touch .env`
4. `code .env`
5. Paste the following into the .env file
    ```
    TOKEN=""
    FILEPATH=""
    ```
    - *To Get The Token...*
        - To get a token from your Github account, go to the [tokens](https://github.com/settings/tokens) page and click **Generate new token**
        - For the note, put something like "Project Automator", to indicate you are using the token for this repo
        - In the **Select scopes** section, only checkbox **repo**
        - Click **Generate token** at the bottom
        - Copy and paste the generated token into the `TOKEN=""` field, inside the quotes
    - *To Get The Filepath...*
        - Choose a file location where you generally keep all of your projects/repos or create a brand new folder for this!
        - Copy the file path to that directory into the `FILEPATH=""` field, inside the quotes
6.  `cd ~`
7.  `code .bashrc`
    - Copy the file path to `.my_commands.sh` and paste it into the command, as shown below
    - `source "/c/the/path/to/my/project_automator/.my_commands.sh"`
    - After saving `.bashrc`, reboot the terminal. If you get this warning: `WARNING: Found ~/.bashrc but no ~/.bash_profile, ~/.bash_login or ~/.profile.`, just ignore it and continue on
8. And that's it! You are all set to use the `create` command whenever you want to start up a project!
    
---
## Command Usage
```
Usage:   
  create [options] <repo_name> 

General Options:
  -h, --here                    Execute the command at your current working directory
  -r, --remote                  If you have a local repo and want to create a remote repo.
  -l, --local                   If you have a remote repo and want to create a local repo (Equivalent of using `git clone`)
```

---
## Remarks
1. Make sure this is not your first time using Github or Git
    - The script assumes that you have your Github credentials saved in your OS' credential manager 
2. Have [Python](https://www.python.org/downloads/) installed on your system (The script is in Python, duh...)
3. Have [Visual Studio Code](https://code.visualstudio.com/download) installed on your system (Probably the best text editor you will ever see in your life)
