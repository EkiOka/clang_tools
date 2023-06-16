"""お手軽簡単にご利用可能なAPI群

専門店(python standard library)には敵わないし。
そもそも、仲介業者(adaptors)を介して専門店から仕入れてる。

"""
#========================================================================
# IMPORT
#========================================================================
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_codecs     as codecs
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_datetime   as datetime
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_getpass    as getpass
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_hashlib    as hashlib
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_inspect    as inspect
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_jinja2     as jinja2
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_json       as json
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_logging    as logging
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_markdown   as markdown
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_os         as os
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_pathlib    as pathlib
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_re         as re
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_shutil     as shutil
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_subprocess as subprocess
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_sys        as sys
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_traceback  as traceback
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_uuid       as uuid
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp_yaml       as yaml

import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list           as pl

#========================================================================
# CONST
#========================================================================
#
# 定数の名前が安定しないため命名規則をメモしておく
# 目的の対象_種別の順に記載する
#
# 例えば以下のようになる。
# ENC_DEF      : エンコードが欲しい->デフォルトで使用するもの
# SEP_DIR2FILE : 区切り文字が欲しい->ディレクトリとファイルを区切るためのもの
#

ENC_DEF:str="utf-8"
"""エンコード：テキストファイルを扱う時のデフォルト"""

SEP_DIR2FILE:str  = os.sep()
"""区切り文字：ディレクトリとファイル"""

SEP_FILE2EXT:str  = os.extsep()
"""区切り文字：ディレクトリと拡張子"""

SEP_PATH2PATH:str = os.pathsep()
"""区切り文字：パスとパス"""

SEP_DATE2DATE:str = "/"
"""区切り文字：年月日"""

SEP_TIME2TIME:str = ":"
"""区切り文字：時分秒"""

SEP_DATE2TIME:str = " "
"""区切り文字：日付と時間を連続で記載する場合"""

INDENT_JSON_DEF:int=4
"""JSONファイル：インデントサイズ"""

RET_CODE_CR:str="\r"
"""改行コード：CR"""

RET_CODE_LF:str="\n"
"""改行コード：LF"""

RET_CODE_CRLF:str="\r\n"
"""改行コード：CRLF"""

RET_CODE_DEF:str=RET_CODE_LF
"""改行コード：デフォルト値"""

TYPE_METHOD:str=object
"""型：メソッド"""


class dec:
    """コンソールテキストの装飾
    """
    FC_BLACK     = "\033[30m" # 標準出力の文字色を黒にする文字列
    FC_RED       = "\033[31m" # 標準出力の文字色を赤にする文字列
    FC_GREEN     = "\033[32m" # 標準出力の文字色を緑にする文字列
    FC_YELLOW    = "\033[33m" # 標準出力の文字色を黄にする文字列
    FC_BLUE      = "\033[34m" # 標準出力の文字色を青にする文字列
    FC_MAGENTA   = "\033[35m" # 標準出力の文字色をマゼンタにする文字列
    FC_CYAN      = "\033[36m" # 標準出力の文字色をシアンにする文字列
    FC_WHITE     = "\033[37m" # 標準出力の文字色を白にする文字列
    BC_BLACK     = "\033[40m" # 標準出力の文字色を黒にする文字列
    BC_RED       = "\033[41m" # 標準出力の文字色を赤にする文字列
    BC_GREEN     = "\033[42m" # 標準出力の文字色を緑にする文字列
    BC_YELLOW    = "\033[43m" # 標準出力の文字色を黄にする文字列
    BC_BLUE      = "\033[44m" # 標準出力の文字色を青にする文字列
    BC_MAGENTA   = "\033[45m" # 標準出力の文字色をマゼンタにする文字列
    BC_CYAN      = "\033[46m" # 標準出力の文字色をシアンにする文字列
    BC_WHITE     = "\033[47m" # 標準出力の文字色を白にする文字列
    END          = "\033[0m"  # 標準出力の文字色・装飾を終了する文字列
    FB_REVERSE   = "\033[7m"  # 標準出力の文字色・背景色を反転させる文字列
    BOLD         = "\033[1m"  # 標準出力の文字を太字にする文字列
    UNDER_LINE   = "\033[4m"  # 標準出力の文字に下線を付ける文字列
