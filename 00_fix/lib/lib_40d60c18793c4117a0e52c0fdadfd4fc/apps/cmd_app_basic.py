"""基本的なコンソール(シェル)アプリの基底クラス

ゆるくアプリが作れることを目指します。
"""

import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl

class cmd_app_internal:
    """コマンドアプリ(内部構造)"""
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
    ID_CLASS = "bd2c738c64234e478a081006e744550e"
    """クラス識別用ID"""
    NAME_METHOD = "main"
    """reg_mainで本クラスのインスタンスに登録されるメソッド名"""
    RE_PATTERN_PARAM="^[a-z][0-9a-z_]*$"
    """起動引数名の正規表現パターン"""
    #========================================================================
    # VARIABLES
    #========================================================================
    args_cfg:dict=dict()
    """引数設定"""
    args:list[str]
    """起動引数"""
    params:dict=dict()
    """mainに渡す引数"""
    app_id:str = ""
    """アプリケーション固有ID"""
    __re_pattern_param=None
    """起動引数の正規表現パターン(compile結果)
    """
    #========================================================================
    # METHOD
    #========================================================================
    #------------------------------------------------------------------------
    # METHOD / INITIALIZE
    #------------------------------------------------------------------------
    def __init__(s,id:str,args:list[str]=None) -> None:
        """コマンドアプリを生成します。

        Parameters
        ----------
        id : str
            アプリケーション固有ID(アプリケーション毎にUUIDを設定してください。)
        args : list[str] or None
            起動引数を渡します。
            Noneの場合はsys.argvから取得するため、デバッグ時に任意の引数を渡したいときのみ使用してください。
        """
        s.app_id = id
        if args == None:
            args = a.startup_params()
        s.args = args
        s.__re_pattern_param = a.re_compile(s.RE_PATTERN_PARAM)
    #------------------------------------------------------------------------
    # METHOD / MAIN PROCESS
    #------------------------------------------------------------------------
    def pre_main(s):
        a.log_info(f"---------------------------------------------------")
        a.log_info(f"{s.args[0]}")
        a.log_info(f"---------------------------------------------------")
        a.log_info(f"cur_dir  : {a.get_cur_dir()}")
        for i in range(0,len(s.args),1):
            a.log_info(f"sys.argv[{i}] : {s.args[i]}")
        for k,v in s.args_cfg.items():
            a.log_info(f"args_cfg : {k} : {v}")
        s.set_params()
        for k,v in s.params.items():
            a.log_info(f"params : {k} : {v}")
        s.set_args_value()
        return
    def post_main(s):
        a.log_info(f"---------------------------------------------------")
        return
    def set_params(s):
        """起動引数を辞書型としてparamsに設定します。
        """
        pattern = "^-(?P<key>[a-z][0-9a-z_]*):(?P<value>.*)$"
        cmp = a.re_compile(pattern)
        for i in range(1,len(s.args),1):
            arg = s.args[i]
            m = a.re_match(arg,compiled_re=cmp)
            if m:
                k = a.re_group(m,"key")
                v = a.re_group(m,"value")
                s.params[k]=v
            else:
                a.raise_Exception(f"起動パラメータがパターンにマッチしませんでした。(arg='{arg}',re pattern='{pattern}')")
    def set_args_value(s):
        """paramsの内容をargs_cfgに従って展開します。
        """
        for (cfg_key,cfg_val) in s.args_cfg.items():
            a.log_info(f"cfg_key:{cfg_key}")
            a.log_info(f"cfg_val:{cfg_val}")
            cfg_type = cfg_val.get("type","")
            if not cfg_key in s.params.keys():
                a.raise_Exception(f"起動時に指定された引数に{cfg_key}がありません。\nparams=({s.params})')")
            prm_val  = s.params[cfg_key]
            match cfg_type:
                case "text":
                    # 既にセットされているので処理不要
                    pass
                case "path_list":
                    s.params[cfg_key] = list(str(prm_val).split(a.SEP_PATH2PATH))
                    pass
                case "path_name":
                    evn_pl =pl.env_path_list()
                    if prm_val in evn_pl.keys():
                        s.params[cfg_key] = evn_pl[prm_val]
                    else:
                        a.raise_Exception(f"起動引数({cfg_key})で指定されたパス名({prm_val})は存在しません。")
                case _:
                    a.raise_Exception(f"未対応の型が指定されました。cfg_type='{cfg_type}'")
    def start(s):
        s.pre_main()
        if s.NAME_METHOD in s.__dict__.keys():
            a.log_info(s.params)            
            s.main(s, **s.params)
        else:
            a.raise_Exception(f"起動対象の関数{s.NAME_METHOD}が設定されていません。{s.reg_main.__name__}メソッドで登録してください。")
        s.post_main()
    def add_param_cfg_text(s,name:str):
        """起動引数設定にテキスト形式追加"""
        if a.re_match(name,compiled_re=s.__re_pattern_param):
            s.args_cfg[name] = {"type":"text"}
    def add_param_cfg_path_list(s,name:str):
        """起動引数設定にパスリスト形式追加"""
        if a.re_match(name,compiled_re=s.__re_pattern_param):
            s.args_cfg[name] = {"type":"path_list"}
    def add_param_cfg_path_name(s,name:str):
        """起動引数設定にパス名形式追加"""
        if a.re_match(name,compiled_re=s.__re_pattern_param):
            s.args_cfg[name] = {"type":"path_name"}

class cmd_app:
    """コマンドアプリ基底クラス
    """
    #========================================================================
    # VARIABLES
    #========================================================================
    __cmd_app:cmd_app_internal=None
    """private処理、変数などを格納する変数
    """
    #========================================================================
    # METHOD
    #========================================================================
    def __init__(s,id:str, args=None) -> None:
        """コマンドアプリを生成します。

        Parameters
        ----------
        id : str
            アプリケーション固有ID(アプリケーション毎にUUIDを設定してください。)
        args : list[str] or None
            起動引数を渡します。
            Noneの場合はsys.argvから取得するため、デバッグ時に任意の引数を渡したいときのみ使用してください。
        """
        s.__cmd_app = cmd_app_internal(id,args)
    def start(s):
        s.__cmd_app.start()
    def reg_main(s,func:a.TYPE_METHOD):
        """起動関数登録

        func : Method
            コマンドとして起動する関数
            引数はargs_cfgに合わせてください。
        """
        a.add_method(s.__cmd_app,func,s.__cmd_app.NAME_METHOD)
    def add_param_cfg_text(s,name:str):
        """起動引数設定にテキスト形式追加

        Parameters
        ----------
        name : str
            起動引数名
        """
        s.__cmd_app.add_param_cfg_text(name)
    def add_param_cfg_path_list(s,name:str):
        """起動引数設定にパスリスト形式追加

        Parameters
        ----------
        name : str
            起動引数名
        """
        s.__cmd_app.add_param_cfg_path_list(name)
    def add_param_cfg_path_name(s,name:str):
        """起動引数設定にパス名形式追加

        Parameters
        ----------
        name : str
            起動引数名
        """
        s.__cmd_app.add_param_cfg_path_name(name)
