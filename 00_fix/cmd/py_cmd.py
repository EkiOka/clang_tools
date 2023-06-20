"""pythonコマンドを実行する

本スクリプトは可変長引数であるため、cmd_appを使用しない。

"""

import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl

def init():
    a.cur_logger_id = "8451209a5f2642459f3a6ff66b56e409"
    env_path:dict=dict()
    env_path = pl.env_path_list()
    
    dir_tools = env_path.get("dir_tools" ,[])

    if len(dir_tools) == 0:

        dir_tools = a.environ_variable("CLT_TOOLS_DIR","")
        a.log_debug(f"dir_tools : {dir_tools}")
        if dir_tools == "":
            a.raise_NotFound(
                target="CLT_TOOLS_DIR",
                type_name="environment variable")
        else:
            returncode = a.start_proc(["py",f"{dir_tools}\\init_path.py"])

            if returncode != 0:

                a.raise_Exception(
                    f"path list initialize error. ({dir_tools}\\init_path.py)")
    a.cur_logger_id = ""

def start_cmd():
    a.cur_logger_id = "ad4496626a664c46a84b203e5c9832c6"
    
    env_path:dict=dict()
    env_path = pl.env_path_list()

    dir_tools      = env_path.get("dir_tools",     "")
    params = a.startup_params()
    a.log_debug(f"params:{params}")

    if len(params) >= 1:

        tool_params = []
        params.pop(0)
        tool_name = params.pop(0)
        # .pyなししてい対応
        if a.cnv_file_ext(tool_name) == "":
            tool_name = tool_name + ".py"
        a.log_debug(f"tool_name:{tool_name}")

        tool_path = [ f"{dir}\\{tool_name}" for dir in dir_tools ]

        # 起動パラメータ生成
        for path in tool_path:
            p = ["py",path]
            p.extend(params)
            tool_params.append(p)

        returncode = None
        for tp in tool_params:
            if a.is_exist(tp[1]):
                try:
                    returncode = a.start_proc(tp)
                    break
                except:
                    a.raise_Exception(f"start process error.(params:{tp})")
        if returncode == None:
            a.log_info("コマンドを発見できませんでした。探索対象となったパスをダンプします。")
            for tp in tool_params:
                a.log_info(str(tp))
            a.raise_NotFound(
                target=f"{tool_name}",
                type_name="command")
    else:
        a.raise_Exception(f"parameter count error. ({params})")
    a.cur_logger_id = ""
    return


init()
start_cmd()
