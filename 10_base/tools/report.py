import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl


class cmd_rpt(cab.cmd_app):

    cur_checker_name: str
    cur_file_name: str
    cur_func_name: str
    cur_var_name: str

    def gen_report(s):
        file_report = pl.get_user_path("file_report")
        rpt = dict()
        try:
            rpt = a.load_yaml(file_report)
        except:
            rpt = dict()

        # ============================================
        # doxygen
        # ============================================
        s.cur_checker_name = "doxygen"
        checker_report = rpt.get(s.cur_checker_name, {})
        rpt[s.cur_checker_name] = checker_report

        file_tmp_dxy_rpt = pl.get_user_path("file_tmp_dxy_rpt")
        dir_out_dxy_yml = pl.get_user_path("dir_out_dxy_yml")
        dox_yml_files = a.get_file_list(f"{dir_out_dxy_yml}\\*.yml")
        for file in dox_yml_files:
            yml_data = a.load_yaml(file)
            for k, v in yml_data.items():
                s.cur_file_name = k
                dest_file = checker_report.get(k,{})
                checker_report[k] = dest_file
                s.check_doxygen_file(v,dest_file)
                pass
        a.save_yaml(file_tmp_dxy_rpt,rpt)
        return

    def check_doxygen_file(s, src: dict,dest:dict):
        functions = src.get("functions")
        variables = src.get("variables")
        includes  = src.get("includes")

        for item in functions:
            s.check_doxygen_func(item,dest)
        for item in variables:
            s.check_doxygen_var(item,dest)
        for item in includes:
            s.check_doxygen_inc(item,dest)

        return

    def check_doxygen_func(s, src: dict,dest:dict):
        name = src.get("name","")
        dest_func = dest.get(name,{})
        dest[name] = dest_func
        s.check_identifier_len(name,"関数名",dest_func)
        return
    def check_doxygen_var(s, src: dict,dest:dict):
        name = src.get("name","")
        dest_var = dest.get(name,{})
        dest[name] = dest_var
        s.check_identifier_len(name,"変数名",dest_var)
        return
    def check_doxygen_inc(s, src: dict,dest:dict):
        return

    def check_identifier_len(s,src:str,src_type:str,dest:dict):
        """識別子31文字制限確認"""
        id = "CCI_0E1246EF705F4F138F0B705371A4132D"
        res = True
        id_dest = dest.get(id,{})
        dest[id]=id_dest
        if len(src)>31:
            res = False
            id_dest["msg"]=f"{src_type}は最大識別子長31を超えています(length={len(src)})"
        id_dest["result"]=res
        return
 
         

def __main(s: cmd_rpt):
    s.gen_report()
    return


app = cmd_rpt("d69588ae140b47bebe5f00372b7be53c")
app.reg_main(__main)
app.start()
