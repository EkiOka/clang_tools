import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab

class cmd(cab.cmd_app):
    pass

def __main(s,src_md_path:str,src_cfg_name:str,src_tmpl_name:str,dest_html_path:str):
    a.set_log_id("d8602c736fc4419cba6a27baf3ce0992")
    func = a.cur_function_name()
    a.log_debug(f"{func} > src_md_path    : {src_md_path}")
    a.log_debug(f"{func} > src_cfg_name   : {src_cfg_name}")
    a.log_debug(f"{func} > src_tmpl_name  : {src_tmpl_name}")
    a.log_debug(f"{func} > dest_html_path : {dest_html_path}")

    src_cfg_path = src_cfg_name
    src_tmpl_path = src_tmpl_name

    src_md_text   = a.load_text(src_md_path)
    src_md_dir    = a.cnv_abs_dir_path(src_md_path)
    src_yaml_path = a.cnv_abs_file_path_none_ext(src_md_path)+".yml"
    src_yaml_data = dict()
    try:
        src_yaml_data = a.load_yaml(src_yaml_path)
    except:
        src_yaml_data = dict()
    src_cfg_data = a.load_yaml(src_cfg_path)
    html_text = a.cnv_markdown_to_html(src_md_text,src_md_dir)
    a.log_debug(f"{func} > src_md_text : {src_md_text}")
    a.log_debug(f"{func} > html_text   : {html_text}")

    cfg_data = dict()
    cfg_data["data_0ad5e680ae104f759b7452632d6f6380"]=src_cfg_data
    cfg_data["data_5748645e84d54977b42c83f3b9527a3b"]=html_text
    cfg_data["data_e92b12a896bb4e8dbdef1c83ab77e025"]=src_yaml_data
    dst_text = a.cnv_template_to_text(cfg_data,src_tmpl_path)
    a.save_text(dest_html_path,dst_text)
    a.set_log_id()

app = cmd("18b32644f6fa4bc3b4603b71d574f99d")
app.reg_main(__main)
app.add_param_cfg_text("src_md_path")
app.add_param_cfg_usr_path_name("src_cfg_name")
app.add_param_cfg_usr_path_name("src_tmpl_name")
app.add_param_cfg_text("dest_html_path")
app.start()
