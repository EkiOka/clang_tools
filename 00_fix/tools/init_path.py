import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl

class cmd_init_path(cab.cmd_app):
    pass

def initialize(s:cmd_init_path):
    a.log_debug(f"stat initialize.")
    dest = pl.env_path_list()

    ws = a.get_cur_dir()

    dest[ "dir_tools"         ] = [
        f"{ws}\\00_fix\\tools",
        f"{ws}\\20_user\\tools",
        f"{ws}\\10_base\\tools",
    ]

    dest[ "dir_lib"           ] = f"{ws}\\00_fix\\lib"
    dest[ "dir_cmd"           ] = f"{ws}\\00_fix\\cmd"

    dest[ "dir_base"          ] = f"{ws}\\10_base"
    dest[ "dir_base_cfg"      ] = f"{ws}\\10_base\\cfg"
    dest[ "dir_base_src"      ] = f"{ws}\\10_base\\src"
    dest[ "dir_base_template" ] = f"{ws}\\10_base\\template"
    dest[ "dir_base_notes"    ] = f"{ws}\\10_base\\notes"
    dest[ "dir_base_cmd"      ] = f"{ws}\\10_base\\cmd"

    dest[ "dir_user"          ] = f"{ws}\\20_user"
    dest[ "dir_user_cfg"      ] = f"{ws}\\20_user\\cfg"
    dest[ "dir_user_src"      ] = f"{ws}\\20_user\\src"
    dest[ "dir_user_template" ] = f"{ws}\\20_user\\template"
    dest[ "dir_user_notes"    ] = f"{ws}\\20_user\\notes"
    dest[ "dir_user_cmd"      ] = f"{ws}\\20_user\\cmd"

    dest[ "dir_base_tmpl_note" ] = f"{ws}\\10_base\\template\\notes"
    dest[ "dir_user_tmpl_note" ] = f"{ws}\\20_user\\template\\notes"

    dest[ "dir_tmp"             ] = f"{ws}\\50_out_tmp"
    dest[ "dir_tmp_filelist"    ] = f"{ws}\\50_out_tmp\\filelist"
    dest[ "dir_tmp_notes"       ] = f"{ws}\\50_out_tmp\\notes"
    dest[ "dir_tmp_dox"         ] = f"{ws}\\50_out_tmp\\doxygen"
    dest[ "dir_tmp_dox_mk"      ] = f"{ws}\\50_out_tmp\\doxygen\\mk"
    dest[ "dir_tmp_dox_res"     ] = f"{ws}\\50_out_tmp\\doxygen\\result"
    dest[ "dir_tmp_dox_xml"     ] = f"{ws}\\50_out_tmp\\doxygen\\xml"
    dest[ "dir_tmp_dox_yml"     ] = f"{ws}\\50_out_tmp\\doxygen\\yml"
    dest[ "dir_tmp_mk"          ] = f"{ws}\\50_out_tmp\\mk"

    dest[ "dir_out"             ] = f"{ws}\\60_out"
    dest[ "dir_out_filelist"    ] = f"{ws}\\60_out\\filelist"
    dest[ "dir_out_notes"       ] = f"{ws}\\60_out\\notes"
    dest[ "dir_out_dox"         ] = f"{ws}\\60_out\\doxygen"
    dest[ "dir_out_dox_mk"      ] = f"{ws}\\60_out\\doxygen\\mk"
    dest[ "dir_out_dox_res"     ] = f"{ws}\\60_out\\doxygen\\result"
    dest[ "dir_out_dox_xml"     ] = f"{ws}\\60_out\\doxygen\\xml"
    dest[ "dir_out_dox_yml"     ] = f"{ws}\\60_out\\doxygen\\yml"

    dest[ "mask_tmp_dox_xml_files" ] = f"{ws}\\50_out_tmp\\doxygen\\xml\\**\\*_8c.xml"
    dest[ "mask_out_dox_xml_files" ] = f"{ws}\\60_out\\doxygen\\xml\\**\\*_8c.xml"
    dest[ "file_doxyfile_template" ] = f"{ws}\\20_user\\template\\doxygen\\Doxyfile"

    dest[ "file_dox_mk_template" ] = f"{ws}\\20_user\\template\\doxygen.mk"
    dest[ "file_tmp_doxyfile"    ] = f"{ws}\\50_out_tmp\\doxygen\\Doxyfile"
    dest[ "file_tmp_dox_mk"    ] = f"{ws}\\50_out_tmp\\doxygen\\mk\\doxygen.mk"
    dest[ "file_out_dox_mk"    ] = f"{ws}\\60_out\\doxygen\\mk\\doxygen.mk"

    dest[ "file_tmp_dox_marge_yml"  ] = f"{ws}\\50_out_tmp\\doxygen\\result\\marge.yml"

    pl.update_evn_path(dest)

    for k,v in dest.items():
        if str(k).find("dir_") == 0:
           if isinstance(v,str):
                a.log_debug(f"key : {k} / value : {v}")
                if not(a.is_exist(v)):
                    a.log_debug(f"make_dir:{v}")
                    a.make_dir(v)
           elif isinstance(v,list):
               for item in v:
                    a.log_debug(f"key : {k} / value : {item}")
                    if not(a.is_exist(item)):
                        a.log_debug(f"make_dir:{item}")
                        a.make_dir(item)
    a.log_debug(f"complete initialize.")

app = cmd_init_path("7cfa9d28d6604519a4cc0b37a985e8c4")
app.reg_main(initialize)
app.start()
