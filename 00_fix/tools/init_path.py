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
    dest_env["dir_base_cfg"] = f"{ws}\\10_base\\cfg"
    dest_env["dir_base_src"] = f"{ws}\\10_base\\src"
    dest_env["dir_base_template"] = f"{ws}\\10_base\\template"
    dest_env["dir_base_notes"] = f"{ws}\\10_base\\notes"
    dest_env["dir_base_cmd"] = f"{ws}\\10_base\\cmd"

    dest_env["dir_user"] = f"{ws}\\20_user"
    dest_env["dir_user_cfg"] = f"{ws}\\20_user\\cfg"
    dest_env["dir_user_src"] = f"{ws}\\20_user\\src"
    dest_env["dir_user_template"] = f"{ws}\\20_user\\template"
    dest_env["dir_user_notes"] = f"{ws}\\20_user\\notes"
    dest_env["dir_user_cmd"] = f"{ws}\\20_user\\cmd"

    dest_env["dir_base_tmpl_note"] = f"{ws}\\10_base\\template\\notes"
    dest_env["dir_user_tmpl_note"] = f"{ws}\\20_user\\template\\notes"

    dest_env["dir_tmp"] = f"{ws}\\50_out_tmp"
    dest_env["dir_tmp_filelist"] = f"{ws}\\50_out_tmp\\filelist"
    dest_env["dir_tmp_notes"] = f"{ws}\\50_out_tmp\\notes"
    dest_env["dir_tmp_dox"] = f"{ws}\\50_out_tmp\\doxygen"
    dest_env["dir_tmp_dox_mk"] = f"{ws}\\50_out_tmp\\doxygen\\mk"
    dest_env["dir_tmp_dox_res"] = f"{ws}\\50_out_tmp\\doxygen\\result"
    dest_env["dir_tmp_dox_xml"] = f"{ws}\\50_out_tmp\\doxygen\\xml"
    dest_env["dir_tmp_dox_yml"] = f"{ws}\\50_out_tmp\\doxygen\\yml"
    dest_env["dir_tmp_mk"] = f"{ws}\\50_out_tmp\\mk"

    dest_env["dir_out"] = f"{ws}\\60_out"
    dest_env["dir_out_filelist"] = f"{ws}\\60_out\\filelist"
    dest_env["dir_out_notes"] = f"{ws}\\60_out\\notes"
    dest_env["dir_out_dox"] = f"{ws}\\60_out\\doxygen"
    dest_env["dir_out_dox_mk"] = f"{ws}\\60_out\\doxygen\\mk"
    dest_env["dir_out_dox_res"] = f"{ws}\\60_out\\doxygen\\result"
    dest_env["dir_out_dox_xml"] = f"{ws}\\60_out\\doxygen\\xml"
    dest_env["dir_out_dox_yml"] = f"{ws}\\60_out\\doxygen\\yml"

    dest_env["mask_tmp_dox_xml_files"] = f"{ws}\\50_out_tmp\\doxygen\\xml\\**\\*_8c.xml"
    dest_env["mask_out_dox_xml_files"] = f"{ws}\\60_out\\doxygen\\xml\\**\\*_8c.xml"
    dest_env["file_doxyfile_template"] = f"{ws}\\20_user\\template\\doxygen\\Doxyfile"

    dest_env["file_dox_mk_template"] = f"{ws}\\20_user\\template\\doxygen.mk"
    dest_env["file_tmp_doxyfile"] = f"{ws}\\50_out_tmp\\doxygen\\Doxyfile"
    dest_env["file_tmp_dox_mk"] = f"{ws}\\50_out_tmp\\doxygen\\mk\\doxygen.mk"
    dest_env["file_out_dox_mk"] = f"{ws}\\60_out\\doxygen\\mk\\doxygen.mk"

    dest_env["file_tmp_dox_marge_yml"] = f"{ws}\\50_out_tmp\\doxygen\\result\\marge.yml"

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
