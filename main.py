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
token = os.getenv('TOKEN')      # Gets Github OAuth Token
path = os.getenv('FILEPATH')    # Gets Project/Repos Directory
path = os.path.normpath(path)   # Normalizes Filepath

#############
# FUNCTIONS #
#############

def format(msg):
    lines = msg.split('\n')
    tab_size = 4
    lines = [line[tab_size:] for line in lines]
    return '\n'.join(lines)
    
    
def error(e):
    msg = '''\
    Usage: create [options] <repo_name>
    Try 'create --help' for more information.'''
    print(format(msg))
    print('\n' + e)
    sys.exit(0)
    
    
def help():
    msg = '''
    Usage:
        create [options] <repo_name> 

    General Options:
            --help                  Show help.
        -h, --here                  Execute the command at your current working directory.
        -l, --local                 If you have a remote repo and want to create a local repo 
                                    (Equivalent of using `git clone`).
        -p, --private               Creates a private, remote repository.
        -r, --remote                If you have a local repo and want to create a remote repo.
  
    NOTE:
        --local & --remote (or -l & -r) cannot be used simulateneously, 
        as that is suggestive of the basic 'create' command'''
    print(format(msg))
    sys.exit(0)
    
    
def create(info):     

    global path
    if info['here']:
        path = os.getcwd()
        
    repo_name = info['repo_name']
    user = Github(token).get_user()

    try:
        repo = user.create_repo(repo_name, private=info['private'])
    except:
        print('ERROR: remote repository already exists.')
        sys.exit(0)

    # git clone method
    repo.create_file('README.md', 'Initial commit', f'# {repo_name}')
    os.chdir(path)
    run(['git', 'clone', repo.clone_url], shell=False)
    print(f'Successfully created remote and local repository: {repo_name}')

    os.chdir(repo_name)
    run(['code', '.'], shell=True)
    
    
def create_remote(info):

    global path
    if info['here']:
        path = os.getcwd()

    repo_name = info['repo_name']
    full_path = os.path.join(path, repo_name)
    if not os.path.isdir(full_path):
        print('ERROR: repository not found.')
        sys.exit(0)

    user = Github(token).get_user()

    try:
        repo = user.create_repo(repo_name, private=info['private'])
    except:
        print('ERROR: remote repository already exists.')
        sys.exit(0)

    os.chdir(full_path)
    run(['git', 'remote', 'add', 'origin', repo.clone_url], shell=False)
    run(['git', 'branch', '-M', 'main'], shell=False)
    run(['git', 'push', '-u', 'origin', 'main'], shell=False)
    print(f'Successfully created remote repository: {repo_name}')


def create_local(info):

    global path
    if info['here']:
        path = os.getcwd()

    repo_name = info['repo_name']
    user = Github(token).get_user()

    try:
        repo = user.get_repo(repo_name)
    except:
        print('ERROR: remote repository does not exist.')
        sys.exit(0)

    os.chdir(path)
    run(['git', 'clone', repo.clone_url], shell=False)
    print(f'Successfully cloned repository: {repo_name}')

    os.chdir(repo_name)
    run(['code', '.'], shell=True)


#############
# MAIN CODE #
#############

if __name__ == '__main__':

    ## EDGE CASES ##
    args = sys.argv[1:]
    
    # Display help page if --help is entered
    if '--help' in args:
        help()
    
    # If too many or too little args are entered OR the last argument is not a repo_name
    if not (1 <= len(args) <= 3):
        error_msg = 'ERROR: Too few or too many arguments entered.'
        error(error_msg)
    elif args[-1].startswith('-'):
        error_msg = 'ERROR: repo_name not found.'
        error(error_msg)

    # Check if all options entered are valid
    ALL_OPTIONS = {'--help', '-h', '--here', '-l', '--local', '-p', '--private', '-r', '--remote'}
    for option in args[:-1]:
        if option not in ALL_OPTIONS:
            error_msg = f'ERROR: unknown option '{option}''
            error(error_msg)
            
    # Reduce all flags to one letter flags
    options = set()
    for option in args[:-1]:
        start_index = option.rfind('-')
        short_flag = option[start_index: start_index + 2]
        options.add(short_flag)

    # Check if -l and -r flag are both entered
    if '-l' in options and '-r' in options:
        error_msg = 'ERROR: cannot use -l and -r flag simultaneously'
        error(error_msg)

    
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
