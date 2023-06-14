import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

os = None
# リリース時にはコメントアウトしてください
import os

def __import():
    global os
    if os == None:
        os = pkgs.imp("os")
def environ()->dict:
    res = dict()
    for k,v in os.environ.items():
        res[k]=v
        res[str(k).upper()]=v
        res[str(k).lower()]=v
    return res
def name()->str:
    __import()
    return os.name
def sep()->str:
    __import()
    return os.sep
def extsep()->str:
    __import()
    return os.extsep
def pathsep()->str:
    __import()
    return os.pathsep
def getcwd() -> str:
    """カレントディレクトリ取得
    """
    __import()
    return os.getcwd()
def chdir(path:str):
    """カレントディレクトリ設定

    Parameters
    ----------
    path : str
        ファイルパス
    """
    __import()
    os.chdir(path)
def exists(path:str)->bool:
    """ファイル有無判定
    """
    __import()
    return os.path.exists(path)
def isfile(path:str)->bool:
    """ファイル判定
    """
    __import()
    return os.path.isfile(path)
def isdir(path:str)->bool:
    """ディレクトリ判定
    """
    __import()
    os.path.isdir(path)
def isabs(path)->bool:
    """絶対パス判定
    """
    return os.path.isabs(path)
def getsize(path:str)->int:
    """ファイルサイズ取得
    """
    __import()
    return os.path.getsize(path)
def getmtime(path:str)->float:
    """最終更新日時取得
    """
    __import()
    return os.path.getmtime(path)
def abspath(path:str)->str:
    """絶対パス取得
    """
    __import()
    return os.path.abspath(path)
def dirname(path:str)->str:
    """ディレクトリパス取得
    """
    __import()
    return os.path.dirname(path)
def splitext(path:str)->list[str]:
    """拡張子とファイル名を分割
    """
    __import()
    return [ str(item) for item in os.path.splitext(path) ]
def basename(path:str)->str:
    """ファイル名取得
    """
    __import()
    return os.path.basename(path)
def remove(path:str):
    """ファイル・ディレクトリ削除
    """
    __import()
    return os.remove(path)
def makedirs(path:str,exist_ok:bool=True):
    """ディレクトリ作成
    """
    __import()
    os.makedirs(path,exist_ok=exist_ok)
def replace(src:str, dst:str):
    __import()
    os.replace(src=src,dst=dst)
def relpath(path:str,start:str):
    __import()
    os.path.relpath(path,start)