#========================================================================
# VARIABLE
#========================================================================

any:object=object()
"""型が複数ある場合の説明用識別子
"""

StaticFunction:object=object()
"""メソッドではない静的関数
"""


is_supposed_debug:bool=False
"""想定したデバッグ環境(win/vscode)かどうか
"""
if "debugpy" in sys.modules().keys():
    if os.name() == "nt":
        is_supposed_debug = True

prefix:str = ""
"""コマンドラインの先頭に表示する固定の文字列
"""

__logger = None

#========================================================================
# FUNCTION
#========================================================================
#------------------------------------------------------------------------
# CURRENT DIRECTORY
#------------------------------------------------------------------------
def get_cur_dir()->str:
    """カレントディレクトリ取得
    """
    return os.getcwd()
def set_cur_dir(path:str)->None:
    """カレントディレクトリ設定
    """
    os.chdir(path)
#------------------------------------------------------------------------
# PATH INFO
#------------------------------------------------------------------------
def is_exist(path:str)->bool:
    """ファイル有無判定
    """
    return os.exists(path)
def is_file(path:str)->bool:
    """ファイル判定
    """
    return os.isfile(path)
def is_dir(path:str)->bool:
    """ディレクトリ判定
    """
    return os.isdir(path)
def is_abs_path(path:str)->bool:
    """絶対パス判定
    """
    return os.isabs(path)
#------------------------------------------------------------------------
# PATH CONTROL
#------------------------------------------------------------------------
def __cnv_path_sep(path:str, sep:str=SEP_DIR2FILE)->str:
    """パスの区切り文字を統一

    Parameters
    ----------
    path : str
        区切り文字を統一するパス
    sep : str, optional
        統一する区切り文字, by default SEP_DIR2FILE

    Returns
    -------
    str
        区切り文字を統一されたパス
    """
    log_info(f"path: type={type(path)}, value ={path}")
    log_info(f"sep:  type={type(sep)},  value ={sep}")
    res = path.replace("/",sep)
    res = res.replace("\\",sep)
    return res
def cnv_abs_path(path:str,sep:str=SEP_DIR2FILE)->str:
    """絶対パス変換

    Parameters
    ----------
    path : str
        変換対象のパス
    sep : str, optional
        パスの区切り文字, by default SEP_DIR2FILE

    Returns
    -------
    str
        絶対パス
    """
    res = ""
    if is_abs_path(path):
        res = path
    else:
        res = os.abspath(path)
    res = __cnv_path_sep(res,sep)
    return res
def cnv_abs_dir_path(path:str,sep:str=SEP_DIR2FILE)->str:
    """ディレクトリパス(絶対パス形式)変換

    Parameters
    ----------
    path : str
        変換対象パス
    sep : str, optional
        パスの区切り文字, by default SEP_DIR2FILE

    Returns
    -------
    str
        絶対パス形式のディレクトリパス
    """
    log_info(cur_function_name())
    abs_path = cnv_abs_path(path,sep)
    log_info(f"abs_path:{abs_path}")
    res = ""
    if is_dir(abs_path):
        log_info(f"abs_path is dir.")
        res = abs_path
    else:
        log_info(f"abs_path is not dir")
        res = os.dirname(abs_path)
    log_info(f"res:{res}")
    return res
def cnv_abs_file_path_none_ext(path:str,sep:str=SEP_DIR2FILE)->str:
    """ . と拡張子は除いた絶対パスに変換

    拡張子は最初の区切り文字"."の後ろの文字列と判別します。
    例）aaa.tar.gzの場合はtar.gzを拡張子として扱います。

    Parameters
    ----------
    path : str
        変換対象パス
    sep : str, optional
        パスの区切り文字, by default SEP_DIR2FILE

    Returns
    -------
    str
        絶対パス形式のファイルパス。
        ファイルパスに拡張子区切り文字(".")と拡張子は含まれません。
    """
    abs_path = cnv_abs_path(path,sep)
    res = ""
    if is_dir(abs_path):
        raise Exception(f"ファイルパスの引数(path)にディレクトリパスが指定されました。\n(path:{path})")
    else:
        res = abs_path
    res = os.splitext(res)[0]
    return res
