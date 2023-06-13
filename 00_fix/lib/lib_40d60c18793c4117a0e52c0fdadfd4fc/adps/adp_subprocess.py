import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

subprocess = None
subprocess_CompletedProcess_bytes = object
# リリース時にはコメントアウトしてください
#import subprocess
#subprocess_CompletedProcess_bytes = subprocess.CompletedProcess[bytes]

def __import():
    global subprocess
    global subprocess_CompletedProcess_bytes
    if subprocess == None:
        subprocess = pkgs.imp("subprocess")
        subprocess_CompletedProcess_bytes = subprocess.CompletedProcess[bytes]

def run(params:list[str])->int:
    __import()
    cp = subprocess.run(params)
    return cp.returncode
