import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

uuid = None
# リリース時にはコメントアウトしてください
#import uuid

def __import():
    global uuid
    if uuid == None:
        uuid = pkgs.imp("uuid")

def uuid1_hex()->str:
    __import()
    return uuid.uuid1().hex
def uuid3_hex()->str:
    __import()
    return uuid.uuid3().hex
def uuid4_hex()->str:
    __import()
    return uuid.uuid4().hex
def uuid5_hex()->str:
    __import()
    return uuid.uuid5().hex
