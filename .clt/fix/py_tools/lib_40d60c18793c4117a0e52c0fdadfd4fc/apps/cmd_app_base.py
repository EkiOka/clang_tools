"""基本的なコンソール(シェル)アプリの基底クラス

ゆるくアプリが作れることを目指します。
"""

import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import inspect


class cmd_app:
    """コマンドアプリ基底クラス

    ■ 基本使用方法
    本クラスは以下の手順で使用してください。
    1. 本クラスを継承したクラスを作成する
    2. 1.のクラスのインスタンスを作成する。
        2.1. `id`にはユニークなIDを指定してください。(UUIDなど)
        2.2. 特定のパラメータでデバッグしたい場合は、`args`を設定してください。
    3. 継承したクラスにdef main(self)メソッドを追加してください。
        3.1. `main`以外の名前を使用したい場合は`startup_method`を設定してください。
    4. startメソッドを呼び出してください。

    ■ 起動パラメータの渡し方
    外部からコンフィグ(設定値)を渡したい場合は以下の通りとします。
    0. 継承クラスの`__init__`からデフォルト値として`default_config`にセットする
    1. 起動引数として渡す。
        1.1. この方法ではライブラリの`re`にて、`RE_PATTERN_PARAM`で指定されたパターンに一致したものを使用します。
        1.2. 一致しないパターンの場合はコンフィグファイルのパスとして認識します。
        1.3. この方法ではパラメータは文字列しか取り扱いできないため注意すること
    2. 起動元の.pyファイルと同名のファイルラベルを持つYAMLファイルをコンフィグファイルとして認識する
    3. 起動元の.pyふぃあると同名のファイルラベルを持つディレクトリ内にあるYAMLファイルをコンフィグファイルとして認識する
    4. cmd_appの `clt_` + 生成引数(`id`) の環境変数で指定されたマスクをライブラリの`glob`で検索し、一致したファイルをコンフィグファイルとして認識する
    5. 上記、1～4で読み出されたコンフィグファイル内のルート要素に`include_configs`要素がありその内容を`glob`の検索マスクし、一致したものをコンフィグファイルとして認識する
    6. 上記、0～5までの引数をdeepcopyで上書きしたものが起動パラメータとして使用される。
    7. 上書きの順番は`cfg_priority`で決定される
    """
    # ========================================================================
    #
    # CONST
    #
    # ========================================================================

    __ID_CLASS = "390022f8e4eb4f1faf2c4cb523bb9d96"
    """cmd_appクラス識別用ID"""

    __CFG_ROOT_ELEMENT = "cfg_4198bbb9c3f548e5b0ba067102eee93e"
    """コンフィグルート要素名"""

    __CFG_INC_ELEMENT  = "include_configs"
    """関節include名"""

    RE_PATTERN_PARAM = "^-(?P<key>[a-z][0-9a-z_]*):(?P<value>.*)$"
    """起動引数名の正規表現パターン"""

    # ========================================================================
    # VARIABLES / COMMON
    # ========================================================================

    app_id: str = ""
    """アプリケーション固有ID"""
    evar:dict
    """起動時の環境変数"""
    startup_params: list[str]
    """起動引数"""
    startup_method:str = "main"

    # ========================================================================
    # VARIABLES / CONFIG
    # ========================================================================

    cfg_priority:dict={
        "startup_params"         : 10,
        "startup_params_cfg"     : 100,
        "startup_params_cfg_inc" : 500,
        "py_exe_cfg"             : 1000,
        "py_exe_cfg_inc"         : 5000,
        "def_cfg_inc"            : 6000,
        "def_cfg_inc_inc"        : 7000,
        "py_sub_cfg"             : 10000,
        "py_sub_cfg_inc"         : 50000,
        "env_cfg"                : 100000,
        "env_cfg_inc"            : 500000,
        "def_cfg"                : 999999,
    }
    """コンフィグパラメータの優先度を指定します。
    
    数字の大きいものは小さいもので上書きされます。
    """

    default_config:dict={}
    """アプリケーションのデフォルト設定
    
    継承先のクラスの`__init__`にてセットしてください
    """

    cfg:dict=dict()
    """アプリケーション動作設定(マージ後)"""
    cfgs:dict=dict()
    """アプリケーション動作設定(全設定)"""

    # ========================================================================
    # VARIABLES / PATH
    # ========================================================================

    path_py_file:str
    """起動元の.pyファイルパス"""
    name_py_file:str
    """起動元の.pyファイル名"""
    label_py_file:str
    """起動元の.pyファイルラベル"""
    path_py_dir:str
    """実行ディレクトリパス"""
    path_sub_dir:str
    """自己ディレクトリパス"""
    path_sub_cfg_dir:str
    """自己ディレクトリコンフィグパス"""

    # ========================================================================
    # METHOD
    # ========================================================================
    def __init__(s, id: str, argv=None) -> None:
        """コマンドアプリを生成します。

        Parameters
        ----------
        id : str
            アプリケーション固有ID(アプリケーション毎にUUIDを設定してください。)
        argv : list[str] or None
            起動引数を渡します。
            Noneの場合はsys.argvから取得するため、デバッグ時に任意の引数を渡したいときのみ使用してください。
        """
        if a.is_supposed_debug:
            a.log_setup(id)
        a.set_log_id(id)

        SP = a.SEP_DIR2FILE

        s.app_id         = id

        a.log_debug("")
        a.log_debug("## 環境変数")
        s.evar          = a.environ_variables()
        for k,v in s.evar.items():
            a.log_debug(f"{k}:{v}")

        a.log_debug("")
        a.log_debug("## 基本パス")
        s.path_py_file     = a.caller_file_name()
        s.path_py_dir      = a.cnv_abs_dir_path(s.path_py_file)
        s.name_py_file     = a.cnv_file_name(s.path_py_file)
        s.label_py_file    = a.cnv_file_name_none_ext(s.name_py_file)
        s.path_sub_dir     = f"{s.path_py_dir}{SP}{s.label_py_file}"
        s.path_sub_cfg_dir = f"{s.path_sub_dir}{SP}config"
        a.log_debug(f"起動元.py : ファイルパス       : {s.path_py_file}")
        a.log_debug(f"起動元.py : ファイル名         : {s.name_py_file}")
        a.log_debug(f"起動元.py : ファイルラベル     : {s.label_py_file}")
        a.log_debug(f"実行ディレクトリパス           : {s.path_py_dir}")
        a.log_debug(f"自己ディレクトリパス           : {s.path_sub_dir}")
        a.log_debug(f"自己ディレクトリコンフィグパス : {s.path_sub_cfg_dir}")

        a.log_debug("")
        a.log_debug("## 起動引数")
        if argv == None:
            s.startup_params = a.deep_copy(a.startup_params())
        else:
            s.startup_params = argv
        s.startup_params.pop(0)

        for v in s.startup_params:
            a.log_debug(v)

        a.set_log_id()

    def start(s):
        """アプリケーションを開始します。"""
        a.set_log_id(s.app_id)

        a.log_debug("")
        a.log_debug("## コンフィグ読み出し")
        s.__load_cfg_sequence()

        a.log_debug("")
        a.log_debug("## コンフィグの結合")
        s.__marge_cfg()

        a.log_debug("")
        a.log_debug("## main関数起動")
        s.main()

        a.log_debug("")
        a.log_debug("## main関数終了")
        a.set_log_id()
    
    def main(s):
        """メイン関数
        """
        a.log_error("main関数をオーバーライドしてください。")

    # ========================================================================
    # 非公開関数
    # ========================================================================

    # ------------------------------------------------------------------------
    # ANALYZE STARTUP PARAMS
    # ------------------------------------------------------------------------
    def __analyze_params(s)->tuple[dict,list]:
        res_params = dict()
        res_files  = list()
        prms = s.startup_params
        pat  = s.RE_PATTERN_PARAM
        cmp = a.re_compile(pat)
        for prm in prms:
            mat = cmp.match(prm)
            if mat:
                k = a.re_group(mat,"key")
                v = a.re_group(mat,"value")
                a.log_debug(f"{prm}はコンフィグとして認識します。({k}:{v})")
                res_params[k]=v
            else:
                a.log_debug(f"{prm}はファイルパスとして認識します。")
                if a.is_exist(prm):
                    if a.is_file(prm):
                        res_files.append(prm)
                    else:
                        a.log_warning(f"{prm}はファイルではありません。")
                else:
                    a.log_warning(f"{prm}は存在しないファイルです。")
        return res_params, res_files
    # ------------------------------------------------------------------------
    # LOAD CFG
    # ------------------------------------------------------------------------
    def __load_cfg_sequence(s):
        a.log_debug("")
        a.log_debug("### デフォルトコンフィグ読み出し")
        s.__load_default_cfg()
        a.log_debug("")
        a.log_debug("### 起動引数からのコンフィグ読み出し")
        s.__load_params_cfg()
        a.log_debug("")
        a.log_debug("### 実行ディレクトリからコンフィグ読み出し")
        s.__load_exe_cfg()
        a.log_debug("")
        a.log_debug("### 自己ディレクトリからコンフィグ読み出し")
        s.__load_sub_cfg()
        a.log_debug("")
        a.log_debug("### 環境変数の指定ディレクトリからコンフィグ読み出し")
        s.__load_env_cfg()
    def __load_default_cfg(s):
        """デフォルトコンフィグ読み出し"""
        def_cfg:list = s.cfgs.get("def_cfg",[])
        s.cfgs["def_cfg"] = def_cfg
        def_cfg.append(a.deep_copy(s.default_config))
        a.log_debug("#### デフォルトコンフィグのパスからコンフィグ読み出し")
        for cfg in def_cfg:
            s.__load_cfgs(cfg.get(s.__CFG_INC_ELEMENT,[]),"def_cfg_inc","def_cfg_inc_inc")
        return
    def __load_params_cfg(s):
        """起動引数コンフィグ読み出し"""

        a.log_debug("")
        a.log_debug("#### 起動引数解析")
        cfg_startup_params, cfg_files = s.__analyze_params()

        a.log_debug("")
        a.log_debug("#### 起動引数をコンフィグ値に変換")
        cfg:list = s.cfgs.get("startup_params",[])
        s.cfgs["startup_params"] = cfg
        cfg.append(cfg_startup_params)

        a.log_debug("")
        a.log_debug("#### 起動引数のパスからコンフィグ読み出し")
        s.__load_cfgs(cfg_files,"startup_params_cfg","startup_params_cfg_inc")
        return
    def __load_exe_cfg(s):
        """実行ディレクトリコンフィグ読み出し"""
        SP = a.SEP_DIR2FILE
        patterns = [
            f"{s.path_py_dir}{SP}{s.label_py_file}.yml",
            f"{s.path_py_dir}{SP}{s.label_py_file}.json"
        ]
        files = [ ptn for ptn in patterns if a.is_exist(ptn) ]
        s.__load_cfgs(files,"py_exe_cfg","py_exe_cfg_inc")
        return
    def __load_sub_cfg(s):
        """自己ディレクトリコンフィグ読み出し"""
        SP = a.SEP_DIR2FILE
        s.__load_cfgs_masks([f"{s.path_sub_cfg_dir}{SP}**{SP}*.*"],"py_sub_cfg","py_sub_cfg_inc")
        return
    def __load_env_cfg(s):
        """環境変数コンフィグ読み出し"""
        evar_name = "clt_" + s.app_id
        dir_path_list = a.environ_variable(evar_name,"")
        if dir_path_list == "":
            a.log_info(f"環境変数({evar_name})はありません。")
        else:
            s.__load_cfgs_masks(dir_path_list.split(a.SEP_PATH2PATH),"env_cfg","env_cfg_inc")
    def __load_cfgs_masks(s,path_list:list[str],cfg_priority:str,inc_priority:str = ""):
        """マスクで指定したコンフィグを読み出す"""
        files = sorted(a.get_file_list(path_list))
        s.__load_cfgs(files,cfg_priority,inc_priority)
        return
    def __load_cfgs(s,path_list:list[str],cfg_priority:str,inc_priority:str = ""):
        """複数のコンフィグを読み出す"""
        for path in path_list:
            s.__load_cfg(path,cfg_priority,inc_priority)
        return
    def __load_cfg(s,path:str,cfg_priority:str,inc_priority:str):
        """指定された単一のコンフィグを読み出す"""
        if a.is_exist(path):
            if a.is_file(path):
                try:
                    tmp:dict = a.load_yaml(path)
                    if isinstance(tmp,dict):
                        if not(s.__CFG_ROOT_ELEMENT in tmp.keys()):
                            a.log_warning(f"{path}のルート要素として{s.__CFG_ROOT_ELEMENT}が存在しません。")
                        else:
                            root:dict = tmp[s.__CFG_ROOT_ELEMENT]
                            if isinstance(root,dict):
                                if s.__CFG_INC_ELEMENT in root.keys():
                                    incs = root[s.__CFG_INC_ELEMENT]
                                    if isinstance(incs,list):
                                        cfgs:list = s.cfgs.get(cfg_priority,[])
                                        s.cfgs[cfg_priority]=cfgs
                                        cfgs.append(root)
                                        a.log_info(f"{path}のコンフィグ内容を{cfg_priority}に追加しました")
                                        if inc_priority == "":
                                            if len(incs)>0:
                                                a.log_warning(f"{path}のルート({s.__CFG_ROOT_ELEMENT})要素内にある{s.__CFG_INC_ELEMENT}にパスが指定されていますがネスト構造にはできません。無視します。")
                                        else:
                                            s.__load_cfgs_masks(incs,inc_priority)
                                    else:
                                        a.log_warning(f"{path}のルート({s.__CFG_ROOT_ELEMENT})要素内にある{s.__CFG_INC_ELEMENT}がlist型ではありません。")

                                else:
                                    a.log_warning(f"{path}のルート({s.__CFG_ROOT_ELEMENT})要素内に{s.__CFG_INC_ELEMENT}要素がありません。")
                                    
                            else:
                                a.log_warning(f"{path}のルート({s.__CFG_ROOT_ELEMENT})要素がdict型ではありません。")
                    else:
                        a.log_warning(f"{path}にルート({s.__CFG_ROOT_ELEMENT})要素がありません。")
                except Exception as e:
                    a.log_warning(f"{path}はYAMLとしての読み出しに失敗しました。")
                    a.log_warning(e)
            else:
                a.log_warning(f"{path}はファイルではありません。")
        else:
            a.log_warning(f"{path}は存在しないファイルです。")

        return
    # ------------------------------------------------------------------------
    # MARGE CFG
    # ------------------------------------------------------------------------
    def __marge_cfg(s):
        res = list()
        for k,v in s.cfg_priority.items():
            res.append( {"priority":v, "value":k})
        res = sorted(res, key=lambda x: x["priority"])
        for item in res:
            key = item["value"]
            cfgs = s.cfgs.get(key,[])
            for c in cfgs:
                s.cfg = a.deep_update(s.cfg,c)
