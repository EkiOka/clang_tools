import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

json = None
# リリース時にはコメントアウトしてください
#import json

def __import():
    global json
    if json == None:
        json = pkgs.imp("json")

def loads(src:str):
    __import()
    return json.loads(src)

def dump(obj, fp, ensure_ascii=True, indent=None, separators=None, sort_keys=False):
    __import()
    json.dump(obj,fp,ensure_ascii=ensure_ascii,indent=indent,separators=separators, sort_keys=sort_keys)
