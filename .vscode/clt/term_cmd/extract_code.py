"""アプリケーション基礎クラス開発環境
"""

# $inc_start(id=cf01a64851664ffdb8c55101b541e83f)
import enum
import sys
import os
import yaml

# $inc_end(id=cf01a64851664ffdb8c55101b541e83f)

# $inc_start(id=67bb2db60f664911aa8463a560f5802a)
SEP_D2F = "\\"  # パス内のディレクトリ、ファイルの区切り文字列
SEP_P2P = ";"  # パスとパスを区切る文字列
Any = object  # 型指定をしない場合の型
SEP_EXT = "."
DEF_ENC = "utf-8"
R = "r"
W = "w"
STR_EMPTY = ""
LIST_EMPTY = []
CR = "\r"  # Carriage Return
LF = "\n"  # Line Feed
CRLF = "\r\n"  # Carriage Return and Line Feed
COLON = ":"
# $inc_end(id=67bb2db60f664911aa8463a560f5802a)

# $inc_start(id=afa85816584641f29a9cd8b3cae4dfdf)
EXE_DIR = os.path.dirname(__file__)
EXE_FILE_NAME = os.path.basename(__file__)
EXE_FILE_EXT = EXE_FILE_NAME.split(SEP_EXT)[-1:]
EXE_FILE_LEBAL = SEP_EXT.join(EXE_FILE_NAME.split(SEP_EXT)[0:-1])
SD = os.getcwd()  # Startup current Directory
# $inc_end(id=afa85816584641f29a9cd8b3cae4dfdf)

# $inc_start(id=b76ca5a1d6c14e76a7e1352b4b033b76)
START_PRM_SEP = COLON
"""起動引数の引数名と値の区切り文字"""
START_PRM_NAME_CFG_FILE = "cfg"
"""コンフィグファイルパスを指示する起動引数名"""
START_PRM_DEF_CFG_FILE = EXE_FILE_LEBAL + ".yml"
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

    startup_param_cfg_file_path: str = START_PRM_DEF_CFG_FILE
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
            value_list = p.split(START_PRM_SEP)
            name = STR_EMPTY
            value = STR_EMPTY
            value_list_len = len(value_list)
            if value_list_len == 0:
                pass
            elif value_list_len == 1:
                name = p.lower()
                value = True
            elif value_list_len >= 2:
                name = value_list[0].lower()
                value = START_PRM_SEP.join(value_list[1:])
            res[name] = value

        cfg[application_config_base.cfg_pri.START_PARAM] = res
        cfg_path = res.get(START_PRM_NAME_CFG_FILE, STR_EMPTY)
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

    def _get_str(self, name: str) -> str:
        """通常の文字列設定値を取得します"""
        return self.get(name, APP_CFG_DEF.get(name, STR_EMPTY))

    def _get_list(self, name: str, sep=SEP_P2P) -> list[str]:
        """通常の文字列設定値を取得します"""
        str_value: str = self.get(name, APP_CFG_DEF.get(name, STR_EMPTY))
        res = str_value.split(sep)
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
                    line.replace(CR, STR_EMPTY).replace(LF, STR_EMPTY)
                    for line in file.readlines()
                ]
        return lines



    def save_text_lines(
        self, path: str, lines: list[str], ret_code: str = LF, encoding=DEF_ENC
    ):
        with open(path, W, encoding=encoding) as file:
            file.writelines([line + ret_code for line in lines])
        return


    def run(self):
        """アプリケーションの動作を実行します

        メソッドをオーバーライドして使用してください。
        """
        return


# $inc_end(id=b76ca5a1d6c14e76a7e1352b4b033b76)

# ---------------------------------------------------------------------------
# contents
# ---------------------------------------------------------------------------
import glob
import re

ERR_MSG_6AFEADB1CA94487D9504EBB88FBED2D4 = "未定義の機能が呼ばれました。"
AREA_PARAM_LIST_NAMES = ["depend"]
APP_CFG_DEF = {
    "lang": "py",
    "pattern": "^[\\t ]*#[\\t ]+\\$(?P<func>[a-zA-Z][a-zA-Z_]*)\\((?P<params>.*)\\).*$",
    "mask": "*/**/*.py",
    "enc": DEF_ENC,
    "dst": EXE_FILE_LEBAL + "_output.yml",
}


