import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl

class cmd(cab.cmd_app):
    pass

def __main(s:cmd):

    #---------------------------------------------------------------------
    # リスト読出
    #---------------------------------------------------------------------
    upl = pl.user_path_list()
    epl = pl.env_path_list()

    #---------------------------------------------------------------------
    # 環境パス取得
    #---------------------------------------------------------------------
    dir_base = epl["dir_base"]
    dir_user = epl["dir_user"]
    dir_tmp  = epl["dir_tmp"]
    dir_out  = epl["dir_out"]

    dir_tmp_mk = epl["dir_tmp_mk"]

    dir_tmp_filelist = epl["dir_tmp_filelist"]
    dir_out_filelist = epl["dir_out_filelist"]

    dir_user_notes     = epl["dir_user_notes"]
    dir_user_cfg       = epl["dir_user_cfg"]
    dir_user_tmpl_note = epl["dir_user_tmpl_note"]

    dir_user_template = epl["dir_user_template"]

    #---------------------------------------------------------------------
    # アプリケーションパス設定
    #---------------------------------------------------------------------
    # 初期値はデフォルトインストールパス
    add_application("doxygen_exe", r"C:\Program Files\doxygen\bin\doxygen.exe" ,upl)
    add_application("dot_exe",     r"C:\Program Files\Git\bin\git.exe" ,upl)
    add_application("git_exe",     r"C:\Program Files\Graphviz\bin\dot.exe" ,upl)
    add_application("java_exe",    r"C:\Program Files (x86)\Java\jre-1.8\bin\java.exe" ,upl)
    add_application("sakura_exe",  r"C:\Program Files (x86)\sakura\sakura.exe" ,upl)
    add_application("ea_exe",      r"C:\Program Files (x86)\SparxSystems Japan\EA\EA.exe" ,upl)
    add_application("make_exe",    r"C:\Program Files (x86)\GnuWin32\bin\make.exe" ,upl)

    #---------------------------------------------------------------------
    # notes関係パス設定
    #---------------------------------------------------------------------

    upl["mask_user_notes"]=f"{dir_user_notes}\\**\\*.md"
    upl["file_user_note_css"]=f"{dir_user_notes}\\markdown.css"
    upl["file_user_note_cfg"]=f"{dir_user_cfg}\\note_common.yml"
    upl["file_user_note_tmpl"]=f"{dir_user_tmpl_note}\\note.html"

    # makefile
    upl["file_user_note_mk"]  = f"{dir_user_template}\\mk\\note.mk"
    upl["file_tmp_note_mk"  ] = f"{dir_tmp_mk}\\note.mk"

    #---------------------------------------------------------------------
    # リスト更新
    #---------------------------------------------------------------------
    pl.update_user_path(upl)
    return

def add_application(key:str,value:str,dest:dict):
    if a.is_exist(value):
        dest[key] = value

app = cmd("2990fc3bc3304ab68c0af04edf7e6fdb")
app.reg_main(__main)
app.start()
