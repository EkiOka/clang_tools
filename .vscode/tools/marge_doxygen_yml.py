
#####################################################################
# import
#####################################################################

from lib import lib

#####################################################################
# 関数起動
#####################################################################


def marge_files(src_mask:str, dest_path:str):

    dest_data = dict()
    dest_root = dict()
    dest_data["doxygen"]=dest_root
    files = lib.glob.glob(src_mask)
    for file in files:
        src_data = lib.yaml.load(file)
        lib.log.debug(f"file={file}")
        lib.log.debug(f"src_data={src_data}")
        dest_root.update(src_data)

    lib.yaml.save(dest_path, dest_data)
    return


#####################################################################
# シェル起動
#####################################################################

def __main(params:dict):
    """本スクリプトがシェルから呼び出された際のファイル処理を記載
    """
    src_mask = params["src_mask"]
    dest_path = params["dest_path"]
    marge_files(src_mask,dest_path)
    return

__args_cfg={
    "script":{"type":"text"},
    "src_mask":{"type":"text"},
    "dest_path":{"type":"text"}
}


lib.cmd_app.start(
    __name__,
    __main,
    __args_cfg
    )