"""doxygenのmarge ymlファイルを解析しやすい形式に変換
"""

#####################################################################
# import
#####################################################################

import sys
from lib import lib

#####################################################################
# 内部関数定義
#####################################################################

def __main(params:dict):

    lib.log.enable()

    src_path = params["src_path"]
    dest_path = params["dest_path"]

    lib.log.debug(f"src_path={src_path}")
    lib.log.debug(f"dest_path={dest_path}")

    yml_data = lib.yaml.load(src_path)
    rpt_data = cnv(yml_data)
    lib.yaml.save(dest_path,rpt_data)

    return

def cnv(doxygen_yml:dict)->dict:
    res = dict()


    return res

#####################################################################
# シェル起動
#####################################################################

__args_cfg={
    "script":{"type":"text"},
    "src_path":{"type":"text"},
    "dest_path":{"type":"text"}
}

if "debugpy" not in sys.modules:
    lib.cmd_app.start(
        __name__,
        __main,
        __args_cfg
        )
else:
    lib.cmd_app.start(
        __name__,
        __main,
        __args_cfg,
        [__file__,
         '-src_path:Z01_out\\doxygen\\result\\result.yml',
         '-dest_path:Z01_out\\doxygen\\result\\doxygen.rpt']
        )
