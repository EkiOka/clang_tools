from lib_a48c5c3ad4e94017bcc275492c101193 import ul

params = ul.get_start_params()
py = params.pop(0)
env_vars = ul.get_env_vars()
env_id = ul.get_env_id()

def __init():
    path_list = ul.load_path()
    env_path = path_list.get(env_id,{})
    dir_tools = env_path.get("dir_tools","")
    dir_user_tools = env_path.get("dir_user_tools","")
    dir_base_tools = env_path.get("dir_base_tools","")

    if dir_tools == "" or dir_user_tools == "" or dir_base_tools == "":
        ul.log_enable()
        dir_tools = env_vars.get("CLT_TOOLS_DIR","")
        ul.log_debug(f"dir_tools : {dir_tools}")
        if dir_tools == "":
            ul.log_debug(f"env_vars : {env_vars}")
            raise Exception(f"{py} > environment variable `CLT_TOOLS_DIR` not found.")
        else:
            cp = ul.start_proc(["py",f"{dir_tools}\\init.py"])
            if cp.returncode != 0:
                raise Exception(f"{py} > path list initialize error. ({dir_tools}\\init.py)")

def __main():
    path_list = ul.load_path()
    env_path = path_list.get(env_id,{})
    dir_tools = env_path.get("dir_tools","")
    dir_user_tools = env_path.get("dir_user_tools","")
    dir_base_tools = env_path.get("dir_base_tools","")

    if len(params) >= 1:
        tool_name = params.pop(0)
        tool_path = [
            f"{dir_tools}\\{tool_name}",
            f"{dir_user_tools}\\{tool_name}",
            f"{dir_base_tools}\\{tool_name}",
        ]
        tool_params = []
        for path in tool_path:
            p = ["py",path]
            p.extend(params)
            tool_params.append(p)

        ul.log_enable()
        cp = None
        for tp in tool_params:
            if ul.is_exist(tp[1]):
                try:
                    cp = ul.start_proc(tp)
                except:
                    raise Exception(f"start process error.(params:{tp})")
                break
            else:
                ul.log_debug(f"{py} > command not found. ({tp[1]})")
        if cp == None:
            raise Exception(f"{py} > command not found. ({tool_name})")

    else:
        raise Exception(f"{py} > parameter count error. ({params})")

    return

__init()
__main()

