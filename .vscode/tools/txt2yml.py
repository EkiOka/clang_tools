"""txtをymlに変換
"""

#####################################################################
# import
#####################################################################

from lib import lib
from sign import sign

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
    src_path  = params[sign.src_path]
    dest_path = params[sign.dest_path]

    src = lib.text.load(src_path)

    dest_phase1 = __cnv_phase1(src)
    dest_phase2 = __cnv_phase2(dest_phase1)
    dest        = __cnv_phase3(dest_phase2,src_path)

    lib.yaml.save(dest_path,dest)

def __cnv_phase1(src)->list:
    """単純な辞書型配列に変換
    """
    res = list()
    for cur in src:
        dst = dict()
        dst[sign.txt] = cur
        res.append(dst)
    return res

def __cnv_phase2(src)->list:
    """改行コードのCRLFをまとめる
    """
    res = list()
    pool = list()
    for cur in src:
        if cur[sign.txt] == sign.cr:
            pool.append(cur)
        elif cur[sign.txt] == sign.lf:
            pool.append(cur)
            p_txt = ""
            for p_cur in pool:
                p_txt = p_txt + p_cur[sign.txt]
            dst = dict()
            dst[sign.txt] = p_txt
            res.append(dst)
            pool = list()
        else:
            for p_cur in pool:
                res.append(p_cur)
            res.append(cur)
            pool = list()

    return res

def __cnv_phase3(src,file_name)->list:
    """テキスト座標を設定
    """
    column = 1
    line = 1
    for cur in src:
        cur[sign.file_name   ]=file_name
        cur[sign.begin_column]=column
        cur[sign.end_column  ]=column
        cur[sign.begin_line  ]=line
        cur[sign.end_line    ]=line
        if cur[sign.txt] == sign.crlf:
            cur[sign.end_column] = cur[sign.end_column] + 1
            column = 1
            line = line + 1
            pass
        elif cur[sign.txt] == sign.cr:
            column = 1
            line = line + 1
            pass
        elif cur[sign.txt] == sign.lf:
            column = 1
            line = line + 1
            pass
        else:
            column = column + 1
            pass
    return src

#####################################################################
# シェル起動
#####################################################################

__args_cfg={
    "script":{"type":"text"},
    sign.src_path:{"type":"text"},
    sign.dest_path:{"type":"text"}
}

lib.cmd_app.start(
    __name__,
    __func,
    __args_cfg
    )