def cnv_file_name(path:str)->str:
    """ファイル名(拡張子含む)変換"""
    res = os.basename(path)
    return res
def cnv_file_name_none_ext(path:str)->str:
    """ファイル名(拡張子含まない)変換"""
    name = cnv_file_name(path)
    res = os.splitext(name)[0]
    return res
def cnv_parent_dir(path:str)->str:
    """親ディレクトリパス変換

    Parameters
    ----------
    path : str
        変換対象パス

    Returns
    -------
    str
        親ディレクトリパス
    """
    res = pathlib.Path_parent(path)
    return res
def cnv_file_ext(path:str)->str:
    """拡張子( 先頭 . なし )変換

    拡張子は最初の区切り文字"."の後ろの文字列と判別します。
    例）aaa.tar.gzの場合はtar.gzを拡張子として扱います。

    Parameters
    ----------
    path : str
        変換対象のパス

    Returns
    -------
    str
        拡張子
        先頭にある拡張子区切り文字(".")は含まれません。
    """
    name = os.basename(path)
    name_parts = os.splitext(name)
    res = ""
    if len(name_parts)>=2:
        name_parts.pop(0)
        res = ".".join(name_parts)
    return res
def cnv_rel_path(path:str,start:str=None):
    """相対パスを取得"""
    return os.relpath(path,start)
#------------------------------------------------------------------------
# FILE INFORMATION
#------------------------------------------------------------------------
def get_file_size(path:str)->int:
    """ファイルサイズ取得
    """
    return os.getsize(path)
def get_file_update_time(path:str)->float:
    """ファイル更新日時取得
    """
    return os.getmtime(path)
def get_file_sha256(path:str)->str:
    """ファイルSHA256取得
    """
    res = ""
    with open(path,"rb") as file:
        fileData = file.read()
        res = hashlib.sha256(fileData)
    return res
def get_file_sha512(path:str)->str:
    """ファイルSHA512取得
    """
    res = ""
    with open(path,"rb") as file:
        fileData = file.read()
        res = hashlib.sha512(fileData)
    return res
#------------------------------------------------------------------------
# FILE LOAD/SAVE
#------------------------------------------------------------------------
def load_bin(path:str)->bytes:
    """バイナリファイル読出

    Parameters
    ----------
    path : str
        ファイルパス

    Returns
    -------
    bytes
        読みだしたデータ
    """
    res = None
    with open(path, 'rb') as file:
        res = file.read()
    return res
def load_text(path:str,encoding:str=ENC_DEF)->str:
    """テキストファイル読出

    Parameters
    ----------
    path : str
        ファイルパス
    encoding : str, optional
        読みだすファイルのエンコード, by default ENC_DEF

    Returns
    -------
    str
        読みだされたテキスト
    """
    res = ""
    with open(path, encoding=encoding) as f:
        res = f.read()
    return res
def load_text_lines(path:str,encoding:str=ENC_DEF)->list[str]:
    """テキストファイル読出->リスト

    Parameters
    ----------
    path : str
        ファイルパス
    encoding : str, optional
        読みだすファイルのエンコード, by default ENC_DEF

    Returns
    -------
    list[str]
        読みだされたテキスト
    """
    res = []
    with open(path, encoding=encoding) as f:
        res = f.readlines()
    return res
