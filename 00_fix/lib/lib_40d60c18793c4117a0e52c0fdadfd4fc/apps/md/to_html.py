import sys
from importlib import import_module

import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps as lib

# import pip install library                                  python -m pip install --upgrade pip
import jinja2
import markdown                                             # pip install markdown
from markdown_include.include import MarkdownInclude        # pip install markdown-include
from md2html_links import CustomLinkExtension               # download https://github.com/ricmua/markdown-md2html_links
                                                            # and copy md2html_links.py to python lib
class Z__md_preprocessor(markdown.preprocessors.Preprocessor):

    has_mermaid = False

    def run_lines(self, lines):
        re = import_module("re")
        string = import_module("string")
        # ca = code area
        pat_ca_start = re.compile(
            r"^(?P<code_area_sign>[\~\`]{3})[\ \t]*(?P<code_area_name>[a-zA-Z_]*)[\ \t]*$")
        pat_ca_end = re.compile(
            r"^(?P<code_area_sign>[\~\`]{3})[\ \t]*$")

        result_lines = []
        code_area_sign = ""
        code_area_name = ""
        for line in lines:
            code_changed = False
            src_line = line
            print_line = ''.join(filter(lambda x: x in string.printable, line))

            match code_area_name:
                case "":
                    mat = pat_ca_start.match(print_line)
                    if mat:
                        code_area_sign = mat.group("code_area_sign")
                        code_area_name = mat.group("code_area_name")
                        if code_area_name == "mermaid":
                            result_lines.append('<div class="mermaid">')
                            self.has_mermaid = True
                            code_changed = True
                        else:
                            code_area_name = "-"

                case "mermaid":
                    mat = pat_ca_end.match(print_line)
                    if mat:
                        if mat.group("code_area_sign") == code_area_sign:
                            result_lines.append("</div>")
                            result_lines.append("")
                            code_area_name = "" # area end
                            code_changed = True
                    if not code_changed:
                        result_lines.append(src_line.strip())
                        code_changed = True

                case "-": # not supported area
                    mat = pat_ca_end.match(print_line)
                    if mat:
                        if mat.group("code_area_sign") == code_area_sign:
                            code_area_name = "" # area end
                    pass

            if not code_changed:
                result_lines.append(src_line)

        return result_lines

    def run(self, lines):
        result_lines = self.run_lines(lines)
        return result_lines
class Z__md_extension(markdown.Extension):
    def extendMarkdown(self, md:markdown.core.Markdown, md_globals=None):
        """ add extension instance. """
        pp =Z__md_preprocessor(md)
        md.preprocessors.register(pp, 'my_pre_proc', 35)
        md.registerExtension(self)

    def makeExtension(**kwargs):
        return Z__md_extension(**kwargs)
class cmd_md2html(lib.cmd_app):

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
            app = cmd_md2html("00f4d582243344f6979a2b5428fd194b",sys.argv)

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
            app = cmd_md2html("6ebde7519a1c4fcb9d2fc6317f631e35",sys.argv)

        app.add_param_cfg_path_name("src_md_name")
        app.add_param_cfg_path_name("src_cfg_name")
        app.add_param_cfg_path_name("src_tmp_name")
        app.add_param_cfg_path_name("dest_name")
        app.reg_main(cnv_md2html)
        app.start()

    def cnv_markdown_to_html(s,src:str, include_base_path=".")->str:
        md = markdown.Markdown(extensions=[
            Z__md_extension(),
            "admonition",
            "tables",
            "toc",
            "nl2br",
            "codehilite",
            "fenced_code",
            MarkdownInclude(configs={'base_path':include_base_path}),
            CustomLinkExtension(),
            ],
            extension_configs={
                "toc": { "toc_depth": "2-3" }
            }
            )
        res = md.convert(src)
        return res
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
def cnv_md2html(s:cmd_md2html, src_md_path:str,src_cfg_path:str,src_tmp_path:str, dest_path:str):
    u = s.base_cmd_app.utility
    src_md_text  = u.load_text(src_md_path)
    src_md_dir   = u.cnv_abs_dir_path(src_md_path)
    src_json_name = u.cnv_file_name_none_ext(src_md_path)+".json"
    src_json_path = f"{src_md_dir}\\{src_json_name}"
    src_json_data = dict()
    try:
        src_json_data = u.load_json(src_json_path)
    except:
        src_json_data = dict()
    src_cfg_data = u.load_json(src_cfg_path)
    html_text = s.cnv_markdown_to_html(src_md_text)
    cfg_data = dict()
    cfg_data["data_0ad5e680ae104f759b7452632d6f6380"]=src_cfg_data
    cfg_data["data_5748645e84d54977b42c83f3b9527a3b"]=html_text
    cfg_data["data_e92b12a896bb4e8dbdef1c83ab77e025"]=src_json_data
    dst_text = s.cnv_template_to_text(cfg_data,src_tmp_path)
    u.save_text(dest_path,dst_text)
def cnv_md2html_name(s:cmd_md2html, src_md_name:str,src_cfg_name:str,src_tmp_name:str, dest_name:str):
    cnv_md2html(s,src_md_name,src_cfg_name,src_tmp_name,dest_name)
