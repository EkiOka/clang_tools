import getpass
import subprocess
import os

open_dir = os.path.dirname(__file__)

for dir_path in os.environ["PATH"].split(os.pathsep):
    path = f"{dir_path}\\..\\code.exe"
    if os.path.exists(path):
        print(f"o : {path}")
        subprocess.Popen(f'{path} "{open_dir}"')
        break
    else:
        print(f"x : {path}")
