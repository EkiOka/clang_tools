import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a


def __main(s: cab.cmd_app, doxyfile_name: str):
    a.set_log_id("fbb03656fb5942b084faf81e37219c42")
    if not a.is_exist(doxyfile_name):
        a.log_error(f"doxyfile_nameで指定したファイル({doxyfile_name})が存在しません。")
        a.sys.exit(1)

    file = a.cur_file_name()
    func = a.cur_function_name()

    a.log_debug(f"{file} > {func} > doxyfile_name : {doxyfile_name}")

    exe = pl.get_user_path("exe_doxygen")
    dest_path = pl.get_user_path("file_tmp_doxyfile")
    file_cfg_doxygen = pl.get_user_path("file_cfg_doxygen")
    if not a.is_exist(file_cfg_doxygen):
        a.log_error(f"file_cfg_doxygenで指定したファイル({file_cfg_doxygen})が存在しません。")
        a.sys.exit(1)


    a.log_debug(f"{file} > {func} > exe               : {exe}")
    a.log_debug(f"{file} > {func} > dest_path         : {dest_path}")
    a.log_debug(f"{file} > {func} > file_cfg_doxygen  : {file_cfg_doxygen}")

    cfg = a.load_yaml(file_cfg_doxygen)

    dest = a.cnv_template_to_text(cfg, doxyfile_name)

    a.log_debug(f"{file} > {func} > dest          : {dest[:30]}(...)")

    a.save_text(dest_path, dest)
    res = a.start_proc([exe, dest_path])

    a.log_debug(f"{file} > {func} > res           : {res}")

    a.set_log_id()
    a.sys.exit(res)


app = cab.cmd_app("e32273a247e14ba5a8839b3b35d7e42b")
app.reg_main(__main)
app.add_param_cfg_path_name("doxyfile_name")
app.start()