def save_text(path:str,text:any,encoding:str=ENC_DEF,ret_code:str=RET_CODE_DEF):
    """テキストファイル保存

    Parameters
    ----------
    path : str
        ファイルパス
    text : Any
        テキストデータ
        型はstrとlist[str]にのみ対応しています。
    encoding : str, optional
        保存に使用するエンコード, by default ENC_DEF
    ret_code : str, optional
        保存に使用する改行コード, by default RET_CODE_DEF
    """
    make_dir_from_file_path(path)
    if isinstance(text,str):
        with open(path, mode="w", encoding=encoding) as f:
            match ret_code:
                case "\n":
                    text = text.replace("\r\n","\n")
                    text = text.replace("\r","\n")
                case "\r\n":
                    text = text.replace("\r\n","\n")
                    text = text.replace("\r","\n")
                    text = text.replace("\n","\r\n")
                case "\r":
                    text = text.replace("\r\n","\r")
                    text = text.replace("\n","\r")
                    pass
                case _:
                    raise Exception(f"改行コードの指定が異常です ret_code={ret_code}")
            text = text.replace("\n",ret_code)
            f.write(text)
    elif isinstance(text,list[str]):
        with open(path, mode="w", encoding=encoding) as f:
            f.writelines([line + ret_code for line in text])
    else:
        raise Exception(f"未対応の型({type(text)})が引数(text)に渡されました")
def load_json(path: str) -> any:
    text = load_text(path)
    res = json.loads(text)
    return res
