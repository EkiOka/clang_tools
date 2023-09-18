import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

re = None
re_Match = None
# リリース時にはコメントアウトしてください
import re
re_Match = re.Match


def __import():
    global re
    global re_Match
    if re == None:
        re = pkgs.imp("re")
        re_Match = re.Match

def compile(pattern:str):
    __import()
    return re.compile(pattern)

def match(text:str,pattern):
    __import()
    res = False
    if isinstance(pattern,str):
        res = re.match(pattern,text)
    else:
        res = pattern.match(text)
    return res

def group(match_result,name:str):
    if isinstance(match_result,re_Match):
        return match_result.group(name)
    else:
        raise Exception(f"引数(match_result)が不正です。value=({match_result}) , type={type(match_result)}")
