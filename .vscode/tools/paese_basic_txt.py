"""txtをymlに変換
"""

#####################################################################
# import
#####################################################################

from lib import lib
from sign import sign
from sign import basic_text_sign as bts

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

    src = lib.yaml.load(src_path)

    dest_phase1 = __cnv_phase1(src)
    dest_phase2 = __cnv_phase2(dest_phase1)
    dest        = __cnv_phase3(dest_phase2)

    lib.yaml.save(dest_path,dest)

def __cnv_phase1(src:list)->list:
    res = list()

    for s in src:
        d = dict()
        d.update(s)
        txt = d[sign.txt]
        if txt in bts.alphabet_lowercase:
            d[sign.type]=bts.alphabet_lowercase_name
        elif txt in bts.alphabet_uppercase:
            d[sign.type]=bts.alphabet_uppercase_name
        elif txt in bts.number:
            d[sign.type]=bts.number_name
        elif txt in bts.space:
            d[sign.type]=bts.space_name
        elif txt in bts.mark:
            d[sign.type]=bts.mark_name
        elif txt in bts.control_code:
            d[sign.type]=bts.control_code_name
        else:
            d[sign.type]=bts.unknown_name
        res.append(d)

    return res

def __cnv_phase2(src:list)->list:
    res = list()

    count = len(src)
    cur_index = 0
    # 改行、タブは置き換える
    while(cur_index<count):
        s = src[cur_index]
        dst = dict()
        dst.update(s)
        txt = dst[sign.txt]
        typ = dst[sign.type]
        if typ == bts.control_code_name:
            if txt in bts.tab:
                dst[sign.type] = bts.tab_name
            elif txt in bts.new_line:
                dst[sign.type] = bts.new_line_name

        res.append(dst)
        cur_index = cur_index + 1

    return res

def __cnv_phase3(src:list)->list:
    res = list()


    count = len(src)
    cur_index = 0
    while(cur_index<count):
        s = src[cur_index]
        dst = dict()
        dst.update(s)
        
        cur_name = s.get(sign.type,bts.unknown_name)
        if cur_name == bts.mark_name:
            cur_index = cur_index + 1
            res.append(dst)
        else:
            # 最初の要素は即追加
            cur_index = cur_index + 1
            res.append(dst)
            cur_index = __marge_chars(src,dst,cur_index)
    
    return res

def __marge_chars(src:list,dst:dict,start_index:int):
    dst_name = dst.get(sign.type,bts.unknown_name)
    index = start_index
    count = len(src)
    while(index<count):
        s = src[index]
        cur_name = s.get(sign.type,bts.unknown_name)
        if dst_name == cur_name:
            dst[sign.txt]        = dst[sign.txt] + s.get(sign.txt,"")
            dst[sign.end_column] = s.get(sign.end_column ,0)
            dst[sign.end_line]   = s.get(sign.end_line   ,0)
            index = index + 1
        else:
            break
    return index

#####################################################################
# シェル起動
#####################################################################

__args_cfg={
    sign.script:sign.args_type_txt,
    sign.src_path:sign.args_type_txt,
    sign.dest_path:sign.args_type_txt
}

lib.cmd_app.start(
    __name__,
    __func,
    __args_cfg
    )
