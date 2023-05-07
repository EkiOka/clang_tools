
#####################################################################
# import
#####################################################################

import sys
from lib import lib

def __main(params:dict):
    enable_masks  = params["enable_masks"]
    disable_masks = params["disable_masks"]
    dest_path     = params["dest"]
    
    dest = lib.glob.glob_dis(enable_masks,disable_masks)
    lib.json.save(path=dest_path,data=dest,no_updated_file_over_write=False)
    return


#####################################################################
# シェル起動
#####################################################################

__args_cfg={
    "script":{"type":"text"},
    "enable_masks":{
        "type":"list",
        "separator":";"
        },
    "disable_masks":{
        "type":"list",
        "separator":";"
        },
    "dest":{"type":"text"}
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
        )
