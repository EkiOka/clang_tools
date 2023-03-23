import xml.etree.ElementTree as ET
import yaml
import codecs
import json
import glob
import re
import sys
import os

class lib:
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
        def save(path: str,data):
            """ jsonファイルとしてデータを保存する
            """
            enc = "utf-8"
            ensure_ascii=False
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
                yaml.dump(obj,f,default_flow_style=False)
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
            print(f"{pf}---------------------------------------------------")
            print(f"{pf}{args[0]}")
            print(f"{pf}---------------------------------------------------")
            print(f"{pf}cur_dir  : {os.getcwd()}")
            print(f"{pf}sys.argv : {args}")
            print(f"{pf}args_cfg : {args_cfg}")

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
                    print( f"{pf}{k.ljust(key_max)} : {v}")
                else:
                    params[k]=v
                    print( f"{pf}{k.ljust(key_max)} : {v}")
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
