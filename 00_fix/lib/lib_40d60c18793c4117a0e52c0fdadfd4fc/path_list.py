import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a

EVAR_NAME_PATH_LIST = "path_list_path"
"""環境変数名：パスリストファイルのパス"""

EVAR_ENV_ID = "env_id"
"""環境変数名：環境ID

環境IDは本スクリプトなどを含めたvscode環境の固有IDです。
"""

SEP_ID2NAME="/"

def env_id()->str:
    """環境変数ID取得"""
    res = a.environ_variable(EVAR_ENV_ID,"")
    if res == "":
        a.raise_NotFound(
            target=EVAR_ENV_ID,
            type_name="environment variable")

    return res
def path_list_path()->str:
    """パスリストファイル(JSON)へのパスを取得"""
    a.set_log_id("f26ded7706f84825a9f9b728db7f890c")
    func = a.cur_function_name()
    res = a.environ_variable(EVAR_NAME_PATH_LIST,"")
    a.log_debug(f"{func} > res : {res}")
    if res == "":
        res = f"{a.get_cur_dir()}\\path_list.json"
    a.log_debug(f"{func} > res : {res}")
    a.set_log_id()
    return res
def load_path()->dict:
    """パスリスト読み出し"""
    a.set_log_id("60810ef5ceb5403b891a86aded162da5")
    func = a.cur_function_name()
    path = path_list_path()
    a.log_debug(f"{func} > path : {path}")
    res = None
    try:
        res = a.load_json(path)
    except:
        res = dict()
    a.log_debug(f"{func} > res : {str(res)[:30]}")
    a.set_log_id()
    return res

def save_path(path_list:dict):
    """パスリスト保存"""
    path = path_list_path()
    a.save_json(path,path_list)
def path_list(id:str)->dict:
    """個別パスリスト取得

    Parameters
    ----------
    id : str
        取得するパスリストID

    Returns
    -------
    dict
        パスリスト
    """
    a.set_log_id("8abcf5d15b2543a6866137d70e9b7fea")
    func = a.cur_function_name()
    a.log_debug(f"{func} > id : {id}")
    res = {}
    if id == None or id == "":
        a.raise_NotFound(id,"path list ID")
    else:
        path_list = load_path()
        a.log_debug(f"{func} > path_list : {str(path_list)[:30]}(...)")
        if id in path_list.keys():
            res = path_list[id]
        else:
            path_list[id]=res
            save_path(path_list)
    a.log_debug(f"{func} > res : {str(res)[0:30]}(...)")
    a.set_log_id()
    return res

def update_path(id_src:dict, id:str)->dict:
    """個別パスリスト一部更新
    """
    dest = load_path()
    dest_id = dest.get(id,{})
    dest_id.update(id_src)
    dest[id]=dest_id
    save_path(dest)

def update_evn_path(src:dict)->dict:
    """環境パスリスト更新
    """
    id = env_id()
    update_path(src,id)

def update_user_path(src:dict)->dict:
    """ユーザーパスリスト更新
    """
    id = a.user_name()
    update_path(src,id)

def env_path_list()->dict:
    """環境固有パスリスト取得"""
    a.set_log_id("df1ba740e87e435b9b855a36c9d2dcea")
    func = a.cur_function_name()
    id = env_id()
    a.log_debug(f"{func} > id : {id}")
    a.set_log_id()
    return path_list(id)

def user_path_list()->dict:
    """ユーザー固有パスリスト取得"""
    a.set_log_id("73674a518c5749e9a9c70f6a958fb3dc")
    func = a.cur_function_name()
    id = a.user_name()
    a.log_debug(f"{func} > id : {id}")
    a.set_log_id()
    return path_list(id)

def get_path(name:str):
    a.set_log_id("9b413f7b5e914c0abc5387e546900601")
    func = a.cur_function_name()
    res = ""
    split_name = name.split(SEP_ID2NAME)
    match(len(split_name)):
        case 1:
            name = split_name[0]
            lst = user_path_list()
            res = lst.get(name,"")
            a.log_debug(f"{func} > name : {name}")
            a.log_debug(f"{func} > lst : {lst}")
            a.log_debug(f"{func} > res : {res}")
            pass
        case 2:
            id = split_name[0]
            name = split_name[1]
            lst = path_list(id)
            res = lst.get(name,"")
            a.log_debug(f"{func} > id : {id}")
            a.log_debug(f"{func} > name : {name}")
            a.log_debug(f"{func} > lst : {lst}")
            a.log_debug(f"{func} > res : {res}")
            pass
        case _:
            a.raise_Exception(f"nameの値{name}が異常です。")
    a.set_log_id()
    return res

def get_user_path(name:str):
    a.set_log_id("3c3a69831d134d999c0fbf7eee70a4a0")
    func = a.cur_function_name()
    res = ""
    lst = user_path_list()
    res = lst.get(name,"")
    a.log_debug(f"{func} > name : {name}")
    a.log_debug(f"{func} > lst  : {lst}")
    a.log_debug(f"{func} > res  : {res}")
    a.set_log_id("")
    return res

def get_env_path(name:str):
    a.set_log_id("131a2ee97950459190be8bf47aba4d2c")
    func = a.cur_function_name()
    res = ""
    lst = env_path_list()
    res = lst.get(name,"")
    a.log_debug(f"{func} > name : {name}")
    a.log_debug(f"{func} > lst  : {lst}")
    a.log_debug(f"{func} > res  : {res}")
    a.set_log_id()
    return res
