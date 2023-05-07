
# import standard library
import uuid
import datetime
import hashlib
import os
import sys
import pathlib
import shutil
import glob
import json
import codecs
import tkinter
import logging
import logging.config
import traceback
import re
import string
import inspect
import platform
import xml.etree.ElementTree as ET

# import pip install library                                  python -m pip install --upgrade pip
import jinja2                                               # pip install jinja2
import openpyxl                                             # pip install openpyxl
import markdown                                             # pip install markdown
from markdown_include.include import MarkdownInclude        # pip install markdown-include
from markdown_checklist.extension import ChecklistExtension # pip install markdown-checklist
import yaml                                                 # pip install pyyaml
import xmltodict                                            # pip install xmltodict



class lib:
    class log:
        @staticmethod
        def enable(cfg=None):
            if cfg == None:            
                cfg = {
                    "version": 1,
                    "disable_existing_loggers": False,
                    "formatters": {
                        # フォーマットの説明は以下参照
                        # https://docs.python.org/ja/3/library/logging.html#logrecord-attributes
                        "standard": {
                            "format": "python(%(levelname)s) > %(message)s"
                        },
                        "add_position": {
                            "format": "python(%(levelname)s) > %(funcName)s %(lineno)s %(message)s"
                        }
                    },

                    "handlers": {
                        "console": {
                            "class": "logging.StreamHandler",
                            "level": "DEBUG",
                            "formatter": "standard",
                            "stream": "ext://sys.stdout"
                        },
                        # "file": {
                        #     "class": "logging.FileHandler",
                        #     "level": "INFO",
                        #     "formatter": "standard",
                        #     "filename": f"{__name__}.log"
                        # },
                        "null": {
                            "class": "logging.NullHandler"
                        }
                    },

                    "loggers": {
                        f"{__name__}": {
                            "level": "DEBUG",
                            "handlers": ["console"],
                            "propagate": False
                        }
                    },

                    "root": {
                        "level": "INFO"
                    }
                }

            logging.config.dictConfig(cfg)

        @staticmethod
        def debug(text:str,name:str=__name__):
            log = logging.getLogger(name)
            log.debug(text)
        @staticmethod
        def info(text:str,name:str=__name__):
            log = logging.getLogger(name)
            log.info(text)
        @staticmethod
        def warning(text:str,name:str=__name__):
            log = logging.getLogger(name)
            log.info(text)
        @staticmethod
        def critical(text:str,name:str=__name__):
            log = logging.getLogger(name)
            log.critical(text)

    class text:

        @staticmethod
        def load(path:str)->str:
            res = ""
            with open(path, encoding="utf-8") as f:
                res = f.read()
            return res

        @staticmethod
        def save(path:str,text:str):
            with open(path, mode="w", encoding="utf-8") as f:
                f.write(text)

        @staticmethod
        def to_sha256(text:str)->str:
            return hashlib.sha256(text.encode()).hexdigest()

        @staticmethod
        def to_sha512(text:str)->str:
            return hashlib.sha512(text.encode()).hexdigest()

    class hashlib:

        @staticmethod
        def cnv_file_to_sha256( path : str)->str:
            with open(path, 'rb') as file:
                fileData = file.read()
                res = hashlib.sha256(fileData).hexdigest()
            return res

        @staticmethod
        def cnv_str_to_sha256( string:str)->str:
            return hashlib.sha256(string.encode("utf-8")).hexdigest()

    class json:

        @staticmethod
        def load(path: str) -> dict:
            """json file to object.
            """
            try:
                with open(path, encoding="utf-8_sig") as f:
                    t = f.read()
                return json.loads(t)
            except Exception as e:
                return dict()


        @staticmethod
        def save(path: str,data, no_updated_file_over_write=True):
            """ jsonファイルとしてデータを保存する
                dictデータは順序が保証されないので比較できないため注意
                また既存のデータと内容が同じ場合は書き込みを行いません。
            """
            enc = "utf-8"
            ensure_ascii=False
            new_data = data
            old_data_str = ""
            if isinstance(data,dict):
                new_data = dict(sorted(data.items()))
                old_data_str = "{}"
            elif isinstance(data,list):
                new_data = list(sorted(data))
                old_data_str = "[]"
            if no_updated_file_over_write:
                with codecs.open(path , "w", enc) as f:
                    json.dump(new_data, f, ensure_ascii=ensure_ascii,indent=4, sort_keys=True)
            else:
                try:
                    old_data_str =json.dumps(lib.json.load(path),ensure_ascii=ensure_ascii,indent=4, sort_keys=True)
                    new_data_str =json.dumps(new_data,ensure_ascii=ensure_ascii,indent=4, sort_keys=True)
                except:
                    old_data_str = "{}"
                old_hash = lib.hashlib.cnv_str_to_sha256(old_data_str)
                new_hash = lib.hashlib.cnv_str_to_sha256(new_data_str)
                if old_hash == new_hash:
                    pass
                else:
                    with codecs.open(path , "w", enc) as f:
                        json.dump(data, f, ensure_ascii=ensure_ascii,indent=4, sort_keys=True)


    class yaml:

        @staticmethod
        def load(path: str) -> dict:
            """yaml file to object.
            """
            try:
                obj = dict()
                with open(path, encoding="utf-8_sig") as f:
                    obj = yaml.safe_load(f)
                    return obj
            except OSError as e:
                return None
        @staticmethod
        def save(path: str,obj):
            """object to yaml file.
            """
            with open(path, mode="w", encoding="utf-8_sig") as f:
                yaml.dump(obj,f, allow_unicode=True, default_flow_style=False)
                return
            
    class xml:
        @staticmethod
        def load(path: str) -> dict:
            """xml file to object.
            """
            try:
                xml_tree = ET.parse(path)
                obj = xml_tree.getroot()
                return obj
            except OSError as e:
                return None
        
        def load_dict(path:str)->dict:
            res = ""
            with open(path, encoding='utf-8') as file:
                # xml読み込み
                xml_data = file.read()
                # xml → dict
                res = xmltodict.parse(xml_data)
            return res

    class glob():
        @staticmethod
        def glob(mask,recursive=True):
            res = list()

            if type(mask) is list:
                for m in mask:
                    g = glob.glob(m,recursive=recursive)
                    res.extend(g)
            else:
                g = glob.glob(mask,recursive=recursive)
                res.extend(g)
            res = [item.replace("\\","/") for item in set(res)]
            return res

        @staticmethod
        def glob_dis(enable_masks:list,disable_masks:list,recursive=True)->list:
            enables = []
            disables = []
            for m in enable_masks:
                f = lib.glob.glob(m,recursive)
                enables.extend(f)
            for m in disable_masks:
                f = lib.glob.glob(m,recursive)
                disables.extend(f)
            
            res = list(set(enables) - set(disables))

            return res

        @staticmethod
        def gen_file_list(path:str,enable_masks:list,disable_masks:list,recursive=True,no_updated_file_over_write=False):
            res = lib.glob.glob_dis(enable_masks,disable_masks,recursive)
            res = list(sorted(res))
            lib.json.save(path, res,no_updated_file_over_write)

    class cmd_app:

        @staticmethod
        def __display_head(args,func,args_cfg,prefix):
            pf = prefix
            lib.log.debug(f"{pf}---------------------------------------------------")
            lib.log.debug(f"{pf}{args[0]}")
            lib.log.debug(f"{pf}---------------------------------------------------")
            lib.log.debug(f"{pf}cur_dir  : {os.getcwd()}")
            lib.log.debug(f"{pf}sys.argv : {args}")
            lib.log.debug(f"{pf}args_cfg : {args_cfg}")

        @staticmethod
        def __set_params(func,args_cfg:dict,args:list,prefix:str):
            pf = prefix
            ptn = re.compile("^-(?P<key>[a-zA-Z][0-9a-zA-Z_]*):(?P<value>.*)$")
            params = dict()
            arg_list=list(args_cfg.keys())
            key_max = max([len(x) for x in arg_list])
            for i in range(0,len(args),1):
                k = arg_list[i]
                v = args[i]
                m = ptn.match(v)
                if m:
                    k = m.group("key")
                    v = m.group("value")
                    params[k]=v
                    lib.log.debug( f"{pf}{k.ljust(key_max)} : {v}")
                else:
                    params[k]=v
                    lib.log.debug( f"{pf}{k.ljust(key_max)} : {v}")
            if "debug" in params:
                func(params)
            else:
                if "debugpy" in sys.modules:
                    params["debug"]=True
                else:
                    params["debug"]=False
            return params

        @staticmethod
        def __gen_list(value:str,cfg:dict)->list:
            sep = cfg.get("separator",os.pathsep)
            res = list(value.split(sep))
            return res
        @staticmethod
        def __set_args_value(args_cfg:dict,params:dict):

            for cfg_key,cfg_val in args_cfg.items():
                cfg_type = cfg_val.get("type","")
                prm_val  = params[cfg_key]
                match cfg_type:
                    case "text":
                        pass
                    case "list":
                        params[cfg_key] = lib.cmd_app.__gen_list(prm_val,cfg_val)
                        pass
                    case _:
                        pass

            return

        @staticmethod
        def start(name:str,func,args_cfg:dict,args:list=sys.argv,prefix:str="python > "):
            if name == "__main__":
                lib.cmd_app.__display_head(args,func,args_cfg,prefix)
                params = lib.cmd_app.__set_params(func,args_cfg,args,prefix)
                lib.cmd_app.__set_args_value(args_cfg,params)
                func(params)
    class markdown:
        @staticmethod
        def cnv(src:str, include_base_path=".")->str:

            md = markdown.Markdown(extensions=[
                lib.markdown.my_extension(),
                "admonition",
                "tables",
                "toc",
                "nl2br",
                "codehilite",
                "fenced_code",
                ChecklistExtension(),
                MarkdownInclude(configs={'base_path':include_base_path}),
                ]
                )
            res = md.convert(src)
            return res
        class my_preprocessor(markdown.preprocessors.Preprocessor):

            has_mermaid = False

            def run_lines(self, lines):
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
                if self.has_mermaid:
                    result_lines.append("")
                    result_lines.append("<script>mermaid.initialize({startOnLoad:true});</script>")
                    result_lines.append("")
                return result_lines
        class my_post_processor(markdown.postprocessors.Postprocessor):

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def run(self, html):
                result_html = html
                return result_html

        class my_extension(markdown.Extension):
            def extendMarkdown(self, md, md_globals=None):
                """ add extension instance. """
                md.preprocessors.register(lib.markdown.my_preprocessor(md), 'my_pre_proc', 35)
                #md.postprocessors.register(mul.markdown.my_preprocessor(md), 'my_post_proc', 50)
                md.registerExtension(self)

            def makeExtension(**kwargs):
                return lib.markdown.my_extension(**kwargs)
    def get_parent_dir(src:str)->str:
        """親ディレクトリ取得

        Parameters
        ----------
        src : str
            親ディレクトリを取得する元となるディレクトリ

        Returns
        -------
        str
            親ディレクトリのパス
        """
        p = pathlib.Path(src)
        res = str(p.parent)
        return res


    class jinja2:

        @staticmethod
        def __debug(text:str):
            """テンプレート処理中にデバッグ情報として標準出力を行います
            """
            lib.log.debug(text)
            return ""

        @staticmethod
        def convert(data:dict,template_path:str)->str:

            cur = os.getcwd()
            tmp_dir = os.path.dirname(template_path)
            os.chdir(tmp_dir)
            tmp_file = os.path.basename(template_path)

            loader         = jinja2.FileSystemLoader( searchpath=tmp_dir, encoding='utf-8')
            environment    = jinja2.Environment(loader=loader)
            environment.filters["debug"]=lib.jinja2.__debug

            try:
                template  = environment.get_template(name=tmp_file)
                out_text  = template.render(data)
            except jinja2.exceptions.UndefinedError as e:
                lib.log.debug( f"テンプレートへ入力しているデータをダンプします。")
                lib.log.debug(data)
                lib.log.debug(traceback.format_exc())
                lib.log.debug(e)
                sys.exit(1)
            except jinja2.exceptions.TemplateNotFound as e:
                lib.log.debug(traceback.format_exc())
                lib.log.debug(e)
                lib.log.debug( f"template_path : {template_path}")
                lib.log.debug( f"tmp_dir       : {tmp_dir}")
                lib.log.debug( f"tmp_file      : {tmp_file}")
                lib.log.debug( f"cur           : {cur} -> {os.getcwd()}")
                lib.log.debug( f"raise ファイル「{e}」が見つかりませんでした。")
                sys.exit(1)

            os.chdir(cur)

            return out_text