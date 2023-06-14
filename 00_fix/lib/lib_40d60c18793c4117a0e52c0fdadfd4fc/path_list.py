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
    res = a.environ_variable(EVAR_NAME_PATH_LIST,"")
    if res == "":
        a.raise_NotFound(
            target=EVAR_NAME_PATH_LIST,
            type_name="environment variable")

    return res


def load_path()->dict:
    """パスリスト読み出し"""
    path = path_list_path()
    plp = None
    try:
        plp = a.load_json(path)
    except:
        plp = dict()
    return plp
def save_path(path_list:dict):
    """パスリスト保存"""
    path = path_list_path()
    a.save_json(path,path_list)

def path_list(id:str)->dict:
    """固有パスリスト取得

    Parameters
    ----------
    id : str
        取得するパスリストID

    Returns
    -------
    dict
        パスリスト
    """
    res = {}
    if id == "":
        a.raise_NotFound(id,"path list ID")
    else:
        path_list = load_path()
        if id in path_list.keys():
            res = path_list[id]
        else:
            path_list[id]=res
            save_path(path_list)
    return res

def update_path(src:dict, id:str=env_id)->dict:
    """パスリスト一部更新
    """
    dest = load_path()
    src_id = src.get(id,{})
    dest_id = dest.get(id,{})
    dest_id.update(src_id)
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
    id = env_id()
    return path_list(id)

def user_path_list(s)->dict:
    """ユーザー固有パスリスト取得"""
    id = a.user_name()
    return path_list(id)

def get_path(name:str):
    res = ""
    split_name = name.split(SEP_ID2NAME)
    match(len(split_name)):
        case 1:
            name = split_name[0]
            lst = env_path_list()
            res = lst.get(name,"")
            pass
        case 2:
            id = split_name[0]
            name = split_name[2]
            lst = path_list(id)
            res = lst.get(name,"")
            pass
        case _:
            a.raise_Exception(f"nameの値{name}が異常です。")
    return res