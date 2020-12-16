###########
# IMPORTS #
###########

# Standard Library Imports
import sys
import os
from subprocess import run

# Third Party Library Imports
from github import Github
from dotenv import load_dotenv

# GLOBAL VARIABLES
load_dotenv()                   # Loads local .env
token = os.getenv("TOKEN")      # Gets Github OAuth Token
path = os.getenv("FILEPATH")    # Gets Project/Repos Directory
path = os.path.normpath(path)   # Normalizes Filepath

#############
# FUNCTIONS #
#############

def error():
    msg = """\
    Usage: create [options] <repo_name>
    Try 'create --help' for more information.
    """
    sys.exit(msg)
    
    
def help():
    msg = """\
    Usage:
    create [options] <repo_name> 

    General Options:
            --help                    Show help.
        -h, --here                    Execute the command at your current working directory.
        -l, --local                   If you have a remote repo and want to create a local repo (Equivalent of using `git clone`).
        -p, --private                 Creates a private, remote repository.
        -r, --remote                  If you have a local repo and want to create a remote repo.
  
    NOTE:
        --remote & --local (or -r & -l) cannot be used simulateneously, as that is suggestive of the basic 'create' command
    """
    sys.exit(msg)
    
    
def create(info):     

    if info['here']:
        path = os.getcwd()
        
    repo_name = info['repo_name']
    user = Github(token).get_user()

    try:
        repo = user.create_repo(repo_name, private=info['private'])
    except:
        sys.exit("This repository name already exists on your account!\nTry a different one!")

    repo.create_file("README.md", "Initial commit", f"# {repo_name}")
    os.chdir(path)
    run(['git', 'clone', repo.git_url], shell=False)
    print(f"Successfully created remote and local repository: {repo_name}")

    os.chdir(repo_name)
    run(['code', '.'], shell=False)


def create_remote(info):

    if info['here']:
        path = os.getcwd()

    repo_name = info['repo_name']
    full_path = os.path.join(path, repo_name)
    if not os.path.isdir(full_path):
        sys.exit('Local repository not found!\nTry again!')

    user = Github(token).get_user()

    try:
        repo = user.create_repo(repo_name, private=info['private'])
    except:
        sys.exit("This repository name already exists on your account!\nTry a different one!")

    os.chdir(full_path)
    run(['git', 'remote', 'add', 'origin', repo.clone_url], shell=False)
    run(['git', 'branch', '-M', 'main'], shell=False)
    run(['git', 'push', '-u', 'origin', 'main'], shell=False)
    print(f"Successfully created remote repository: {repo_name}")


def create_local(info):

    if info['here']:
        path = os.getcwd()

    repo_name = info['repo_name']
    user = Github(token).get_user()

    try:
        repo = user.get_repo(repo_name)
    except:
        sys.exit("This repository name does not exist on your account!\nTry again!")

    os.chdir(path)
    run(['git', 'clone', repo.git_url], shell=False)
    print(f"Successfully cloned repository: {repo_name}")

    os.chdir(repo_name)
    run(['code', '.'], shell=False)


#############
# MAIN CODE #
#############

if __name__ == "__main__":

    ## EDGE CASES ##
    args = sys.argv[1:]
    
    # Display help page if --help is entered
    if '--help' in args:
        help()
    
    # If too many or too little args are entered OR the last argument is not a repo_name
    if not (1 < len(args) < 3) or args[-1].startswith('-'):
        error()

    # Check if all flags entered are valid
    ALL_FLAGS = {'--help', '-h', '--here', '-l', '--local', '-p', '--private', '-r', '--remote'}
    for option in args[:-1]:
        if option not in ALL_FLAGS:
            error()
            
    # Reduce all flags to one letter flags
    options = set()
    for option in args[:-1]:
        start_index = option.rfind('-')
        short_flag = option[start_index: start_index + 2]
        options.add(short_flag)

    # Check if -r and -l flag are both entered
    if '-r' in options and '-l' in options:
        error()

    
    ## FUNCTION CALLS ##
    args_info = {
        'repo_name': args[-1],
        'here': '-h' in options,
        'private': '-p' in options
    }

    if '-r' in options:
        create_remote(args_info)
    elif '-l' in options:
        create_local(args_info)
    else:
        create(args_info)
