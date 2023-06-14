import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl

class cmd_update_copy(cab.cmd_app):
    def copy_update_file(s,src:str,dest:str)->bool:
        """ファイルの内容に変化がある場合は更新のため上書きコピーします
        日付の変更のみの場合はコピーしません。
        ファイルパスの指定にはマスクは使えません。
        """
        if not(a.is_exist(src)):
            a.raise_FileNotFound(src)
        run = False
        if not(a.is_exist(dest)):
            a.log_debug(f"copy_update_file > copy(not exits `{dest}`)")
            a.copy_file(src,dest)
            run = True
        else:
            src_size = a.get_file_size(src)
            dst_size = a.get_file_size(dest)

            if not(src_size==dst_size):
                a.log_debug(f"copy_update_file > copy(file size not equal)")
                a.copy_file(src,dest)
                run = True
            else:
                src_time = a.get_file_update_time(src)
                dest_time = a.get_file_update_time(dest)
                if not(src_time==dest_time):
                    src_sha  = a.get_file_sha256(src)   
                    dst_sha  = a.get_file_sha256(dest)   
                    if not(src_sha==dst_sha):
                        a.log_debug(f"copy_update_file > not copy(SHA equal)")
                        a.copy_file(src,dest)
                        run = True
                    else:
                        a.log_debug(f"copy_update_file > not copy(SHA equal)")
                else:
                    a.log_debug(f"copy_update_file > not copy(timestamp equal)")
        return run
    @staticmethod
    def gen_path_app():
        app = cmd_update_copy("caff57f74cfb44dc88661a3ca7875206")
        app.add_param_cfg_text("src_path")
        app.add_param_cfg_text("dest_path")
        app.reg_main(main_path)
        return app
    @staticmethod
    def gen_name_app():
        app = cmd_update_copy("40f6e4e9120f4663a73a6eaec65f05cc")
        app.add_param_cfg_path_name("src_name")
        app.add_param_cfg_path_name("dest_name")
        app.reg_main(main_name)
        return app

def main_path(s:cmd_update_copy,src_path:str,dest_path:str):
    s.copy_update_file(src_path,dest_path)

def main_name(s:cmd_update_copy,src_name:str,dest_name:str):
    main_path(s,src_name,dest_name)

