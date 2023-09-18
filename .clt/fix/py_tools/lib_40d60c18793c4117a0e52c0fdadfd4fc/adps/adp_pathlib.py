import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

pathlib = None
# リリース時にはコメントアウトしてください
#import pathlib

def __import():
    global pathlib
    if pathlib == None:
        pathlib = pkgs.imp("pathlib")
    
def Path_parent(path:str)->str:
    __import()
    return pathlib.Path(path).parent