def save_json(path:str,data,encoding:str=ENC_DEF):
    make_dir_from_file_path(path)
    with codecs.open(path , mode="w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False,indent=INDENT_JSON_DEF, sort_keys=True)
def load_yaml(path:str, encoding=ENC_DEF)->any:
    obj = dict()
    with open(path, encoding=encoding) as f:
        obj = yaml.safe_load(f)
    return obj
def save_yaml(path:str,data:any, encoding=ENC_DEF)->None:
    make_dir_from_file_path(path)
    with open(path, mode="w", encoding=encoding) as f:
        yaml.dump(data,f)
    return    
#------------------------------------------------------------------------
# FILE CONTROL
#------------------------------------------------------------------------
def remove_file(path:str):
    """ファイルを削除する
    """
    os.remove(path)
def remove_dir(path:str):
    """ディレクトリを削除する
    """
    path = cnv_abs_dir_path(path)
    shutil.rmtree(path=path,ignore_errors=True)
def make_dir(path:str):
    os.makedirs(path,True)
def make_dir_from_file_path(path:str):
    path = cnv_abs_dir_path(path)
    os.makedirs(path,True)
def copy_dir_tree(src:str, dest:str, not_ptn=None):
    """ディレクトリツリーをコピーします
    """
    if not_ptn is None:
        shutil.copytree(src, dest, dirs_exist_ok=True)
    else:
        shutil.copytree(src, dest, ignore=not_ptn, dirs_exist_ok=True)
def copy_file(src:str,dest:str):
    """ファイルコピー

    Parameters
    ----------
    src : str
        コピー元のファイルパス
    dest : str
        コピー先のファイルパス
    """
    make_dir_from_file_path(dest)
    shutil.copy2(src,dest)
def move_file(src:str,dest:str):
    """ファイルを移動する
    """
    os.replace(src,dest)
#------------------------------------------------------------------------
# CLASS
#------------------------------------------------------------------------
def add_method(target_instance:any,method:StaticFunction,name:str="",override:bool=True):
        """インスタンスに動的にメソッドを追加する。

        すでにメソッドがある場合は上書きになりますので注意してください。

        Parameters
        ----------
        target_instance : Any
            追加対象のインスタンス
        method : StaticFunction
            追加するメソッド
        name : str
            メソッド名, by default empty string("").
            空文字列の場合はmethodの名前を使用します。
        override : bool
            trueの場合、既にメソッドがある場合は削除
        """
        if name == "":
            name = method.__name__
        if override:
            if name in target_instance.__dict__.keys():
                delattr(target_instance,name)
        setattr(target_instance, name, method )
#------------------------------------------------------------------------
# DICT
#------------------------------------------------------------------------
def keys_maxlen(src:dict)->int:
    """キー最大長取得。

    主にコンソールへの辞書型のテーブル出力などで
    余白を入れる際に使用します。

    Parameters
    ----------
    src : dict
        最大長を求める対象の辞書型

    Returns
    -------
    int
        キーの最大長
    """
    res = max( [ len(str(key)) for key in src.keys() ])
    return res
#------------------------------------------------------------------------
# LIST
#------------------------------------------------------------------------
def loop(data:list,method:StaticFunction,last_method:StaticFunction)->list:
    """ループ処理を行う

    最後の要素だけセパレータを付けない場合など、
    少し処理が違う場合などに使用すること

    Parameters
    ----------
    data : list
        ループ処理の対象となるデータ
    method : StaticFunction
        ループ処理の内容(ただし、最後のデータは除く)
    last_method : StaticFunction
        ループ最後のデータに対する処理の内容
    """
    # 途中の要素を処理
    for d in not_tail(data):
        method(d)
    last_method(tail(data))
def tail(src:list)->any:
    """末尾の要素を取得する
    """
    res = None
    if len(src) > 0:
        res = src[-1]
    return res
def not_tail(src:list)->list:
    """末尾ではない要素を取得する
    """
    res = []
    if len(src) > 0:
        res = src[:-1]
    return res
#------------------------------------------------------------------------
# UUID
#------------------------------------------------------------------------
def uuid_hex_lower()->str:
    return uuid.uuid4_hex().lower()
#------------------------------------------------------------------------
# DATETIME
#------------------------------------------------------------------------
def cnv_datetime_to_YYYYMMDD(src:datetime.datetime, sep:str=SEP_DATE2DATE)->str:
    """日付をYYYYMMDD形式の文字列に変換する
    """
    return datetime.strftime(src,f"%Y{sep}%m{sep}%d")
def cnv_datetime_to_HHMMSS(src:datetime.datetime, sep:str=SEP_TIME2TIME)->str:
    """日時をHHMMSS形式の文字列に変換する
    """
    return datetime.strftime(src,f"%H{sep}%M{sep}%S")
def cnv_datetime_to_YYYYMMDDHHMMSS(
        src:datetime,
        date_sep:str=SEP_DATE2DATE,
        time_sep:str=SEP_TIME2TIME,
        date_time_sep:str=SEP_DATE2TIME)->str:
    """日時をYYYYMMDDHHMMSS形式の文字列に変換する
    """
    date = cnv_datetime_to_YYYYMMDD(src,date_sep)
    time = cnv_datetime_to_HHMMSS(src,time_sep)
    res = f"{date}{date_time_sep}{time}"
    return res
def cnv_str_to_datetime(src:str, format:str="%Y/%m/%d %H:%M:%S"):
    """文字列をdatetimeに変換します
    """
    res = datetime.strptime(src, format)
    return res
def cnv_datetime_to_serial(src:float):
    """datetimeをシリアル値に変換します
    """
    return datetime.serial(src)
def cnv_datetime_to_dict(src:datetime)->dict:
    """日時データを様々な形式に変換してまとめてdictに入れて返します。

    実際のプログラムに使用するというのではなく、変換処理のサンプルとして使用してください。

    Parameters
    ----------
    src : datetime
        変換する日時データ

    Returns
    -------
    dict
        変換後のデータ
    """
    res = dict()
    res["YYYYMMDDHHMMSS"] = datetime.strftime(src,"%Y%m%d%H%M%S")
    res["YYYYMMDD"] = datetime.strftime(src,"%Y%m%d")
    res["YYYY"] = datetime.strftime(src,"%Y")
    res["MM"] = datetime.strftime(src,"%m")
    res["DD"] = datetime.strftime(src,"%d")
    res["HHMMSS"] = datetime.strftime(src,"%H%M%S")
    res["YYYY/MM/DD"] = cnv_datetime_to_YYYYMMDD(src,"/")
    res["YYYY-MM-DD"] = cnv_datetime_to_YYYYMMDD(src,"-")
    res["HH:MM:SS"] = datetime.strftime(src,"%H:%M:%S")
    res["YYYY/MM/DD HH:MM:SS"] = cnv_datetime_to_YYYYMMDDHHMMSS(src,"/",":"," ")
    res["YYYY-MM-DD HH:MM:SS"] = cnv_datetime_to_YYYYMMDDHHMMSS(src,"-",":"," ")
    res["YYYY年MM月DD日"] = datetime.strftime(src,"%Y年%m月%d日")
    res["YYYY年MM月DD日(曜日)"] = datetime.strftime(src,"%Y年%m月%d日(%A)")
    res["YYYY年MM月DD日(曜日short)"] = datetime.strftime(src,"%Y年%m月%d日(%a)")
    res["曜日"]=datetime.strftime(src,"%A")
    res["曜日short"]=datetime.strftime(src,"%a")
    return res
def add_days(src:float,days:int):
    """datetimeに指定の日数を加算または減算します
    """
    return datetime.add_days(src,days)
def update_datetime(src:datetime.datetime, 
                    year:int=-1,month:int=-1,day:int=-1, hour:int=-1,minute:int=-1,second:int=-1,microsecond:int=-1
                    )->float:
    """日時の一部を更新して返します
    """
    return datetime.update_datetime(src,year,month,day,hour,minute,second,microsecond)
#------------------------------------------------------------------------
# LOGGING
#------------------------------------------------------------------------
def log_enable_debug(id:str,cfg:dict=None):
    """デバッグによるログ出力を有効にします

    Parameters
    ----------
    id : str
        固有IDを設定してください
    cfg : dict, optional
        デバッグ出力の出力設定, by default None
    """
    global __logger
    if prefix == "":
        set_default_prefix()
    if cfg == None:            
        cfg = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                # フォーマットの説明は以下参照
                # https://docs.python.org/ja/3/library/logging.html#logrecord-attributes
                "standard": {
                    "format": f"{prefix}(%(levelname)s) %(message)s"
                },
                "add_position": {
                    "format": f"{prefix}(%(levelname)s) %(funcName)s %(lineno)s %(message)s"
                }
            },

            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "level": "DEBUG",
                    "formatter": "standard",
                    "stream": "ext://sys.stdout"
                },
                # "file": {
                #     "class": "logging.FileHandler",
                #     "level": "INFO",
                #     "formatter": "standard",
                #     "filename": f"{__name__}.log"
                # },
                "null": {
                    "class": "logging.NullHandler"
                }
            },

            "loggers": {
                f"{id}": {
                    "level": "DEBUG",
                    "handlers": ["console"],
                    "propagate": False
                }
            },

            "root": {
                "level": "INFO"
            }
        }
    

    logging.dictConfig(cfg)
    __logger = logging.getLogger(id)
