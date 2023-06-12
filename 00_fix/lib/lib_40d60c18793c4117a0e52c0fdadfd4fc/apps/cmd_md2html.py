import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab

class cmd_md2html(cab.cmd_app):

    @staticmethod
    def start_md2html_path(is_test:bool=False):
        app = None
        if is_test:
            app = cmd_md2html(
                "00f4d582243344f6979a2b5428fd194b",
                [
                    "test.py",
                    "-src_md_path:test.md",
                    "-src_cfg_path:test_cfg.json",
                    "-src_tmp_path:test_template.html",
                    "-dest_path:test.html",
                ])
        else:
            app = cmd_md2html("00f4d582243344f6979a2b5428fd194b",a.startup_params())

        app.add_param_cfg_text("src_md_path")
        app.add_param_cfg_text("src_cfg_path")
        app.add_param_cfg_text("src_tmp_path")
        app.add_param_cfg_text("dest_path")
        app.reg_main(cnv_md2html)
        app.start()
    @staticmethod
    def start_md2html_name(is_test:bool=False):
        app = None
        if is_test:
            raise Exception("未対応")
        else:
            app = cmd_md2html("6ebde7519a1c4fcb9d2fc6317f631e35",a.startup_params())

        app.add_param_cfg_path_name("src_md_name")
        app.add_param_cfg_path_name("src_cfg_name")
        app.add_param_cfg_path_name("src_tmp_name")
        app.add_param_cfg_path_name("dest_name")
        app.reg_main(cnv_md2html)
        app.start()

def cnv_md2html(s:cmd_md2html, src_md_path:str,src_cfg_path:str,src_tmp_path:str, dest_path:str):
    src_md_text   = a.load_text(src_md_path)
    src_json_path = a.cnv_abs_file_path_none_ext(src_md_path)+".json"
    src_json_data = dict()
    try:
        src_json_data = a.load_json(src_json_path)
    except:
        src_json_data = dict()
    src_cfg_data = a.load_json(src_cfg_path)
    html_text = a.cnv_markdown_to_html(src_md_text)
    cfg_data = dict()
    cfg_data["data_0ad5e680ae104f759b7452632d6f6380"]=src_cfg_data
    cfg_data["data_5748645e84d54977b42c83f3b9527a3b"]=html_text
    cfg_data["data_e92b12a896bb4e8dbdef1c83ab77e025"]=src_json_data
    dst_text = a.cnv_template_to_text(cfg_data,src_tmp_path)
    a.save_text(dest_path,dst_text)
def cnv_md2html_name(s:cmd_md2html, src_md_name:str,src_cfg_name:str,src_tmp_name:str, dest_name:str):
    cnv_md2html(s,src_md_name,src_cfg_name,src_tmp_name,dest_name)
