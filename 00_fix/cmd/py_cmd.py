from lib_a48c5c3ad4e94017bcc275492c101193 import ul

params = ul.get_start_params()
py = params.pop(0)
env_vars = ul.get_env_vars()
env_id = ul.get_env_id()
prefix = f"{py} > "

def __init():

    path_list = ul.load_path()
    env_path = path_list.get(env_id,{})
    dir_tools = env_path.get("dir_tools","")
    dir_user_tools = env_path.get("dir_user_tools","")
    dir_base_tools = env_path.get("dir_base_tools","")

    if dir_tools == "" or dir_user_tools == "" or dir_base_tools == "":

        ul.log_enable(prefix=prefix)
        dir_tools = env_vars.get("CLT_TOOLS_DIR","")
        ul.log_debug(f"dir_tools : {dir_tools}")

        if dir_tools == "":

            ul.log_debug(f"env_vars : {env_vars}")
            ul.raise_NotFound(
                target="CLT_TOOLS_DIR",
                type_name="environment variable",
                prefix=prefix)
        else:

            cp = ul.start_proc(["py",f"{dir_tools}\\init.py"])

            if cp.returncode != 0:

                ul.raise_Exception(
                    f"path list initialize error. ({dir_tools}\\init.py)",
                    prefix=prefix)

def __main():

    path_list = ul.load_path()
    env_path = path_list.get(env_id,{})
    dir_tools = env_path.get("dir_tools","")
    dir_user_tools = env_path.get("dir_user_tools","")
    dir_base_tools = env_path.get("dir_base_tools","")

    if len(params) >= 1:

        cp = None
        tool_params = []
        tool_name = params.pop(0)
        tool_path = [
            f"{dir_tools}\\{tool_name}",
            f"{dir_user_tools}\\{tool_name}",
            f"{dir_base_tools}\\{tool_name}",
        ]

        ul.log_enable(prefix=prefix)

        for path in tool_path:

            p = ["py",path]
            p.extend(params)
            tool_params.append(p)

        for tp in tool_params:

            if ul.is_exist(tp[1]):

                try:

                    cp = ul.start_proc(tp)
                    break

                except:

                    ul.raise_Exception(
                        f"start process error.(params:{tp})",
                        prefix=prefix)

            else:

                ul.log_debug(f"command not found. ({tp[1]})")

        if cp == None:

            ul.raise_NotFound(
                target=f"{tool_name}",
                type_name="command",
                prefix=prefix)

    else:

        ul.raise_Exception(
            f"parameter count error. ({params})",
            prefix=prefix)
    return

__init()
__main()