def log_std_err(msg:str):
    """ログを標準エラー出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    if is_supposed_debug:
        logging.std_err(f"{prefix} > {dec.FC_RED}{msg}{dec.END}")
    else:
        logging.std_err(f"{prefix} > {msg}")
def log_std_out(msg:str):
    """ログを標準出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    if is_supposed_debug:
        logging.std_out(f"{prefix} > {msg}")
    else:
        logging.std_out(f"{prefix} > {msg}")
def log_debug(msg:str):
    """ローカル環境で開発するときだけ使う情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    if __logger != None:
        if is_supposed_debug:
            s_dec = dec.BC_BLUE
            e_dec = dec.END
            msg = f"{s_dec}{msg}{e_dec}"
        logging.debug(msg,__logger)
def log_info(msg:str):
    """プログラムの状況や変数の内容、処理するデータ数など、後から挙動を把握しやすくするために残す情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    if __logger != None:
        s_dec = ""
        e_dec = ""
        if is_supposed_debug:
            s_dec = dec.FC_GREEN
            e_dec = dec.END
        logging.info(f"{s_dec}{msg}{e_dec}",__logger)
def log_warning(msg:str):
    """プログラムの処理は続いているが、何かしら良くないデータや通知すべきことについての情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    if __logger != None:
        s_dec = dec.FC_YELLOW
        e_dec = dec.END
        if is_supposed_debug:
            s_dec = dec.FC_BLUE
            e_dec = dec.END
        logging.warning(f"{s_dec}{msg}{e_dec}",__logger)
def log_error(msg:str):
    """プログラム上の処理が中断したり、停止した場合の情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    if __logger != None:
        s_dec = dec.FC_RED
        e_dec = dec.END
        if is_supposed_debug:
            s_dec = dec.FC_RED
            e_dec = dec.END
        logging.critical(f"{s_dec}{msg}{e_dec}",__logger)
