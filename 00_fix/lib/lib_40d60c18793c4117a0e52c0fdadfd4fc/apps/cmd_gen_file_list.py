import os
import sys
import glob
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a

class cmd_gen_file_list(cab.cmd_app):

    def __globs(s,mask,recursive=True,sep=os.sep):
        res = list()

        if type(mask) is list:
            for m in mask:
                g = glob.glob(m,recursive=recursive)
                res.extend(g)
        else:
            g = glob.glob(mask,recursive=recursive)
            res.extend(g)
        res = [str(item).replace("\\",sep).replace("/",sep) for item in set(res)]
        return res
    def get_files(s,enable_masks:list[str],disable_masks:list[str]=[],recursive=True)->list:
        enables = s.__globs(enable_masks,recursive)
        disables = s.__globs(disable_masks,recursive)
        res = list(set(enables) - set(disables))
        return res

    @staticmethod
    def start_gen_file_list(is_test:bool=False):
        app = None
        if is_test:
            raise Exception("未対応")
        else:
            app = cmd_gen_file_list("543857fbceb54ca3b59153ecfe73d6d2",sys.argv)
        app.add_param_cfg_text("src_ena_masks")
        app.add_param_cfg_text("src_dis_masks")
        app.add_param_cfg_text("dest_path")
        app.reg_main(gen_file_list)
        app.start()
    @staticmethod
    def start_gen_file_list_name(is_test:bool=False):
        app = None
        if is_test:
            raise Exception("未対応")
        else:
            app = cmd_gen_file_list("56dea2e76f224d1098e8630766ce3d2b",sys.argv)
        app.add_param_cfg_path_name("src_ena_masks")
        app.add_param_cfg_path_name("src_dis_masks")
        app.add_param_cfg_path_name("dest_name")
        app.reg_main(gen_file_list_name)
        app.start()

def gen_file_list(s:cmd_gen_file_list, src_ena_masks:list,src_dis_masks:list, dest_path:str):
    func = a.cur_function_name()
    a.log_info(f"{func} > src_ena_masks:{src_ena_masks}")
    a.log_info(f"{func} > src_dis_masks:{src_dis_masks}")
    a.log_info(f"{func} > dest_path:{dest_path}")
    files = s.get_files(src_ena_masks,src_dis_masks)
    a.save_json(dest_path,files)

def gen_file_list_name(s:cmd_gen_file_list, src_ena_masks:str,src_dis_masks:str, dest_name:str):
    func = a.cur_function_name()
    a.log_info(f"{func} > src_ena_masks:{src_ena_masks}")
    a.log_info(f"{func} > src_dis_masks:{src_dis_masks}")
    a.log_info(f"{func} > dest_name:{dest_name}")
    gen_file_list(s,src_ena_masks,src_dis_masks,dest_name)
