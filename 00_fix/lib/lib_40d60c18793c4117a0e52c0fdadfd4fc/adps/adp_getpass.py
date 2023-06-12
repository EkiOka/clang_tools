import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

getpass = None
# リリース時にはコメントアウトしてください
#import getpass

def __import():
    global getpass
    if getpass == None:
        getpass = pkgs.imp("getpass")

def getuser():
    __import()
    return getpass.getuser()
