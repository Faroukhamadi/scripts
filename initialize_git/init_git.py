import os
from sys import argv


def init_git():
    print(f"Initializing new git repository in {argv[1]}")
    os.system(f"echo \"# {argv[1]}\" >> README.md")
    os.system("git init")
    os.system(f"git add {argv[2]}")
    os.system("git commit -m \"first commit\"")
    os.system("git branch -M main")
    os.system(
        f"git remote add origin git@github.com:Faroukhamadi/{argv[1]}.git"
    )
    os.system("git push -u origin main")


init_git()
