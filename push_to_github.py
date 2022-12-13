import os

def deploy():
    os.system("git add .")
    os.system("git commit -m 'deploy'")
    os.system("git push")
