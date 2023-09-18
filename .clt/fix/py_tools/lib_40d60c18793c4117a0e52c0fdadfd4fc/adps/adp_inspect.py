import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

inspect = None
# リリース時にはコメントアウトしてください
#import inspect

def __import():
    global inspect
    if inspect == None:
        inspect = pkgs.imp("inspect")

def stack_file_name(bask_count:int=1):
    __import()
    cur = inspect.currentframe()
    back = __frame_back(cur,bask_count)
    res = __file_name(back)
    return res
def stack_function_name(bask_count:int=1):
    __import()
    cur = inspect.currentframe()
    back = __frame_back(cur,bask_count)
    res = __function_name(back)
    return res
def stack_line_no(bask_count:int=1):
    __import()
    cur = inspect.currentframe()
    back = __frame_back(cur,bask_count)
    res = __line_no(back)
    return res
def stack_local_var(name:str,default_value=None,bask_count:int=1):
    __import()
    cur = inspect.currentframe()
    back = __frame_back(cur,bask_count)
    vars = __locals(back)
    res = vars.get(name,default_value)
    return res


def caller_file_name(bask_count:int=2)->str:
    __import()
    cur = inspect.currentframe()
    back = __frame_back(cur,bask_count)
    res = __file_name(back)
    return res
def caller_function_name(bask_count:int=2)->str:
    __import()
    cur = inspect.currentframe()
    back = __frame_back(cur,bask_count)
    res = __function_name(back)
    return res
def caller_line_no(bask_count:int=2)->int:
    __import()
    cur = inspect.currentframe()
    back = __frame_back(cur,bask_count)
    res = __line_no(back)
    return res

def __line_no(cur)->str:
    res = 0
    if cur != None:
        res = cur.f_lineno
    return res


def __locals(cur)->str:
    res = 0
    if cur != None:
        res = cur.f_locals
    return res

def __file_name(cur)->str:
    res = ""
    if cur != None:
        code = cur.f_code
        if code != None:
            res = code.co_filename
    return res
def __function_name(cur)->str:
    res = ""
    if cur != None:
        code = cur.f_code
        if code != None:
            res = code.co_name
    return res

def __frame_back(cur,count:int=1):
    res = None
    back = cur.f_back
    if back != None:
        count = count - 1
        if count == 0:
            res = back
        else:
            res = __frame_back(back,count)
    return res
