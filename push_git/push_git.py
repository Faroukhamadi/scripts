import os
from sys import argv


def push_git():
    print("Pushing to git")
    os.system(f"cd {argv[1]}")
    os.system(f"git add .")
    os.system(f"git commit -m \"{argv[2]}\"")
    os.system("git push")


push_git()
