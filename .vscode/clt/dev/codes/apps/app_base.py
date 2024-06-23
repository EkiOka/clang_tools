"""アプリケーション基礎クラス開発環境
"""

# $code_start(id=cf01a64851664ffdb8c55101b541e83f,type=singleton_lines)
import enum
import sys
import os
import yaml

# $code_end(id=cf01a64851664ffdb8c55101b541e83f)
# $code_start(id=67bb2db60f664911aa8463a560f5802a,type=singleton_lines)
SEP_D2F = "\\"  # パス内のディレクトリ、ファイルの区切り文字列
SEP_P2P = ";"  # パスとパスを区切る文字列
Any = object  # 型指定をしない場合の型
SEP_EXT = "."
DEF_ENC = "utf-8"
R = "r"
W = "w"
# $code_end(id=67bb2db60f664911aa8463a560f5802a)

# $code_params(id=afa85816584641f29a9cd8b3cae4dfdf,name=depend,value=cf01a64851664ffdb8c55101b541e83f)
# $code_start(id=afa85816584641f29a9cd8b3cae4dfdf,type=singleton_lines)
EXE_DIR = os.path.dirname(__file__)
EXE_FILE_NAME = os.path.basename(__file__)
EXE_FILE_EXT = EXE_FILE_NAME.split(SEP_EXT)[-1:]
EXE_FILE_LEBAL = SEP_EXT.join(EXE_FILE_NAME.split(SEP_EXT)[0:-1])
CD = os.getcwd()
# $code_end(id=afa85816584641f29a9cd8b3cae4dfdf)

# $code_params(id=b76ca5a1d6c14e76a7e1352b4b033b76,name=depend,value=afa85816584641f29a9cd8b3cae4dfdf)
# $code_params(id=b76ca5a1d6c14e76a7e1352b4b033b76,name=depend,value=cf01a64851664ffdb8c55101b541e83f)
# $code_params(id=b76ca5a1d6c14e76a7e1352b4b033b76,name=depend,value=67bb2db60f664911aa8463a560f5802a)
# $code_start(id=b76ca5a1d6c14e76a7e1352b4b033b76,type=unique_area)
PRM_NAME_CFG_FILE = "cfg"
"""コンフィグファイルパスを指示する起動引数名"""
PRM_DEF_CFG_FILE_NAME = EXE_FILE_LEBAL + ".yml"
"""デフォルトコンフィグ：コンフィグファイル名"""
ERR_MSG_57DD103A3B5D46FAAE2088B3754C3EA3 = (
    "未対応のコンフィグデータソースが指定されました"
)


