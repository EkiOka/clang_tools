import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a

id = "f81080a3582b4378a7fa7b0a3b2654f5"

def __main(s: cab.cmd_app, src_name: str, dest_name: str, target: str):

    a.set_log_id(id)

    a.log_debug(f"src_name  : {src_name}")
    a.log_debug(f"dest_name : {dest_name}")
    a.log_debug(f"target    : {target}")
    if not a.is_exist(src_name):
        a.log_error(f"src_nameで指定したファイル({src_name})が存在しません。")
        a.sys.exit(1)

    exe_make = pl.get_user_path("exe_make")
    if not a.is_exist(exe_make):
        a.log_error(f"exe_makeで指定したファイル({exe_make})が存在しません。")
        a.sys.exit(1)

    a.log_debug(f"exe_make  : {exe_make}")

    dest = a.cnv_template_to_text({}, src_name)
    a.save_text(dest_name, dest)
    res = a.start_proc([exe_make, "--no-print-directory",
                       f"--makefile={dest_name}", target])
    a.log_debug(f"res       : {res}")
    a.set_log_id()
    a.sys.exit(res)

a.log_setup(id)

app = cab.cmd_app(id)
app.reg_main(__main)
app.add_param_cfg_usr_path_name("src_name")
app.add_param_cfg_usr_path_name("dest_name")
app.add_param_cfg_text("target")
app.start()

