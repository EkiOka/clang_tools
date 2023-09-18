import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

copy = None
# リリース時にはコメントアウトしてください
# import copy

def __import():
    global copy
    if copy == None:
        copy = pkgs.imp("copy")


def deep_copy(src):
    __import()
    return copy.deepcopy(src)
