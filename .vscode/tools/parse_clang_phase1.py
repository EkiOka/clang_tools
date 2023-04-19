"""フェーズ(1)
from X3010:2003(ISO/IEC9899:1999)
5.1.1.2 翻訳フェーズ

以下引用

> （1） 必要ならば，物理的なソースファイルの多バイト文字を，
> 対応するソース文字集合に，処理系定義の方法で，写像する
> （この際，行の終わりを示すものに対して改行文字を導入する。）。
> 3文字表記を，対応する単一の文字の内部表現に置き換える。

写像までは終わっている前提なので3文字表記のみ置き換える

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

    dest = __cnv_phase1(src)

    lib.yaml.save(dest_path,dest)

def __cnv_phase1(src:list)->list:
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

        res.append(dst)
        cur_index = cur_index + 1

    return res

def __match(src:list, start_index:int, text:str, dest:dict)->bool:
    count = len(src)
    cur_index = start_index
    text_len = len(text)
    cur_txt = src[cur_index][sign.txt]
    cur_txt_len = len(cur_txt)
    res = False
    match_list = list()
    dest["match_list"]=match_list
    dest["start_index"]=start_index
    dest["end_index"]=cur_index

    while( ( cur_txt_len <= text_len ) and ( cur_index < count ) ):
        parts_text = text[0:cur_txt_len]
        print(parts_text)
        if text == cur_txt:
            match_list.append(src[cur_index])
            dest["end_index"]=cur_index
            res = True
        elif parts_text == cur_txt:
            match_list.append(src[cur_index])
            dest["end_index"]=cur_index
            cur_index   = cur_index + 1
            cur_txt     = cur_txt + src[cur_index][sign.txt]
            cur_txt_len = len(cur_txt)
        else: # parts_text != cur_txt
            match_list.clear()
            break

    return res

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
