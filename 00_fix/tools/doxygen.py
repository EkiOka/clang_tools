import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list          as pl
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp           as a

# a.log_enable_debug("5f8032979a844aa9a2bf385b9c74d74b")

def __main(s:cab.cmd_app, doxyfile_name:str):

    file = a.cur_file_name()
    func = a.cur_function_name()
    a.log_info(f"{file} > {func} > doxyfile_name : {doxyfile_name}")

    exe = pl.get_user_path("doxygen_exe")
    dest_path = pl.get_env_path("file_tmp_doxyfile")

    a.log_info(f"{file} > {func} > exe           : {exe}")
    a.log_info(f"{file} > {func} > dest_path     : {dest_path}")
    
    dest = a.cnv_template_to_text({},doxyfile_name)

    a.log_info(f"{file} > {func} > dest          : {dest[:30]}(...)")

    a.save_text(dest_path,dest)
    res = a.start_proc([exe,dest_path])

    a.log_info(f"{file} > {func} > res           : {res}")

    a.sys.exit(res)

app = cab.cmd_app("e32273a247e14ba5a8839b3b35d7e42b")
app.reg_main(__main)
app.add_param_cfg_env_path_name("doxyfile_name")
app.start()