class func_type(enum.StrEnum):
    CODE_PARAMS = "code_params"
    CODE_START = "code_start"
    CODE_END = "code_end"
    INC_PARAMS = "inc_params"
    INC_START = "inc_start"
    INC_END = "inc_end"


class configration(application_config_base):

    @property
    def ptn(self) -> str:
        return self._get_str("pattern")

    @property
    def masks(self) -> list[str]:
        """入力元のファイルマスクリスト"""
        return self._get_list("mask", SEP_P2P)

    @property
    def enc(self) -> str:
        return self._get_str("enc")

    @property
    def dst(self) -> str:
        return self._get_str("dst")


class application(application_base):

    config: configration

    def __init__(self) -> None:
        """アプリケーションクラスを生成します"""
        self.config = configration()
        super().__init__()
        return

    def run(self):

        s = self
        cfg = s.config
        masks = cfg.masks
        enc = cfg.enc
        dst = cfg.dst
        dst_data = dict()
        for mask in masks:
            files = glob.glob(mask, recursive=True)
            for file in files:
                lines = s.load_text_lines(file, enc)
                s.extract_codes(os.path.basename(file), lines, dst_data)
        s.save_yaml(dst, dst_data, enc)
        return

    def extract_codes(self, src_file: str, src_lines: list[str], dst: dict) -> None:
        s = self
        cfg = s.config
        ptn = cfg.ptn
        cmp = re.compile(ptn)
        cur_area = []
        for line_index in range(0, len(src_lines), 1):
            line_no = line_index + 1
            line = src_lines[line_index].replace("\n", "").replace("\r", "")
            mat = cmp.match(line)
            if mat is None:
                for area_index in range(0, len(cur_area), 1):
                    area: dict = cur_area[area_index]
                    area_type = area.get("type", "unique_area")
                    area_lines: list = area.get("lines", [])
                    area["lines"] = area_lines
                    match (area_type):
                        case "unique_area":
                            area_lines.append(line)
                            pass
                        case "singleton_lines":
                            if line in area_lines:
                                pass
                            else:
                                area_lines.append(line)
                pass
            else:
                mat_dict = mat.groupdict()
                mat_func = mat_dict.get("func")
                mat_params = mat_dict.get("params")
                params = s.cnv_params(mat_params)
                param_id = params.get("id", "")
                dst_id_data: dict = dst.get(param_id, {})
                dst[param_id] = dst_id_data
                match mat_func:
                    case func_type.CODE_PARAMS:
                        s.cnv_code_param(params, dst_id_data)
                    case func_type.CODE_START:
                        param_type = params.get("type", "unique_area")
                        dst_id_data["type"] = param_type
                        if param_type == "unique_area":
                            dst_id_data["lines"] = []
                        cur_area.append(dst_id_data)
                        pass
                    case func_type.CODE_END:
                        cur_area.remove(dst_id_data)
                        pass
                    case func_type.INC_PARAMS:
                        pass
                    case func_type.INC_START:
                        pass
                    case func_type.INC_END:
                        pass
                    case _:
                        print(
                            f'{ERR_MSG_6AFEADB1CA94487D9504EBB88FBED2D4}(src_file={src_file},line_no={line_no},func="{mat_func}")'
                        )
                pass
        return None

    def cnv_code_param(self, params: dict, dst_id_data: dict) -> None:
        param_name = params.get("name", "")
        param_value = params.get("value", "")
        if param_name in AREA_PARAM_LIST_NAMES:
            cur_param_value: list = dst_id_data.get(param_name, [])
            if param_value in cur_param_value:
                pass
            else:
                cur_param_value.append(param_value)
            dst_id_data[param_name] = cur_param_value
        else:
            dst_id_data[param_name] = param_value
        return None

    def cnv_params(self, src: str) -> dict:
        res = dict()
        params = src.split(",")
        for param in params:
            param_split = param.split("=")
            name = param_split[0]
            value = "=".join(param_split[1:])
            res[name] = value
        return res


app = application()
app.run()
