from lib_a48c5c3ad4e94017bcc275492c101193 import ul

def initialize(py:str, vscode_debug:bool):
    id = ul.get_env_id()
    if id == ul.id:
        raise Exception("環境変数 env_id が設定されていません。")

    path_list = ul.load_path()
    dest = path_list.get(id,{})
    path_list[id]=dest

    ws = ul.get_cur_dir()

    dest[ "dir_tools"         ] = f"{ws}\\00_fix\\tools"
    dest[ "dir_lib"           ] = f"{ws}\\00_fix\\lib"
    dest[ "dir_cmd"           ] = f"{ws}\\00_fix\\cmd"

    dest[ "dir_base_cfg"      ] = f"{ws}\\10_base\\cfg"
    dest[ "dir_base_src"      ] = f"{ws}\\10_base\\src"
    dest[ "dir_base_template" ] = f"{ws}\\10_base\\template"
    dest[ "dir_user_cfg"      ] = f"{ws}\\20_user\\cfg"
    dest[ "dir_user_src"      ] = f"{ws}\\20_user\\src"
    dest[ "dir_user_template" ] = f"{ws}\\20_user\\template"

    dest[ "dir_tmp_filelist"  ] = f"{ws}\\50_out_tmp\\filelist"
    dest[ "dir_tmp_dox_mk"    ] = f"{ws}\\50_out_tmp\\doxygen\\mk"
    dest[ "dir_tmp_dox_res"   ] = f"{ws}\\50_out_tmp\\doxygen\\result"
    dest[ "dir_tmp_dox_xml"   ] = f"{ws}\\50_out_tmp\\doxygen\\xml"
    dest[ "dir_tmp_dox_yml"   ] = f"{ws}\\50_out_tmp\\doxygen\\yml"

    dest[ "dir_out_filelist"  ] = f"{ws}\\60_out\\filelist"
    dest[ "dir_out_dox_mk"    ] = f"{ws}\\60_out\\doxygen\\mk"
    dest[ "dir_out_dox_res"   ] = f"{ws}\\60_out\\doxygen\\result"
    dest[ "dir_out_dox_xml"   ] = f"{ws}\\60_out\\doxygen\\xml"
    dest[ "dir_out_dox_yml"   ] = f"{ws}\\60_out\\doxygen\\yml"

    dest[ "mask_dox_xml_files"     ] = f"{ws}\\50_out_tmp\\doxygen\\xml\\**\\*_8c.xml"
    dest[ "file_doxyfile_template" ] = f"{ws}\\20_user\\template\\Doxyfile"

    dest[ "file_dox_mk_template" ] = f"{ws}\\20_user\\template\\doxygen.mk"
    dest[ "file_tmp_dox_mk"    ] = f"{ws}\\50_out_tmp\\doxygen\\mk\\doxygen.mk"
    dest[ "file_out_dox_mk"    ] = f"{ws}\\60_out\\doxygen\\mk\\doxygen.mk"

    dest[ "file_tmp_dox_marge_yml"  ] = f"{ws}\\50_out_tmp\\doxygen\\result\\marge.yml"

    ul.update_path(path_list,id)

app = ul.cmd_app()
app.start(__name__,initialize)
