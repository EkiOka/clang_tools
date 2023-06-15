import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl

class cmd(cab.cmd_app):
    pass

def __main(s:cmd):
    upl = pl.user_path_list()
    file_tmp_file_list_target_inc = upl.get("file_tmp_file_list_target_inc","")
    file_out_file_list_target_src = upl.get("file_out_file_list_target_src","")
    if file_tmp_file_list_target_inc == "" or file_out_file_list_target_src == "":
        a.raise_Exception("file_tmp_file_list_target_inc, またはfile_out_file_list_target_srcが設定されていません。user_init.batを実行してください。")
    src_files = a.load_json(file_out_file_list_target_src)
    src_dirs = [ a.cnv_abs_dir_path(file) for file in src_files]
    src_dirs = list(set(src_dirs)) # 重複削除
    a.save_json(file_tmp_file_list_target_inc,src_dirs)
    return

app = cmd("76193c396970407f9d8b4496f5c2c6c9")
app.reg_main(__main)
app.start()
