import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

sys = None
logging = None
logging_config = None
# リリース時にはコメントアウトしてください
#import sys
#import logging
#import logging.config
#logging_config = logging.config

def __import():
    global sys
    global logging
    global logging_config
    if logging == None:
        sys = pkgs.imp("sys")
        logging = pkgs.imp("logging")
        logging_config = pkgs.imp("logging.config")


def dictConfig(cfg:dict):
    __import()
    logging_config.dictConfig(cfg)

def getLogger(id:str):
    __import()
    return logging.getLogger(id)
def debug(msg:str,logger):
    """ローカル環境で開発するときだけ使う情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    logger.debug(msg)
def info(msg:str,logger):
    """プログラムの状況や変数の内容、処理するデータ数など、後から挙動を把握しやすくするために残す情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    logger.info(msg)
def warning(msg:str,logger):
    """プログラムの処理は続いているが、何かしら良くないデータや通知すべきことについての情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    logger.warning(msg)
def error(msg:str,logger):
    """プログラム上の処理が中断したり、停止した場合の情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    logger.error(msg)
def critical(msg:str,logger):
    """システム全体や連携システムに影響する重大な問題が発生した場合の情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    logger.critical(msg)