def log_critical(msg:str):
    """システム全体や連携システムに影響する重大な問題が発生した場合の情報を出力します。

    Parameters
    ----------
    msg : str
        出力メッセージ
    """
    if __logger != None:
        s_dec = dec.BC_RED
        e_dec = dec.END
        if is_supposed_debug:
            s_dec = dec.FC_RED + dec.FB_REVERSE
            e_dec = dec.END
        logging.critical(f"{s_dec}{msg}{e_dec}",__logger)
def raise_Exception(msg:str):
    """汎用の例外を発生させます。

    Parameters
    ----------
    msg : str
        例外メッセージ
    """
    if is_supposed_debug:
        # vscodeで例外投げないのは単なる趣味です。(ポップアップうざい)
        log_error(msg)
        sys.exit(1)
    else:
        raise Exception(msg)
def raise_FileNotFound(path:str):
    """ファイルがない場合の例外を発生させます。

    Parameters
    ----------
    path : str
        ファイルパス
    """
    msg = f"file not found.({path})"
    if is_supposed_debug:
        # vscodeで例外投げないのは単なる趣味です。(ポップアップうざい)
        log_error(msg)
        sys.exit(1)
    else:
        raise FileNotFoundError(msg)
def raise_NotFound(target:str,type_name:str):
    """ファイル以外の何かが不在である場合の例外を発生させます。

    Parameters
    ----------
    target : str
        存在しないものインスタンス文字列
    type_name : str
        存在しないものの名前
    """
    msg = f"{type_name}({target}) not found."
    if is_supposed_debug:
        # vscodeで例外投げないのは単なる趣味です。(ポップアップうざい)
        log_error(msg)
        sys.exit(1)
    else:
        raise Exception(msg)
def raise_ValueRange(value,min=None,max=None):
        """値が範囲外の場合の例外を発生させます。

        Parameters
        ----------
        value : Any
            範囲外になっている値のインスタンス
        min : Any, optional
            最小値, by default None
        max : Any, optional
            最大値, by default None
        """
        if min != None:
            if max != None:
                msg = f"value is over.( {min} < {value} < {max} )."
            else:
                msg = f"value is over.( {min} < {value} )."
        else:
            if max != None:
                msg = f"value is over.( {value} < {max} )."
            else:
                msg = f"min and max is None.( min : {min} / max : {max} )."

        if is_supposed_debug:
            # vscodeで例外投げないのは単なる趣味です。(ポップアップうざい)
            log_error(msg)
            sys.exit(1)
        else:
            raise ValueError(msg)
