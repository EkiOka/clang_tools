import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a

id = "1c4e9c8c730b48c28799b0fccab4d63e"


def __main(s: cab.cmd_app, src_name: str, dest_name: str, target: str):
    a.set_log_id("d3ff7b7c81e74b2fba24922a092e32b0")
    a.log_debug(f"src_name  : {src_name}")
    a.log_debug(f"dest_name : {dest_name}")
    a.log_debug(f"target    : {target}")

    exe_make = pl.get_user_path("exe_make")

    a.log_debug(f"exe_make  : {exe_make}")

    dest = a.cnv_template_to_text({}, src_name)
    a.save_text(dest_name, dest)
    res = a.start_proc([exe_make, "--no-print-directory",
                       f"--makefile={dest_name}", target])
    a.log_debug(f"res       : {res}")
    a.set_log_id()
    a.sys.exit(res)


a.log_setup("d3ff7b7c81e74b2fba24922a092e32b0")
a.set_log_id(id)

app = cab.cmd_app(id)
app.reg_main(__main)
app.add_param_cfg_usr_path_name("src_name")
app.add_param_cfg_usr_path_name("dest_name")
app.add_param_cfg_text("target")
app.start()

a.set_log_id()
