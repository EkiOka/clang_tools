import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl


class cmd_init_path(cab.cmd_app):
    pass


def initialize(s: cmd_init_path):
    a.set_log_id("7b4bd489e3774252b3811288cfe321b4")
    a.log_debug(f"stat initialize.")
    dest_env = pl.env_path_list()

    ws = a.get_cur_dir()

    dest_env["dir_tools"] = [
        f"{ws}\\00_fix\\tools",
        f"{ws}\\20_user\\tools",
        f"{ws}\\10_base\\tools",
    ]

    dest_env["dir_lib"] = f"{ws}\\00_fix\\lib"
    dest_env["dir_cmd"] = f"{ws}\\00_fix\\cmd"

    dest_env["dir_base"] = f"{ws}\\10_base"
    dest_env["dir_base_cmd"] = f"{ws}\\10_base\\cmd"

    dest_env["dir_user"] = f"{ws}\\20_user"
    dest_env["dir_user_cmd"] = f"{ws}\\20_user\\cmd"

    pl.update_evn_path(dest_env)
    pl.update_user_path(dest_env)

    for k, v in dest_env.items():
        if str(k).find("dir_") == 0:
            if isinstance(v, str):
                a.log_debug(f"key : {k} / value : {v}")
                if not (a.is_exist(v)):
                    a.log_debug(f"make_dir:{v}")
                    a.make_dir(v)
            elif isinstance(v, list):
                for item in v:
                    a.log_debug(f"key : {k} / value : {item}")
                    if not (a.is_exist(item)):
                        a.log_debug(f"make_dir:{item}")
                        a.make_dir(item)
    a.log_debug(f"complete initialize.")
    a.set_log_id()


app = cmd_init_path("7cfa9d28d6604519a4cc0b37a985e8c4")
app.reg_main(initialize)
app.start()
