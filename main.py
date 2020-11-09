###########
# IMPORTS #
###########

# Standard Library Imports
import sys
import os

# Third Party Library Imports
from github import Github
from dotenv import load_dotenv
import pygit2

########
# CODE #
########
load_dotenv()   # Loads local .env with Github information

# GLOBAL VARIABLES
token = os.getenv("TOKEN")
path = os.getenv("FILEPATH")


def create():
    folderName = str(sys.argv[1])
    user = Github(token).get_user()
    
    try:
        repo = user.create_repo(folderName)
    except:
        sys.exit("This repository name already exists on your account! Try a different one!")
        
    repo.create_file("README.md", "Initial commit", f"# {folderName}")
    pygit2.clone_repository(repo.git_url, f"{path}\{str(folderName)}")
    print(f"Successfully created repository: {folderName}")
    os.chdir(f"{path}\{str(folderName)}")
    os.system("code .")


if __name__ == "__main__":
    create()