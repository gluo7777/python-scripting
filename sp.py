import subprocess as sp
import os

def check_git_exec():
    cp = sp.run(['git', '--version'], capture_output=True, text=True)
    if 'git version' in cp.stdout:
        return True
    return False

def upload():
    if not check_git_exec():
        print('Git is not installed', err=True)
        return
    file = os.path.abspath('.') + '/' + '.gitignore'
    if not os.path.exists(file):
        print('No .gitignore in this directory', err=True)
        return
    print('initializing local repo and committing files')
    sp.run(['git','init','.'])
    sp.run(['git','add','.'])
    sp.run(['git','commit','-m','First Commit'])
    print('adding remote origin')
    sp.run(['git', 'remote', 'add', 'origin','random'])
    print('uploading to upstream')
    # sp.run(['git','push','-u','origin','master'])

# upload()

print(os.path.exists(os.path.abspath('.') + '/' + '.git'))