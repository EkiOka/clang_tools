import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

urllib = None
parse_result = object
# リリース時にはコメントアウトしてください
import urllib

def __import():
    global urllib
    global parse_result
    if urllib == None:
        urllib = pkgs.imp("urllib")

def urlparse(url:str)->parse_result:
    return urllib.urlparse(url)
