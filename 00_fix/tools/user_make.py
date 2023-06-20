import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list          as pl
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp           as a

def __main(s:cab.cmd_app, src_name:str, dest_name:str, target:str):
    make_exe_path = pl.get_user_path("make_exe")
    dest = a.cnv_template_to_text({},src_name)
    a.save_text(dest_name,dest)
    res = a.start_proc([make_exe_path,"--no-print-directory",f"--makefile={dest_name}",target])
    a.sys.exit(res)

app = cab.cmd_app("1c4e9c8c730b48c28799b0fccab4d63e")
app.reg_main(__main)
app.add_param_cfg_usr_path_name("src_name")
app.add_param_cfg_usr_path_name("dest_name")
app.add_param_cfg_text("target")
app.start()
