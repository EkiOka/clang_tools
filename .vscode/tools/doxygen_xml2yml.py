from lib import lib


def __cnv_root(files:list):
    res = dict()
    for f in files:
        dat = lib.xml.load(f)

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
