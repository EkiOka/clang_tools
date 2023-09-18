import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

codecs = None
# リリース時にはコメントアウトしてください
#import codecs

def __import():
    global codecs
    if codecs == None:
        codecs = pkgs.imp("codecs")

def open(path:str, mode:str="r", encoding:str=None):
    __import()
    return codecs.open(path,mode=mode,encoding=encoding)
