import sys
from importlib import import_module

import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps as lib

# import pip install library                                  python -m pip install --upgrade pip
import jinja2
class cmd_tmpl2txt(lib.cmd_app):

    @staticmethod
    def start_md2html_path(is_test:bool=False):
        app = None
        if is_test:
            raise Exception("未対応")
        else:
            app = cmd_tmpl2txt("f3e0bc2034514b5793db63b46e7a81b5",sys.argv)
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
            app = cmd_tmpl2txt("6f0c7790f29b494f984d2a0d6cb8c0cb",sys.argv)
        app.add_param_cfg_path_name("src_tmp_name")
        app.add_param_cfg_path_name("src_cfg_name")
        app.add_param_cfg_path_name("dest_name")
        app.reg_main(cnv_tmpl2txt_name)
        app.start()

    def cnv_template_to_text(s,data:dict,template_path:str)->str:
        u = s.base_cmd_app.utility
        os = u.load_module("os")

        cur = u.cur_dir
        tmp_abs_path  = u.cnv_abs_full_path(template_path)
        tmp_dir       = u.cnv_abs_dir_path(tmp_abs_path)
        tmp_file      = u.cnv_file_name(template_path)
        tmp_file      = tmp_file.replace("\\","/")
        tmp_dir       = tmp_dir.replace("\\","/")
        tmp_abs_path  = tmp_abs_path.replace("\\","/")
        tmp_file_name = u.cnv_file_name(tmp_abs_path)

        u.log_info(f"tmp_abs_path:{tmp_abs_path}")
        u.log_info(f"tmp_dir:{tmp_dir}")
        u.log_info(f"tmp_file:{tmp_file}")
        u.log_info(f"tmp_dir:{tmp_dir}")
        u.log_info(f"tmp_file_name:{tmp_file_name}")

        u.cur_dir = tmp_dir

        loader         = jinja2.FileSystemLoader( searchpath=tmp_dir, encoding='utf-8')
        environment    = jinja2.Environment(loader=loader)

        temp_data = dict()
        temp_data["data_4d22a990e03e4ff0b66061daa1674a0d"]=dict(os.environ)
        temp_data.update(data)

        try:
            template  = environment.get_template(name=tmp_file_name)
            out_text  = template.render(temp_data)
        except jinja2.exceptions.UndefinedError as e:
            u.log_error( f"テンプレートへ入力しているデータをダンプします。")
            u.log_error(temp_data)
            u.log_error(e)
            u.cur_dir = cur
            sys.exit(1)
        except jinja2.exceptions.TemplateNotFound as e:
            u.log_error(e)
            u.log_error( f"template_path : {template_path}")
            u.log_error( f"tmp_dir       : {tmp_dir}")
            u.log_error( f"tmp_file      : {tmp_file}")
            u.log_error( f"cur           : {cur} -> {u.cur_dir}")
            u.log_error( f"raise ファイル「{e}」が見つかりませんでした。")
            u.cur_dir = cur
            sys.exit(1)

        u.cur_dir = cur

        return out_text


def cnv_tmpl2txt(s:cmd_tmpl2txt, src_tmp_path:str,src_cfg_path:str, dest_path:str):
    u = s.base_cmd_app.utility
    src_cfg_data = u.load_json(src_cfg_path)
    cfg_data = dict()
    cfg_data["data_0ad5e680ae104f759b7452632d6f6380"]=src_cfg_data
    dst_text = s.cnv_template_to_text(cfg_data,src_tmp_path)
    u.save_text(dest_path,dst_text)
def cnv_tmpl2txt_name(s:cmd_tmpl2txt, src_tmp_name:str,src_cfg_name:str, dest_name:str):
    cnv_tmpl2txt(s,src_tmp_name,src_cfg_name,dest_name)
