import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

hashlib = None
# リリース時にはコメントアウトしてください
#import hashlib

def __import():
    global hashlib
    if hashlib == None:
        hashlib = pkgs.imp("hashlib")
    
def sha256(value:bytes)->str:
    __import()
    return hashlib.sha256(value).hexdigest()

def sha512(value:bytes)->str:
    __import()
    return hashlib.sha512(value).hexdigest()
