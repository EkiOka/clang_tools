"""doxygenのmarge ymlファイルを解析しやすい形式に変換
"""

from lib import lib

def __cnv(src:dict)->dict:
    res = {}

    return res


def __func(params:dict):
    src_path = params["src_path"]
    dest_path = params["dest_path"]
    src = lib.yaml.load(src_path)
    dest = __cnv(src)
    lib.yaml.save(dest_path,dest)

__args_cfg={
    "script":{"type":"text"},
    "src_path":{"type":"text"},
    "dest_path":{"type":"text"}
}

lib.cmd_app.start(
    __name__,
    __func,
    __args_cfg
    )
