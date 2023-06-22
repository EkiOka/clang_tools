import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

urllib_parse = None
# リリース時にはコメントアウトしてください
#import urllib.parse as urllib_parse

def __import():
    global urllib_parse
    if urllib_parse == None:
        urllib_parse = pkgs.imp("urllib.parse")

def urlparse(url:str):
    __import()
    return urllib_parse.urlparse(url)
