import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

shutil = None
# リリース時にはコメントアウトしてください
#import shutil

def __import():
    global shutil
    if shutil == None:
        shutil = pkgs.imp("shutil")

def rmtree(path:str,ignore_errors:bool=True):
    """ディレクトリ削除

    Parameters
    ----------
    path : str
        対象パス
    ignore_errors : bool, optional
        エラー発生時はエラーを無視するかどうかを設定, by default True
    """
    __import()
    shutil.rmtree(path,ignore_errors=ignore_errors)

def copytree(src:str, dst:str, dirs_exist_ok:bool=True):
    """ファイル・ディレクトリコピー

    ディレクトリツリーを再現しながらコピーします。

    Parameters
    ----------
    src : str
        コピー元
    dst : str
        コピー先
    dirs_exist_ok : bool, optional
        コピー先に既にディレクトリがあった場合にエラーを発生させません, by default True
    """
    __import()
    shutil.copytree(src,dst=dst,dirs_exist_ok=dirs_exist_ok)

def copy2(src:str,dst:str):
    __import()
    shutil.copy2(src=src,dst=dst)
