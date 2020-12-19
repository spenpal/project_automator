# Project Automator

![](https://img.shields.io/github/license/spenpal2000/project_automator)
![](https://img.shields.io/github/stars/spenpal2000/project_automator)

Project Automator is a custom command that automates the process of creating a local repository, remote repository, and linking both repositories, when starting a new project.

## Command Usage

```text
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

## Demo

```text
create test_repo
```

![](https://media.giphy.com/media/VosyQmlyWpIfaV99qb/giphy.gif)

```bash
create -h -l test_repo
```

![](https://media.giphy.com/media/INIqDRkJdkNAHnyzYj/giphy.gif)

```bash
create -p -r test_repo
```

![](https://media.giphy.com/media/Af0dccMz0xKDR9oYoy/giphy.gif)

## Before You Get Started

1. Make sure this is not your first time using Github or Git
   - The script assumes that you have your Github credentials saved in your OS's credential manager
2. Have [Python](https://www.python.org/downloads/) installed on your system (_Python 3.6 or greater_)
3. Have [Visual Studio Code](https://code.visualstudio.com/download) installed on your system (_Probably the best text editor you will ever see in your life_)
4. Use the Bash or [Git Bash](https://git-scm.com/downloads) terminal

## Installation

```bash
git clone https://github.com/spenpal2000/project_automator.git
cd project_automator
pip install -r requirements.txt
code .env
```

### Env File Format

```env
TOKEN=""
FILEPATH=""
```

- _To Get The Token..._
  - Go to Github's [tokens](https://github.com/settings/tokens) page
  - `Generate new token`
  - `Note: Project Automator`
  - In the `Select scopes` section, **only** checkmark `repo`
  - Click `Generate token` at the bottom
  - Paste the generated token into the `TOKEN=""` field, inside the quotes
- _To Get The Filepath..._
  - Choose a file location to store your projects/repos **or** create a brand new folder for this!
  - Paste the file path to that directory into the `FILEPATH=""` field, inside the quotes

```bash
cd ~
code .bashrc
```

### Bashrc File Format

```bash
source "~/the/path/to/project_automator/.my_commands.sh"
```

- Restart the terminal
- And that's it! You are all set to use the `create` command whenever you want to start up a project!
- **You do not have to repeat these steps after you have done it once!**
