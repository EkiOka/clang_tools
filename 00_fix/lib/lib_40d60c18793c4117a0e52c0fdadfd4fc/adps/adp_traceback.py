import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

traceback = None
# リリース時にはコメントアウトしてください
# import traceback

def __import():
    global traceback
    if traceback == None:
        traceback = pkgs.imp("traceback")

def format_exc():
    __import()
    return traceback.format_exc()
