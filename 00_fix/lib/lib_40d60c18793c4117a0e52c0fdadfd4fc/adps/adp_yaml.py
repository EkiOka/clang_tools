import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

yaml = None
# リリース時にはコメントアウトしてください
#import yaml

def __import():
    global yaml
    if yaml == None:
        yaml = pkgs.imp("yaml")

def safe_load(file) -> dict:
    __import()
    return yaml.safe_load(file)

def dump(obj,file, allow_unicode:bool=True,default_flow_style:bool=False):
    __import()
    yaml.dump(obj,file, allow_unicode=allow_unicode, default_flow_style=default_flow_style)
    return
