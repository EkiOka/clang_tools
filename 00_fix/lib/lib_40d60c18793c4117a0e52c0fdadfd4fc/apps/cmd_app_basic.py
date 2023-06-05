"""基本的なコンソール(シェル)アプリの基底クラス

ゆるくアプリが作れることを目指します。
"""

# import standard library
import datetime
from importlib import import_module
import inspect
import os
import sys

# variables
Any = object()
Method = object()
Function = object()

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
class cmd_app_utility:

    #========================================================================
    #
    # CONST
    #
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
    """テキストファイルを扱う時のデフォルトエンコード
    """

    SEP_DIR2FILE:str  = os.sep
    """ディレクトリとファイルの区切り文字
    """

    SEP_FILE2EXT:str  = os.extsep
    """ディレクトリと拡張子の区切り文字
    """

    SEP_PATH2PATH:str = os.pathsep
    """パスとパスの区切り文字
    """

    SEP_DATE2DATE:str = "/"
    """年月日の区切り文字
    """

    SEP_TIME2TIME:str = ":"
    """時分秒の区切り文字
    """

    SEP_DATE2TIME:str = " "
    """日付と時間を連続で記載する場合の区切り文字
    """

    INDENT_JSON_DEF:int=4
    """JSONファイル：インデントサイズ
    """

    RET_CODE_DEF="\n"
    """改行コード：デフォルト値
    """

    #========================================================================
    #
    # VARIABLES
    #
    #========================================================================

    is_supposed_debug:bool=False
    """想定したデバッグ環境(win/vscode)かどうか
    """

    prefix:str = ""
    """コマンドラインの先頭に表示する固定の文字列
    """

    logger=None
    """ロガーインスタンス
    """

    loaded_modules:dict=dict()
    """読み込み済みのモジュール
    """

    #========================================================================
    #
    # METHOD
    #
    #========================================================================

    def __init__(s,py:str):
        s.prefix = s.cnv_file_name(py)
        if "debugpy" in sys.modules:
            if os.name == "nt":
                s.is_supposed_debug = True
                s.log_enable_debug()

    #------------------------------------------------------------------------
    # DEBUG
    #------------------------------------------------------------------------
    def log_enable_debug(s,cfg:dict=None):
        """デバッグによるログ出力を有効にします

        Parameters
        ----------
        cfg : dict, optional
            デバッグ出力の出力設定, by default None
        """
        id = s.uuid
        logging = s.load_module("logging")
        logging_config = s.load_module("logging.config")
        if cfg == None:            
            cfg = {
                "version": 1,
                "disable_existing_loggers": False,
                "formatters": {
                    # フォーマットの説明は以下参照
                    # https://docs.python.org/ja/3/library/logging.html#logrecord-attributes
                    "standard": {
                        "format": f"{s.prefix}(%(levelname)s) %(message)s"
                    },
                    "add_position": {
                        "format": f"{s.prefix}(%(levelname)s) %(funcName)s %(lineno)s %(message)s"
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
        

        logging_config.dictConfig(cfg)
        s.logger = logging.getLogger(id)
    def log_std_err(s,msg:str):
        """ログを標準エラー出力します。

        Parameters
        ----------
        msg : str
            出力メッセージ
        """
        if s.is_supposed_debug:
            print(f"{s.prefix} > {dec.FC_RED}{msg}{dec.END}",file=sys.stderr)
        else:
            print(f"{s.prefix} > {msg}",file=sys.stderr)
    def log_std_out(s,msg:str):
        """ログを標準出力します。

        Parameters
        ----------
        msg : str
            出力メッセージ
        """
        if s.is_supposed_debug:
            print(f"{s.prefix} > {msg}",file=sys.stdout)
        else:
            print(f"{s.prefix} > {msg}",file=sys.stdout)
    def log_debug(s,msg:str):
        """ローカル環境で開発するときだけ使う情報を出力します。

        Parameters
        ----------
        msg : str
            出力メッセージ
        """
        if s.logger != None:
            if s.is_supposed_debug:
                s_dec = dec.BC_BLUE
                e_dec = dec.END
                msg = f"{s_dec}{msg}{e_dec}"
            s.logger.debug(msg)
    def log_info(s,msg:str):
        """プログラムの状況や変数の内容、処理するデータ数など、後から挙動を把握しやすくするために残す情報を出力します。

        Parameters
        ----------
        msg : str
            出力メッセージ
        """
        if s.logger != None:
            s_dec = dec.BC_GREEN
            e_dec = dec.END
            if s.is_supposed_debug:
                s_dec = dec.FC_MAGENTA
                e_dec = dec.END
            s.logger.info(f"{s_dec}{msg}{e_dec}")
    def log_warning(s,msg:str):
        """プログラムの処理は続いているが、何かしら良くないデータや通知すべきことについての情報を出力します。

        Parameters
        ----------
        msg : str
            出力メッセージ
        """
        if s.logger != None:
            s_dec = dec.FC_YELLOW
            e_dec = dec.END
            if s.is_supposed_debug:
                s_dec = dec.fc_blue
                e_dec = dec.END
            s.logger.warning(f"{s_dec}{msg}{e_dec}")
    def log_error(s,msg:str):
        """プログラム上の処理が中断したり、停止した場合の情報を出力します。

        Parameters
        ----------
        msg : str
            出力メッセージ
        """
        if s.logger != None:
            s_dec = dec.FC_RED
            e_dec = dec.END
            if s.is_supposed_debug:
                s_dec = dec.FC_RED
                e_dec = dec.END
            s.logger.critical(f"{s_dec}{msg}{e_dec}")
    def log_critical(s,msg:str):
        """システム全体や連携システムに影響する重大な問題が発生した場合の情報を出力します。

        Parameters
        ----------
        msg : str
            出力メッセージ
        """
        if s.logger != None:
            s_dec = dec.BC_RED
            e_dec = dec.END
            if s.is_supposed_debug:
                s_dec = dec.FC_RED + dec.FB_REVERSE
                e_dec = dec.END
            s.logger.critical(f"{s_dec}{msg}{e_dec}")
    def raise_Exception(s,msg:str):
        """汎用の例外を発生させます。

        Parameters
        ----------
        msg : str
            例外メッセージ
        """
        if s.is_supposed_debug:
            # vscodeで例外投げないのは単なる趣味です。(ポップアップうざい)
            s.log_error(msg)
            sys.exit(1)
        else:
            raise Exception(msg)
    def raise_FileNotFound(s,path:str):
        """ファイルがない場合の例外を発生させます。

        Parameters
        ----------
        path : str
            ファイルパス
        """
        msg = f"file not found.({path})"
        if s.is_supposed_debug:
            # vscodeで例外投げないのは単なる趣味です。(ポップアップうざい)
            s.log_error(msg)
            sys.exit(1)
        else:
            raise FileNotFoundError(msg)
    def raise_NotFound(s,target:str,type_name:str):
        """ファイル以外の何かが不在である場合の例外を発生させます。

        Parameters
        ----------
        target : str
            存在しないものインスタンス文字列
        type_name : str
            存在しないものの名前
        """
        msg = f"{type_name}({target}) not found."
        if s.is_supposed_debug:
            # vscodeで例外投げないのは単なる趣味です。(ポップアップうざい)
            s.log_error(msg)
            sys.exit(1)
        else:
            raise Exception(msg)
    def raise_ValueRange(s,value,min=None,max=None):
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

        if s.is_supposed_debug:
            # vscodeで例外投げないのは単なる趣味です。(ポップアップうざい)
            s.log_error(msg)
            sys.exit(1)
        else:
            raise ValueError(msg)
    def caller_file_name(s,back_count:int=2)->str:
        """呼び出し元の関数のあるファイル名を取得します。

        Returns
        -------
        str
            呼び出し元関数のあるファイル名
        """
        res = ""
        cur = inspect.currentframe()
        back = s.__stack_back(cur,back_count)
        if back != None:
            code = back.f_code
            if code != None:
                res = code.co_filename
            else:
                s.raise_Exception(f"呼び出し元の情報が取得できませんでした。(code='{code}')")
        else:
            s.raise_Exception(f"呼び出し元の情報が取得できませんでした。(back='{back}')")
        return res
    def caller_function_name(s,back_count:int=2)->str:
        """呼び出し元の関数名を取得します。

        Returns
        -------
        str
            呼び出し元関数名
        """
        res = ""
        cur = inspect.currentframe()
        back = s.__stack_back(cur,back_count)
        if back != None:
            code = back.f_code
            if code != None:
                res = code.co_name
            else:
                s.raise_Exception(f"呼び出し元の情報が取得できませんでした。(code='{code}')")
        else:
            s.raise_Exception(f"呼び出し元の情報が取得できませんでした。(back='{back}')")
        return res
    def caller_line_no(s,back_count:int=2)->int:
        """呼び出し元の行番号を取得します。

        Returns
        -------
        int
            呼び出し元の行番号
        """
        res = 0
        cur = inspect.currentframe()
        back = s.__stack_back(cur,back_count)
        if back != None:
            res = back.f_lineno
        else:
            s.raise_Exception(f"呼び出し元の情報が取得できませんでした。cur='{cur}')")
        return res
    def caller_locals(s,back_count:int=2)->dict[str,Any]:
        """呼び出し元の関数のローカル変数取得

        Returns
        -------
        str
            呼び出し元関数のあるファイル名
        """
        res = dict()
        cur = inspect.currentframe()
        back = s.__stack_back(cur,back_count)
        if back != None:
            res = back.f_locals
        else:
            s.raise_Exception(f"呼び出し元の情報が取得できませんでした。(back='{back}')")
        return res
    def __stack_back(s,cur,count:int=1):
        res = None
        for i in range(0,count,1):
            back = cur.f_back
            if back == None:
                res = back
                s.raise_Exception(f"呼び出し元の情報が取得できませんでした。(i={i}, cur='{cur}')")
                break
            else:
                cur = back
                res = cur
        return res
    @property
    def cur_file_name(s)->str:
        """現在のファイル名を取得します。

        Returns
        -------
        str
            現在のファイル名
        """
        res = ""
        cur = inspect.currentframe()
        if cur != None:
            back1 = cur.f_back
            if back1 != None:
                code = back1.f_code
                if code != None:
                    res = code.co_filename
        return res
    @property
    def cur_function_name(s)->str:
        """現在の関数名を取得します。

        Returns
        -------
        str
            現在の関数名
        """
        res = ""
        cur = inspect.currentframe()
        if cur != None:
            back1 = cur.f_back
            if back1 != None:
                code = back1.f_code
                if code != None:
                    res = code.co_name
        return res
    @property
    def cur_line_no()->int:
        """現在の行番号を取得します。

        Returns
        -------
        int
            現在の行番号
        """
        res = 0
        cur = inspect.currentframe()
        if cur != None:
            back1 = cur.f_back
            if back1 != None:
                res = back1.f_lineno
        return res

    #------------------------------------------------------------------------
    # HASH
    #------------------------------------------------------------------------
    def cnv_str_to_sha256(s,src:str)->str:
        """文字列をSHA256に変換します。
        Returns
        -------
        str
            SHA256
        """
        hashlib = s.load_module("hashlib")
        return hashlib.sha256(src.encode()).hexdigest()
    def cnv_str_to_sha512(s,src:str)->str:
        """文字列をSHA512に変換します。
        Returns
        -------
        str
            SHA512
        """
        hashlib = s.load_module("hashlib")
        return hashlib.sha512(src.encode()).hexdigest()
    #------------------------------------------------------------------------
    # UUID
    #------------------------------------------------------------------------
    @property
    def uuid(s)->str:
        """UUIDを生成して取得します。

        Returns
        -------
        str
            UUID。書式は区切り文字無しの小文字(固定)です
        """
        id = s.load_module("uuid")
        return id.uuid4().hex.lower()
    #------------------------------------------------------------------------
    # LIST
    #------------------------------------------------------------------------
    def loop(s,data:list,method,last_method)->list:
        """ループ処理を行う

        最後の要素だけセパレータを付けない場合など、
        少し処理が違う場合などに使用すること

        Parameters
        ----------
        data : list
            ループ処理の対象となるデータ
        method : 
            ループ処理の内容(ただし、最後のデータは除く)
        last_method : 
            ループ最後のデータに対する処理の内容
        """
        # 途中の要素を処理
        for d in s.get_not_tail(data):
            method(d)
        last_method(s.get_tail(data))
    def get_tail(s,items:list)->Any:
        """末尾の要素を取得する
        """
        res = None
        if len(items) > 0:
            res = items[-1]
        return res
    def get_not_tail(s,items:list)->list:
        """末尾ではない要素を取得する
        """
        res = []
        if len(items) > 0:
            res = items[:-1]
        return res
    #------------------------------------------------------------------------
    # DICT
    #------------------------------------------------------------------------
    def get_max_key_len(s,src:dict)->int:
        """辞書型のキーの最大長を取得します。

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
        res = max([len(str(key)) for key in src.keys()])
        return res
    #------------------------------------------------------------------------
    # CLASS
    #------------------------------------------------------------------------
    def add_instance_method(s,target_instance:Any,method:Method,name:str=""):
        """インスタンスに動的にメソッドを追加する。

        すでにメソッドがある場合は上書きになりますので注意してください。

        Parameters
        ----------
        target_instance : Any
            追加対象のインスタンス
        method : Method
            追加するメソッド
        name : str
            メソッド名, by default empty string("").
            空文字列の場合はmethodの名前を使用します。
        """
        if name == "":
            name = method.__name__
        if name in target_instance.__dict__.keys():
            delattr(target_instance,name)
        setattr(target_instance, name, method )
    #------------------------------------------------------------------------
    # DATE/TIME
    #------------------------------------------------------------------------
    def cnv_datetime_to_YYYYMMDD(s,src:datetime, sep:str=SEP_DATE2DATE)->str:
        """日付をYYYYMMDD形式の文字列に変換する

        Parameters
        ----------
        src : datetime
            変換する日付データ
        sep : str, optional
            年月日の区切り文字, by default DATE_SEP

        Returns
        -------
        str
            YYYYMMDD形式の日付文字列
        """
        res = src.strftime(f"%Y{sep}%m{sep}%d")
        return res
    def cnv_datetime_to_HHMMSS(s,src:datetime, sep:str=SEP_TIME2TIME)->str:
        """日時をHHMMSS形式の文字列に変換する

        Parameters
        ----------
        src : datetime
            変換する日時データ
        sep : str, optional
            時分秒の区切り文字, by default SEP_TIME2TIME

        Returns
        -------
        str
            HHMMDD形式の時間文字列
        """
        res = src.strftime(f"%H{sep}%M{sep}%S")
        return res
    def cnv_datetime_to_YYYYMMDDHHMMSS(
            s,
            src:datetime,
            date_sep:str=SEP_DATE2DATE,
            time_sep:str=SEP_TIME2TIME,
            date_time_sep:str=SEP_DATE2TIME)->str:
        """日時をYYYYMMDDHHMMSS形式の文字列に変換する

        Parameters
        ----------
        src : datetime
            変換する日時データ
        date_sep : str, optional
            年月日の区切り文字, by default SEP_DATE2DATE
        time_sep : str, optional
            時分秒の区切り文字, by default SEP_TIME2TIME
        date_time_sep : str, optional
            年月日と時分秒を区切る文字, by default SEP_DATE2TIME

        Returns
        -------
        str
            YYYYMMDDHHMMSS形式の日付文字列
        """
        date = s.cnv_datetime_to_YYYYMMDD(src,date_sep)
        time = s.cnv_datetime_to_HHMMSS(src,time_sep)
        res = f"{date}{date_time_sep}{time}"
        return res
    def cnv_str_to_datetime(s,src:str, format:str="%Y/%m/%d %H:%M:%S"):
        """文字列をdatetimeに変換します
        """
        res = datetime.datetime.strptime(src, format)
        return res
    def cnv_datetime_to_serial(s,src:datetime):
        """datetimeをシリアル値に変換します
        """
        zero_day = datetime.datetime(1899,12,31)
        irregular_next = datetime.datetime(1900,3,1)
        res = (src - zero_day).days
        if src >= irregular_next:
            res = res + 1
        return res
    def cnv_datetime_to_dict(s,src:datetime)->dict:
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
        res["YYYYMMDDHHMMSS"] = src.strftime("%Y%m%d%H%M%S")
        res["YYYYMMDD"] = src.strftime("%Y%m%d")
        res["YYYY"] = src.strftime("%Y")
        res["MM"] = src.strftime("%m")
        res["DD"] = src.strftime("%d")
        res["HHMMSS"] = src.strftime("%H%M%S")
        res["YYYY/MM/DD"] = s.cnv_datetime_to_YYYYMMDD(src,"/")
        res["YYYY-MM-DD"] = s.cnv_datetime_to_YYYYMMDD(src,"-")
        res["HH:MM:SS"] = src.strftime("%H:%M:%S")
        res["YYYY/MM/DD HH:MM:SS"] = s.cnv_datetime_to_YYYYMMDDHHMMSS(src,"/",":"," ")
        res["YYYY-MM-DD HH:MM:SS"] = s.cnv_datetime_to_YYYYMMDDHHMMSS(src,"-",":"," ")
        res["YYYY年MM月DD日"] = src.strftime("%Y年%m月%d日")
        res["YYYY年MM月DD日(曜日)"] = src.strftime("%Y年%m月%d日(%A)")
        res["YYYY年MM月DD日(曜日short)"] = src.strftime("%Y年%m月%d日(%a)")
        res["曜日"]=src.strftime("%A")
        res["曜日short"]=src.strftime("%a")
        return res
    def add_days(s,src,days):
        """datetimeに指定の日数を加算または減算します
        """
        td = datetime.timedelta(days=days)
        return (src + td)
    def update_datetime(src:datetime.datetime, 
                        year:int=-1,month:int=-1,day:int=-1, hour:int=-1,minute:int=-1,second:int=-1,microsecond:int=-1
                        )->datetime.datetime:
        """日時の一部を更新して返します

        変更する部分以外は値の設定は不要です。

        Returns
        -------
        datetime.datetime
            更新後の値
        """
        if year == -1:
            year = src.year
        if month == -1:
            month = src.month
        if day == -1:
            day = src.day
        if hour == -1:
            hour = src.hour
        if minute == -1:
            minute = src.minute
        if second == -1:
            second = src.second
        if microsecond == -1:
            microsecond = src.microsecond
        res = datetime.datetime(year=year,month=month,day=day,hour=hour,minute=minute,second=second,microsecond=microsecond)
        return res
    #------------------------------------------------------------------------
    # FILE/DIRECTORY/PATH
    #------------------------------------------------------------------------
    @property
    def cur_dir(s)->str:
        """カレントディレクトリを取得する
        """
        return os.getcwd()
    @cur_dir.setter
    def cur_dir(s,path:str):
        """カレントディレクトリを変更する
        """
        os.chdir(path)
    def is_exist(s,path):
        """ファイルの有無確認
        """
        return os.path.exists(path)
    def is_file(s,path):
        """ファイルかどうかを確認
        """
        return os.path.isfile(path)
    def is_dir(s,path:str):
        """ディレクトリかどうかを判別する
        """
        return os.path.isdir(path)
    def file_size(s,path:str):
        """ファイルサイズ取得
        """
        return os.path.getsize(path)
    def file_update_time(s,path:str):
        """最終更新日時取得
        """
        return os.path.getmtime(path)
    def is_abs_path(s,path)->bool:
        """絶対パスかどうかを返します。
        """
        return os.path.isabs(path)
    def __cnv_path_sep(s,path:str, sep:str=SEP_DIR2FILE)->str:
        """パスの区切り文字を統一します。

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
        res = path.replace("/",sep)
        res = res.replace("\\",sep)
        return res
    def cnv_abs_full_path(s,path:str,sep:str=SEP_DIR2FILE)->str:
        """指定のパスを絶対パスに変換します。

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
        if s.is_abs_path(path):
            res = path
        else:
            res = os.path.abspath(path)
        res = s.__cnv_path_sep(res,sep)
        s.log_info(f"function : {s.cur_function_name} > res:{res}")
        return res
    def cnv_abs_dir_path(s,path:str,sep:str=SEP_DIR2FILE)->str:
        """絶対パス形式のディレクトリパスに変換します。

        Parameters
        ----------
        path : str
            変換対象パス
        sep : str, optional
            パスの区切り文字, by default SEP_DIR2FILE

        Returns
        -------
        str
            絶対パス形式のディレクトリパスに変換します。
        """
        abs_path = s.cnv_abs_full_path(path,sep)
        s.log_info(f"function : {s.cur_function_name} > abs_path:{abs_path}")
        res = ""
        if s.is_dir(abs_path):
            res = abs_path
        else:
            res = os.path.dirname(abs_path)
        s.log_info(f"function : {s.cur_function_name} > res:{res}")
        return res
    def cnv_abs_file_path_none_ext(s,path:str,sep:str=SEP_DIR2FILE)->str:
        """絶対パス形式のファイルパス(拡張子は除く)に変換します。

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
        abs_path = s.cnv_abs_full_path(path,sep)
        res = ""
        if s.is_dir(abs_path):
            s.raise_Exception(f"ファイルパスの引数(path)にディレクトリパスが指定されました。\n(path:{path})")
        else:
            res = abs_path
        res = os.path.splitext(res)[0]
        return res
    def cnv_file_name(s,path:str)->str:
        """ファイル名(拡張子含む)に変換します。

        Parameters
        ----------
        path : str
            変換対象のパス

        Returns
        -------
        str
            ファイル名(拡張子含む)
        """
        res = os.path.basename(path)
        return res
    def cnv_file_name_none_ext(s,path:str)->str:
        """ファイル名(拡張子除く)に変換します。

        拡張子は最初の区切り文字"."の後ろの文字列と判別します。
        例）aaa.tar.gzの場合はtar.gzを拡張子として扱います。

        Parameters
        ----------
        path : str
            変換対象のパス

        Returns
        -------
        str
            ファイル名
            ファイル名に拡張子区切り文字(".")と拡張子は含まれません。
        """
        res = os.path.splitext(os.path.basename(path))[0]
        return res
    def cnv_parent_dir(s,src:str)->str:
        """親ディレクトリパスに変換します。

        Parameters
        ----------
        src : str
            対象パス

        Returns
        -------
        str
            親ディレクトリパス
        """
        pathlib = s.load_module("pathlib")
        p = pathlib.Path(src)
        res = str(p.parent)
        return res
    def cnv_file_ext(s,path:str)->str:
        """拡張子に変換します。

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
        name = os.path.basename(path)
        name_parts = list(os.path.splitext(name))
        res = ""
        if len(name_parts)>=2:
            name_parts.pop(0)
            res = ".".join(name_parts)
        return res
    def file_sha256(s,path:str)->str:
        """SHA256取得
        """
        res = ""
        with open(path,"rb") as file:
            fileData = file.read()
            hashlib = s.load_module("hashlib")
            res = hashlib.sha256(fileData).hexdigest()
        return res
    def file_sha512(s,path:str)->str:
        """SHA512取得
        """
        res = ""
        with open(path,"rb") as file:
            fileData = file.read()
            hashlib = s.load_module("hashlib")
            res = hashlib.sha512(fileData).hexdigest()
        return res
    def load_bin(s,path:str)->bytes:
        """バイナリファイルを読みだします。

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
    def load_text(s,path:str,encoding:str=ENC_DEF)->str:
        """テキストファイルを読み出します。

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
    def load_text_lines(s,path:str,encoding:str=ENC_DEF)->list[str]:
        """テキストファイルをリスト形式で読みだします。

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
    def save_text(s,path:str,text:Any,encoding:str=ENC_DEF,ret_code:str=RET_CODE_DEF):
        """テキストファイルに保存します。

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
        s.make_dir(path)
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
                        s.raise_Exception(f"改行コードの指定が異常です ret_code={ret_code}")
                text = text.replace("\n",ret_code)
                f.write(text)
        elif isinstance(text,list[str]):
            with open(path, mode="w", encoding=encoding) as f:
                f.writelines([line + ret_code for line in text])
        else:
            s.raise_Exception(f"未対応の型({type(text)})が引数(text)に渡されました")
    def load_json(s,path: str) -> dict:
        json = s.load_module("json")
        text = s.load_text(path)
        res = json.loads(text)
        return res
    def save_json(s,path:str,data,encoding:str=ENC_DEF):
        json = s.load_module("json")
        s.make_dir(path)
        codecs = s.load_module("codecs")
        with codecs.open(path , mode="w", encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False,indent=s.INDENT_JSON_DEF, sort_keys=True)
    def remove_file(s,path:str):
        """ファイルを削除する
        """
        os.remove(path)
    def remove_dir(s,path:str):
        """ディレクトリを削除する
        """
        path = s.cnv_abs_dir_path(path)
        shutil = s.load_module("shutil")
        shutil.rmtree(path=path,ignore_errors=True)
    def make_dir(s,path:str):
        path = s.cnv_abs_dir_path(path)
        s.log_info(f"function : {s.cur_function_name} > path:{path}")
        os.makedirs(name=path,exist_ok=True)
    def copy_dir_tree(s,src:str, dest:str, not_ptn=None):
        """ディレクトリツリーをコピーします
        """
        s.log_info(f"function : {s.cur_function_name} > src:{src}")
        s.log_info(f"function : {s.cur_function_name} > dest:{dest}")
        shutil = s.load_module("shutil")
        if not_ptn is None:
            shutil.copytree(src, dest, dirs_exist_ok=True)
        else:
            shutil.copytree(src, dest, ignore=not_ptn, dirs_exist_ok=True)
    def copy_file(s,src:str,dest:str):
        """ファイルコピー

        Parameters
        ----------
        src : str
            コピー元のファイルパス
        dest : str
            コピー先のファイルパス
        """
        s.log_info(f"function : {s.cur_function_name} > src:{src}")
        s.log_info(f"function : {s.cur_function_name} > dest:{dest}")
        shutil = s.load_module("shutil")
        s.make_dir(dest)
        shutil.copy2(src,dest)
    def move_file(s,src:str,dest:str):
        """ファイルを移動する
        """
        os.replace(src,dest)
    #------------------------------------------------------------------------
    # LIBRARY
    #------------------------------------------------------------------------
    def load_module(s,name):
        """モジュールを動的にimportします。

        一度、importしたモジュールは辞書型に保存して流用します。
        動的にimportした場合はvscodeなどのコード補完が効かないので注意してください。
        """
        res = s.loaded_modules.get(name, None)
        if res == None:
            res = import_module(name)
            s.loaded_modules[name]=res
        return res

class cmd_app_internal:
    """コマンドアプリ(本体)
    """
    #========================================================================
    #
    # CONST
    #
    #========================================================================
    #
    # 定数の名前が安定しないため命名規則をメモしておく
    # 目的の対象_種別の順に記載する
    #
    # 例えば以下のようになる。
    # ENC_DEF      : エンコードが欲しい->デフォルトで使用するもの
    # SEP_DIR2FILE : 区切り文字が欲しい->ディレクトリとファイルを区切るためのもの
    #
    EVAR_NAME_PATH_LIST = "path_list_path"
    """環境変数名：パスリストファイルのパス
    """

    EVAR_ENV_ID = "env_id"
    """環境変数名：環境ID

    環境IDは本スクリプトなどを含めたvscode環境の固有IDです。
    """

    ID_CLASS = "bd2c738c64234e478a081006e744550e"
    """クラス識別用ID
    """
    #========================================================================
    #
    # VARIABLES
    #
    #========================================================================
    utility:cmd_app_utility
    """ユーティリティ関数
    """

    args_cfg:dict=dict()
    """引数設定
    """
    args:list[str]
    """起動引数
    """
    params:dict=dict()
    """mainに渡す引数
    """

    app_id:str = ""
    """アプリケーション固有ID
    """

    path_list:dict=dict()
    """パスリスト
    """
    #========================================================================
    #
    # METHOD
    #
    #========================================================================

    #------------------------------------------------------------------------
    # METHOD / INITIALIZE
    #------------------------------------------------------------------------
    def __init__(s,id:str,args:list[str]) -> None:
        """コマンドアプリを生成します。

        Parameters
        ----------
        id : str
            アプリケーション固有ID(アプリケーション毎にUUIDを設定してください。)
        """
        s.app_id = id
        s.args = args
        s.utility = cmd_app_utility(args[0])

    #------------------------------------------------------------------------
    # METHOD / MAIN PROCESS
    #------------------------------------------------------------------------

    def pre_main(s):
        u = s.utility
        u.log_info(f"---------------------------------------------------")
        u.log_info(f"{s.args[0]}")
        u.log_info(f"---------------------------------------------------")
        u.log_info(f"cur_dir  : {os.getcwd()}")
        for i in range(0,len(s.args),1):
            u.log_info(f"sys.argv : {s.args[i]}")
        for k,v in s.args_cfg.items():
            u.log_info(f"args_cfg : {k} : {v}")
        s.__set_params()
        for k,v in s.params.items():
            u.log_info(f"params : {k} : {v}")
        s.__set_args_value()
        return
    def post_main(s):
        s.utility.log_info(f"---------------------------------------------------")
        return
    def __set_params(s):
        """起動引数を辞書型としてparamsに設定します。
        """
        re = s.utility.load_module("re")
        ptn = re.compile("^-(?P<key>[a-z][0-9a-z_]*):(?P<value>.*)$")
        for i in range(1,len(s.args),1):
            arg = s.args[i]
            m = ptn.match(arg)
            if m:
                k = m.group("key")
                v = m.group("value")
                s.params[k]=v
            else:
                s.utility.raise_Exception(f"起動パラメータがパターンにマッチしませんでした。(arg='{arg}',pattern='{ptn.pattern}')")
    def __set_args_value(s):
        """paramsの内容をargs_cfgに従って展開します。
        """
        for (cfg_key,cfg_val) in s.args_cfg.items():
            s.utility.log_info(f"cfg_key:{cfg_key}")
            s.utility.log_info(f"cfg_val:{cfg_val}")
            cfg_type = cfg_val.get("type","")
            if not cfg_key in s.params.keys():
                s.utility.raise_Exception(f"起動時に指定された引数に{cfg_key}がありません。\nparams=({s.params})')")
            prm_val  = s.params[cfg_key]
            match cfg_type:
                case "text":
                    # 既にセットされているので処理不要
                    pass
                case "path_list":
                    s.params[cfg_key] = list(prm_val.split(os.pathsep))
                    pass
                case "path_name":
                    if prm_val in s.env_path_list.keys():
                        s.params[cfg_key] = s.env_path_list[prm_val]
                    else:
                        s.utility.raise_Exception(f"起動引数({cfg_key})で指定されたパス名({prm_val})は存在しません。")
                case _:
                    s.utility.raise_Exception(f"未対応の型が指定されました。cfg_type='{cfg_type}'")
    #========================================================================
    #
    # METHOD / UTILITY
    #
    #========================================================================
    #------------------------------------------------------------------------
    # ENVIRONMENT
    #------------------------------------------------------------------------
    @property
    def env_id(s)->str:
        """環境変数ID
        Returns
        -------
        str
            環境変数IDを取得します。
        """
        return os.environ.get(s.EVAR_ENV_ID,"")
    @property
    def path_list_path(s)->str:
        """パスリストファイル(JSON)へのパスを取得します。

        Returns
        -------
        str
            パスリストファイルへのパス
        """
        
        return os.environ.get(s.EVAR_NAME_PATH_LIST,"")
    @property
    def user_name(s)->str:
        """ユーザ名を取得する

        Returns
        -------
        str
            ユーザー名
        """
        getpass = s.utility.load_module("getpass")
        return getpass.getuser()
    #------------------------------------------------------------------------
    # PATH LIST
    #------------------------------------------------------------------------
    def load_path(s)->dict:
        path = s.path_list_path
        plp = None
        try:
            plp = s.utility.load_json(path)
        except:
            plp = dict()
        return plp
    def __get_path_list(s,id:str)->dict:
        """パスリスト取得

        Parameters
        ----------
        id : str
            取得するパスリストID

        Returns
        -------
        dict
            パスリスト
        """
        res = {}
        if id == "":
            s.utility.raise_NotFound(id,"path list ID")
        else:
            if id in s.path_list.keys():
                res = s.path_list[id]
            else:
                s.path_list[id]=res
        return res
    def update_path(s,src:dict, id:str=env_id)->dict:
        dest = s.load_path()
        src_id = src.get(id,{})
        dest_id = dest.get(id,{})
        dest_id.update(src_id)
        dest[id]=dest_id
        path = s.path_list_path
        s.utility.save_json(path,dest)

    @property
    def env_path_list(s)->dict:
        """環境固有パスリスト取得

        Returns
        -------
        dict
            パスリスト
        """
        return s.__get_path_list(s.env_id)
    @property
    def class_path_list(s)->dict:
        """クラス固有パスリスト取得

        Returns
        -------
        dict
            パスリスト
        """
        return s.__get_path_list(s.ID_CLASS)
    @property
    def application_path_list(s)->dict:
        """アプリケーションパスリスト取得

        Returns
        -------
        dict
            アプリケーションパスリスト
        """
        return s.__get_path_list(s.app_id)
    @property
    def user_path_list(s)->dict:
        """ユーザーパスリスト取得

        Returns
        -------
        dict
            パスリスト
        """
        return s.__get_path_list(s.user_name)
class cmd_app:
    """コマンドアプリ基底クラス
    """
    #========================================================================
    #
    # CONST
    #
    #========================================================================
    NAME_METHOD = "main"
    """reg_mainで本クラスのインスタンスに登録されるメソッド名
    """

    RE_PATTERN_PARAM="^[a-z][0-9a-z_]*$"
    """起動引数名の正規表現パターン
    """

    #========================================================================
    #
    # VARIABLES
    #
    #========================================================================
    re_pattern_param=None
    """起動引数の正規表現パターン(compile結果)
    """

    base_cmd_app:cmd_app_internal=None
    """private処理、変数などを格納する変数
    """
    #========================================================================
    #
    # METHOD
    #
    #========================================================================
    def __init__(s,id:str, args=sys.argv) -> None:
        """コマンドアプリを生成します。

        Parameters
        ----------
        id : str
            アプリケーション固有ID(アプリケーション毎にUUIDを設定してください。)
        """
        s.base_cmd_app = cmd_app_internal(id,args)
        u = s.base_cmd_app.utility
        re = u.load_module("re")
        s.re_pattern_param = re.compile(s.RE_PATTERN_PARAM)
    def start(s):
        i = s.base_cmd_app
        i.pre_main()
        if s.NAME_METHOD in s.__dict__.keys():
            s.main(s, **i.params)
        else:
            i.utility.raise_Exception(f"起動対象の関数{s.NAME_METHOD}が設定されていません。{s.reg_main.__name__}メソッドで登録してください。")
        i.post_main()
    def reg_main(s,func:Method):
        """起動関数登録

        func : Method
            コマンドとして起動する関数
            引数はargs_cfgに合わせてください。
        """
        s.base_cmd_app.utility.add_instance_method(s,func,s.NAME_METHOD)
    def add_param_cfg_text(s,name:str):
        """起動引数設定にテキスト形式追加

        Parameters
        ----------
        name : str
            起動引数名
        """
        cmp = s.re_pattern_param
        m = cmp.match(name)
        if m:
            s.base_cmd_app.args_cfg[name] = {"type":"text"}
    def add_param_cfg_path_list(s,name:str):
        """起動引数設定にパスリスト形式追加

        Parameters
        ----------
        name : str
            起動引数名
        """
        cmp = s.re_pattern_param
        m = cmp.match(name)
        if m:
            s.base_cmd_app.args_cfg[name] = {"type":"path_list"}
    def add_param_cfg_path_name(s,name:str):
        """起動引数設定にパス名形式追加

        Parameters
        ----------
        name : str
            起動引数名
        """
        cmp = s.re_pattern_param
        m = cmp.match(name)
        if m:
            s.base_cmd_app.args_cfg[name] = {"type":"path_name"}
