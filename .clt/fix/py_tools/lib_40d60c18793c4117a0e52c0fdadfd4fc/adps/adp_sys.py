import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

sys = None
# リリース時にはコメントアウトしてください
#import sys

def __import():
    global sys
    if sys == None:
        sys = pkgs.imp("sys")

def exit(error_code:int):
    __import()
    sys.exit(error_code)

def argv()->list[str]:
    __import()
    return sys.argv

def path()->list[str]:
    __import()
    return sys.path

def modules()->dict:
    __import()
    return sys.modules