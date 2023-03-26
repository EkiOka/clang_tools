from lib import lib
import os

def __cnv_child(xml):
    res = dict()
    res["tag"]=xml.tag
    res["attrib"]=xml.attrib
    res["text"]=xml.text
    res["children"]=list()
    children = res["children"]
    for child in xml:
        children.append(__cnv_child(child))
    return res

def __cnv_root(files:list):
    res = dict()
    for f in files:
        xml_root = lib.xml.load(f)
        yml_root = dict()
        res[os.path.basename(f)]= __cnv_child(xml_root)


    return res

def __func(params:dict):
    src_masks = params["src_masks"]
    dis_masks = params["dis_masks"]
    dest_path = params["dest_path"]
    files = lib.glob.glob_dis(src_masks,dis_masks)
    dest_data = __cnv_root(files)
    lib.yaml.save(dest_path,dest_data)


__args_cfg={
    "script":{"type":"text"},
    "src_masks":{
        "type":"list",
        "separator":";"
        },
    "dis_masks":{
        "type":"list",
        "separator":";"
        },
    "dest_path":{"type":"text"}
}



lib.cmd_app.start(
    __name__,
    __func,
    __args_cfg
    )
