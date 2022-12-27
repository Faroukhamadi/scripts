import os
from sys import argv


def init_git():
    # get repository name from folder
    repo_name = argv[1].split('/')[-1]

    print(f"Initializing new git repository in {argv[1]}")
    os.system(f"echo \"# {repo_name}\" >> README.md")
    os.system("git init")
    os.system(f"git add {argv[1]}")
    os.system("git commit -m \"first commit\"")
    os.system("git branch -M main")
    os.system(
        f"git remote add origin git@github.com:Faroukhamadi/{repo_name}.git"
    )
    os.system("git push -u origin main")


init_git()
