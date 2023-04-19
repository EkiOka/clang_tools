"""doxygenのymlファイルを解析した結果を生成
"""

#####################################################################
# import
#####################################################################

from lib import lib

#####################################################################
# 内部関数定義
#####################################################################


def __func(params:dict):
    """シェル起動基点

    Parameters
    ----------
    params : dict
        起動引数
    """
    src_path = params["src_path"]
    cfg_path = params["cfg_path"]
    dest_path = params["dest_path"]
    src = lib.yaml.load(src_path)
    cfg = lib.yaml.load(cfg_path)
    dest = __chk(src,cfg)
    lib.yaml.save(dest_path,dest)


def __chk(src:dict, cfg:dict):
    res = dict()
    compounddef = src["compounddef"]
    res.update( __chk_compounddef(compounddef,cfg) )
    return res

def __chk_compounddef(src_compounddef, cfg:dict):
    res = dict()

    for compounddef in src_compounddef:
        compoundname = compounddef["compoundname"]

    return res


#####################################################################
# シェル起動
#####################################################################

__args_cfg={
    "script":{"type":"text"},
    "src_path":{"type":"text"},
    "cfg_path":{"type":"text"},
    "dest_path":{"type":"text"}
}

lib.cmd_app.start(
    __name__,
    __func,
    __args_cfg
    )