#------------------------------------------------------------------------
# TEMPLATE FILE
#------------------------------------------------------------------------
def cnv_template_to_text(data:any,template_path:str,template_encoding:str=ENC_DEF)->str:
    """テンプレートからテキストに変換する

    Parameters
    ----------
    data : Any
        テンプレート変数
    template_path : str
        使用するテンプレートのパス
    template_encoding : str, optional
        テンプレートのエンコード, by default ENC_DEF

    Returns
    -------
    str
        変換されたテキスト
    """

    # 現在のカレントディレクトリを取得
    cur = get_cur_dir()

    # テンプレートに関係するパスを取得
    tmp_abs_path = cnv_abs_path(template_path)
    tmp_dir = cnv_abs_dir_path(tmp_abs_path)
    tmp_file_name = cnv_file_name(template_path)

    # パスは/で揃える
    tmp_dir = tmp_dir.replace("\\","/")
    tmp_abs_path = tmp_abs_path.replace("\\","/")

    # テンプレート情報としてパスを格納
    template_info = dict()
    template_info["path"] = tmp_abs_path
    template_info["dir"]  = tmp_dir
    template_info["file"] = tmp_file_name

    # カレントディレクトリをテンプレートファイルのあるディレクトリに変更
    set_cur_dir(tmp_dir)

    # テンプレート生成関連クラスのインスタンス生成
    loader         = jinja2.file_system_loader( searchpath=tmp_dir, encoding=template_encoding)
    environment    = jinja2.environment(loader=loader)

    # フィルタの設定
    environment.add_filter("info",log_info)
    environment.add_filter("debug",log_debug)
    environment.add_filter("warning",log_warning)
    environment.add_filter("error",log_error)
    environment.add_filter("critical",log_critical)
    environment.add_filter("user_path",pl.get_user_path)
    environment.add_filter("env_path",pl.get_env_path)

    # テンプレートに渡すデータ
    temp_data = dict()
    temp_data["data_4d22a990e03e4ff0b66061daa1674a0d"]=os.environ()
    temp_data["data_095064f18e894dcfaa3f8d12b1d0b9ca"]=template_info
    temp_data["data_d74c99efdbb745129d4e98d2194bc941"]=data

    try:
        template  = environment.get_template(name=tmp_file_name)
        out_text  = template.render(temp_data)
    except Exception as e:
        log_std_err(e)
        log_std_err(traceback.format_exc())
        log_std_err( f"template_path : {template_path}")
        log_std_err( f"tmp_dir       : {tmp_dir}")
        log_std_err( f"tmp_file_name : {tmp_file_name}")
        log_std_err( f"cur           : {cur} -> {os.getcwd()}")
        log_std_err( f"temp_data     : {temp_data}")
        # カレントディレクトリを元に戻す
        os.chdir(cur)
        # プロセスを異常終了する
        sys.exit(1)

    # カレントディレクトリを元に戻す
    os.chdir(cur)

    return out_text
#------------------------------------------------------------------------
# MARKDOWN
#------------------------------------------------------------------------
def cnv_markdown_to_html(src:str,include_base_path:str="."):
    """マークダウンテキストをHTMLに変換
    """
    markdown.convert(src,include_base_path=include_base_path)
#------------------------------------------------------------------------
# ENVIRONMENT
#------------------------------------------------------------------------
def cur_file_name()->str:
    return inspect.stack_file_name(2)
def cur_function_name()->str:
    return inspect.stack_function_name(2)
def cur_line_no()->int:
    return inspect.stack_line_no(2)
def caller_file_name()->str:
    return inspect.stack_file_name(3)
def caller_function_name()->str:
    return inspect.stack_function_name(3)
def caller_line_no()->int:
    return inspect.stack_line_no(3)
def environ_variable(name:str,default_value:str=None):
    """環境変数取得
    ない場合はdefault_valueを返す
    """
    res = None
    vars = os.environ()
    keys = vars.keys()
    if name in keys:
        res = vars[name]
    elif name.upper() in keys:
        res = vars[name.upper()]
    elif name.lower() in keys:
        res = vars[name.lower()]
    else:
        res = default_value
    return res
def user_name()->str:
    """ユーザー名取得
    """
    return getpass.getuser()
def startup_params():
    """起動引数取得"""
    return sys.argv()
def startup_py():
    """起動pyスクリプト名"""
    params = startup_params()
    py_path = params[0]
    py_name = cnv_file_name(py_path)
    return py_name
def set_default_prefix():
    global prefix
    prefix = f"{ startup_py() } > "
#------------------------------------------------------------------------
# TEXT
#------------------------------------------------------------------------
def re_compile(pattern:str):
    return re.compile(pattern)
def re_match(text:str,pattern:str=None, compiled_re=None):
    res = None
    if compiled_re != None:
        res = re.match(text,compiled_re)
    elif pattern != None:
        res = re.match(text,pattern)

    return res
def re_group(match_result,name:str):
    return re.group(match_result,name)
#------------------------------------------------------------------------
# PROCESS
#------------------------------------------------------------------------
def start_proc(params:list[str])->int:
    return subprocess.run(params)