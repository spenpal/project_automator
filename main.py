###########
# IMPORTS #
###########

# Standard Library Imports
import sys
import os
from typing import Dict

# Third Party Library Imports
from github import Github
from dotenv import load_dotenv

########
# CODE #
########

# Loads local .env
load_dotenv()

# GLOBAL VARIABLES
token = os.getenv("TOKEN")


def create(info: Dict) -> None:

    if info['here']:
        path = os.getcwd()
    else:
        path = os.getenv("FILEPATH")
        path = os.path.normpath(path)

    repo_name = info['repo_name']
    user = Github(token).get_user()

    try:
        repo = user.create_repo(repo_name)
    except:
        sys.exit("This repository name already exists on your account!\nTry a different one!")

    repo.create_file("README.md", "Initial commit", f"# {repo_name}")
    os.chdir(path)
    os.system(f"git clone {repo.git_url}")
    print(f"Successfully created remote and local repository: {repo_name}")

    os.chdir(repo_name)
    os.system("code .")


def create_remote(info: Dict) -> None:

    if info['here']:
        path = os.getcwd()
    else:
        path = os.getenv("FILEPATH")
        path = os.path.normpath(path)

    repo_name = info['repo_name']
    full_path = os.path.join(path, repo_name)
    if not os.path.isdir(full_path):
        sys.exit('Local repository not found!\nTry again!')

    user = Github(token).get_user()

    try:
        repo = user.create_repo(repo_name)
    except:
        sys.exit("This repository name already exists on your account!\nTry a different one!")

    os.chdir(full_path)
    os.system(f"git remote add origin {repo.clone_url}")
    os.system("git branch -M main")
    os.system("git push -u origin main")

    print(f"Successfully created remote repository: {repo_name}")


def create_local(info: Dict) -> None:

    if info['here']:
        path = os.getcwd()
    else:
        path = os.getenv("FILEPATH")
        path = os.path.normpath(path)

    repo_name = info['repo_name']
    user = Github(token).get_user()

    try:
        repo = user.get_repo(repo_name)
    except:
        sys.exit("This repository name does not exist on your account!\nTry again!")

    os.chdir(path)
    os.system(f"git clone {repo.git_url}")
    print(f"Successfully cloned repository: {repo_name}")

    os.chdir(repo_name)
    os.system("code .")


if __name__ == "__main__":

    # Edge Cases
    args = sys.argv[1:]
    if len(args) > 3:
        sys.exit("Too many arguments!\nTry again!")
    if sys.argv[-1].startswith('-'):
        sys.exit("No project name found!\nMake sure you type it at the end of the command!\nTry again!")

    ALL_FLAGS = {'-h', '-r', '-l'}

    # Reduce all flags to one letter flags
    options = set()
    for i in range(len(args) - 1):
        start_index = args[i].rfind('-')
        short_flag = args[i][start_index: start_index + 2]
        options.add(short_flag)

    # Check if -r and -l flag are both entered
    if '-r' in options and '-l' in options:
        sys.exit("Cannot use -r and -l flag at the same time!\nMaybe use the basic 'create' command...\nTry again!")

    # Check if all flags entered are valid
    for option in options:
        if option not in ALL_FLAGS:
            sys.exit("One or more invalid flags entered!\nTry again!")

    args_info = {
        'repo_name': sys.argv[-1],
        'here': '-h' in options,
    }

    if '-r' in options:
        create_remote(args_info)
    elif '-l' in options:
        create_local(args_info)
    else:
        create(args_info)
