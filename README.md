# Project Automator
![](https://img.shields.io/github/license/spenpal2000/project_automator) ![](https://img.shields.io/github/stars/spenpal2000/project_automator)  
Project Automator is a custom command that automates the process of creating a local repository, remote repository, and linking both repositories, when starting a new project.

## Demo
```
create test_repo
```
![](https://media.giphy.com/media/VosyQmlyWpIfaV99qb/giphy.gif)

```
create -h -l test_repo
```
![]()

```
create -p -r test_repo
```
![]()

## Before You Get Started...
1. Make sure this is not your first time using Github or Git
    - The script assumes that you have your Github credentials saved in your OS's credential manager 
2. Have [Python](https://www.python.org/downloads/) installed on your system (*Python 3.6 or greater*)
3. Have [Visual Studio Code](https://code.visualstudio.com/download) installed on your system (*Probably the best text editor you will ever see in your life*)
4. Use the Bash or Git Bash terminal

## Installation
```
git clone https://github.com/spenpal2000/project_automator.git
cd project_automator
pip install -r requirements.txt
code .env
```
### Env File Format
```
TOKEN=""
FILEPATH=""
```
- *To Get The Token...*
    - Go to Github's [tokens](https://github.com/settings/tokens) page
    - `Generate new token`
    - `Note: Project Automator`
    - In the `Select scopes` section, **only** checkmark `repo`
    - Click `Generate token` at the bottom
    - Paste the generated token into the `TOKEN=""` field, inside the quotes
- *To Get The Filepath...*
    - Choose a file location to store your projects/repos **or** create a brand new folder for this!
    - Paste the file path to that directory into the `FILEPATH=""` field, inside the quotes
```
cd ~
code .bashrc
```

### Bashrc File Format
```
source "~/the/path/to/project_automator/.my_commands.sh"
```
- Restart the terminal
- And that's it! You are all set to use the `create` command whenever you want to start up a project!
- **You do not have to repeat these steps after you have done it once!**
    
## Command Usage
```
Usage:
    create [options] <repo_name> 

General Options:
        --help                  Show help.
    -h, --here                  Use current working directory as the FILEPATH.
    -l, --local                 If you have an existing remote repo and want to create a local repo 
                                (Equivalent of using `git clone`).
    -p, --private               Creates a private, remote repository.
    -r, --remote                If you have an exisiting local repo and want to create a remote repo.

NOTE:
    --local & --remote (or -l & -r) cannot be used simulateneously,
    as that is suggestive of the basic 'create' command
```
