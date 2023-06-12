import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab

# import pip install library                                  python -m pip install --upgrade pip
import jinja2
class cmd_tmpl2txt(cab.cmd_app):

    @staticmethod
    def start_md2html_path(is_test:bool=False):
        app = None
        if is_test:
            raise Exception("未対応")
        else:
            app = cmd_tmpl2txt("f3e0bc2034514b5793db63b46e7a81b5",a.startup_params())
        app.add_param_cfg_text("src_tmp_path")
        app.add_param_cfg_text("src_cfg_path")
        app.add_param_cfg_text("dest_path")
        app.reg_main(cnv_tmpl2txt)
        app.start()
    @staticmethod
    def start_md2html_name(is_test:bool=False):
        app = None
        if is_test:
            raise Exception("未対応")
        else:
            app = cmd_tmpl2txt("6f0c7790f29b494f984d2a0d6cb8c0cb",a.startup_params())
        app.add_param_cfg_path_name("src_tmp_name")
        app.add_param_cfg_path_name("src_cfg_name")
        app.add_param_cfg_path_name("dest_name")
        app.reg_main(cnv_tmpl2txt_name)
        app.start()

def cnv_tmpl2txt(s:cmd_tmpl2txt, src_tmp_path:str,src_cfg_path:str, dest_path:str):
    src_cfg_data = a.load_json(src_cfg_path)
    cfg_data = dict()
    cfg_data["data_0ad5e680ae104f759b7452632d6f6380"]=src_cfg_data
    dst_text = a.cnv_template_to_text(cfg_data,src_tmp_path)
    a.save_text(dest_path,dst_text)
def cnv_tmpl2txt_name(s:cmd_tmpl2txt, src_tmp_name:str,src_cfg_name:str, dest_name:str):
    cnv_tmpl2txt(s,src_tmp_name,src_cfg_name,dest_name)
