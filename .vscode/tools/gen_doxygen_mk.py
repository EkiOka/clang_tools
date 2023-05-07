
#####################################################################
# import
#####################################################################

import os
import sys
from lib import lib

#####################################################################
# 関数起動
#####################################################################

def gen(src_path:str, tmp_path:str, dest_path:str):
    lib.log.enable()

    src_data = lib.yaml.load(src_path)
    lib.log.debug(f"src_data={src_data}")
    dst_data = __cnv(src_data)
    lib.log.debug(f"dst_data={dst_data}")
    dst_text = lib.jinja2.convert(dst_data,tmp_path)
    lib.log.debug(f"dst_text={dst_text}")
    lib.text.save(dest_path,dst_text)

def __cnv(src_data):
    res = dict()
    dest_files=list()
    res["files"] = dest_files

    xml_files = src_data

    for xml_file in xml_files:
        dir = os.path.dirname(xml_file)
        name = os.path.splitext(os.path.basename(xml_file))[0]
        parent_dir = lib.get_parent_dir(dir)
        yml_file = parent_dir + "\\yml\\" + name + ".yml"
        lib.log.debug(f"{xml_file}=>{yml_file}")
        item = dict()
        item["xml"]=xml_file
        item["yml"]=yml_file
        dest_files.append(item)
    return res

#####################################################################
# シェル起動
#####################################################################

def __main(params:dict):
    """本スクリプトがシェルから呼び出された際のファイル処理を記載
    """
    src_path = params["src_path"]
    dest_path = params["dest_path"]
    tmp_path = params["tmp_path"]
    gen(src_path,tmp_path,dest_path)
    return

__args_cfg={
    "script":{"type":"text"},
    "src_path":{"type":"text"},
    "tmp_path":{"type":"text"},
    "dest_path":{"type":"text"}
}


lib.cmd_app.start(
    __name__,
    __main,
    __args_cfg
    )