class application_config_base:
    """アプリケーションコンフィグ設定基礎クラス"""

    class cfg_pri(enum.IntEnum):
        """コンフィグ優先度"""

        START_PARAM = enum.auto()
        """起動引数→コンフィグ"""
        START_PARAM_CFG = enum.auto()
        """起動引数の指定ファイル→コンフィグ"""
        START_PY_CUR_CFG = enum.auto()
        """起動アプリ同一ディレクトリ→コンフィグ"""
        START_PY_DIR_CFG = enum.auto()
        """起動アプリ名(.pyを除く)ディレクトリ→コンフィグ"""
        ENV_DIR_CFG = enum.auto()
        """環境変数指定ディレクトリ→コンフィグ"""

    __cfg: dict = dict()
    """コンフィグデータ"""

    startup_params: list[str] = None
    """起動引数
    
    デバッグ用のダミー引数を渡したい場合は上書きしてください。

    起動引数の形式は「名称:値」「名称」のみのサポートとします。
    名称は英数と"_"のみ使用可能とします。
    英数は内部ではすべて小文字として扱います。

    """

    cfg_priority_list: list[cfg_pri]
    """コンフィグ設定値読み出し優先度設定"""

    startup_param_cfg_file_path: str = PRM_DEF_CFG_FILE_NAME
    """引数で指定されたコンフィグファイルのパス"""

    def __init__(self) -> None:
        s = self
        p = application_config_base.cfg_pri
        s.cfg_priority_list = [
            p.START_PARAM,
            p.START_PARAM_CFG,
            p.START_PY_CUR_CFG,
            p.START_PY_DIR_CFG,
            p.ENV_DIR_CFG,
        ]

    def __analyze_startup_params(self) -> dict:
        """起動引数を分析する

        Returns:
            dict: 分析結果
        """
        s = self
        cfg = s.__cfg

        # 未設定の場合(デバッグ用の値がセットされていない場合)は
        # sys.argvの値を使用する
        if s.startup_params is None:
            s.startup_params = [str(a) for a in sys.argv]

        res = dict()

        params = s.startup_params[1:]
        for p in params:
            value_list = p.split(":")
            name = ""
            value = ""
            value_list_len = len(value_list)
            if value_list_len == 0:
                pass
            elif value_list_len == 1:
                name = p.lower()
                value = True
            elif value_list_len >= 2:
                name = value_list[0].lower()
                value = ":".join(value_list[1:])
            res[name] = value

        cfg[application_config_base.cfg_pri.START_PARAM] = res
        cfg_path = res.get(PRM_NAME_CFG_FILE, "")
        s.startup_param_cfg_file_path = cfg_path
        return res

    def __load_cfg(self, src: cfg_pri) -> dict:
        res = dict()
        match src:
            case application_config_base.cfg_pri.START_PARAM:
                res = self.__analyze_startup_params()
            case application_config_base.cfg_pri.START_PARAM_CFG:
                if os.path.exists(self.startup_param_cfg_file_path):
                    res = self.__load_yaml(self.startup_param_cfg_file_path)
            case application_config_base.cfg_pri.START_PY_CUR_CFG:
                # TODO 実装必要
                pass
            case application_config_base.cfg_pri.START_PY_DIR_CFG:
                # TODO 実装必要
                pass
            case application_config_base.cfg_pri.ENV_DIR_CFG:
                # TODO 実装必要
                pass
            case _:
                raise Exception(
                    f"{ERR_MSG_57DD103A3B5D46FAAE2088B3754C3EA3}(src={src})"
                )

        return res

    def __load_yaml(self, path: str, encoding: str = DEF_ENC) -> Any:
        """YAMLファイルの読み出し

        Args:
            path (str): 読み出し対象のファイルパス
            encoding (str, optional): 読み出し対象のファイルのエンコード. Defaults to DEF_ENC.

        Returns:
            Any: 読み出し結果
        """
        res = None
        with open(path, mode=R, encoding=encoding) as f:
            res = yaml.safe_load(f)
        return res

    def get(
        self, name: str, default_value: object = None, get_list: list[cfg_pri] = None
    ) -> Any:
        """設定値を取得する

        Args:
            name (str):
                取得する設定項目名。
            default_value (object, optional):
                設定値が存在しない場合に返す値。
                初期値はNoneです。
            get_list (list[cfg_pri], optional):
                設定値を取得するデータベースの優先順位。
                Noneを指定した場合はcfg_priority_listの値を使用します。
                初期値はNoneです。

        Returns:
            Any: 設定値
        """
        res = None
        cfg: dict = self.__cfg

        if get_list is None:
            get_list = self.cfg_priority_list

        for src in get_list:

            cfg_src: dict = cfg.get(src, None)

            # 設定値なければ読み込みなおす(1回のみ)
            if cfg_src is None:
                cfg_src = self.__load_cfg(src)

            if isinstance(cfg_src, dict):
                res = cfg_src.get(name, None)
                if not (res is None):
                    break

        if res is None:
            res = default_value

        return res


class application_base:
    """アプリケーション基礎クラス"""

    def __init__(self) -> None:
        """アプリケーション基礎クラスを生成します"""
        return

    def load_yaml(self, path: str, encoding: str = DEF_ENC) -> Any:
        """YAMLファイルの読み出し

        Args:
            path (str): 読み出し対象のファイルパス
            encoding (str, optional): 読み出し対象のファイルのエンコード. Defaults to DEF_ENC.

        Returns:
            Any: 読み出し結果
        """
        res = None
        with open(path, mode=R, encoding=encoding) as f:
            res = yaml.safe_load(f)
        return res

    def save_yaml(self, path: str, data: Any, encoding=DEF_ENC):
        """YAMLファイルの保存

        Args:
            path (str): 保存先のファイルパス
            data (Any): 保存するデータ
            encoding (str, optional): 保存するファイルのエンコード. Defaults to DEF_ENC.
        """
        with open(path, mode=W, encoding=encoding) as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

    def load_text_lines(self, path: str, encoding=DEF_ENC) -> list[str]:
        lines = []
        if os.path.exists(path):
            with open(path, R, encoding=encoding) as file:
                lines = [
                    line.replace("\n", "").replace("\r", "")
                    for line in file.readlines()
                ]
        return lines

    def save_text_lines(
        self, path: str, lines: list[str], ret_code: str = "\n", encoding=DEF_ENC
    ):
        with open(path, W, encoding=encoding) as file:
            file.writelines([line + ret_code for line in lines])
        return

    def run(self):
        """アプリケーションの動作を実行します

        メソッドをオーバーライドして使用してください。
        """
        return


# $code_end(id=b76ca5a1d6c14e76a7e1352b4b033b76)

# ---------------------------------------------------------------------------
# test code
# ---------------------------------------------------------------------------


class test_app(application_base):

    config: application_config_base

    def __init__(self) -> None:
        self.config = application_config_base()
        cfg = self.config
        super().__init__()
        self.config.startup_params = [__file__, "aaa:cc"]
        print(cfg.get("aaa", "bb"))
        return

    def run(self):
        print("test_run")
        return


app = test_app()
app.run()
