"""ユーザパス初期化

ユーザーの依存のパスを取得します。
本ファイルはユーザーの環境に合わせて書き換えが可能です。

アプリケーションが呼び出された場合ユーザーパスを書き換えますが、
既に存在するパスは書き換えられません。

その場合はパスリストを更新するようにしてください。

アクション：
    既存のパス　　　　　　　　　　：書き換えられません
    リビジョン違いの追加のパス　　：追加されます
    リビジョン違いで削除されたパス：そのままとなります。
"""
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

    #---------------------------------------------------------------------
    # 環境パス取得
    #---------------------------------------------------------------------
    ws = a.get_cur_dir()

    dir_base = upl["dir_base"]
    dir_user = upl["dir_user"]
    dir_tmp  = upl.get("dir_tmp",f"{ws}\\50_out_tmp")
    dir_out  = upl.get("dir_out",f"{ws}\\60_out")

    dir_cfg       = upl.get("dir_cfg",f"{dir_user}\\cfg")
    dir_src       = upl.get("dir_src",f"{dir_user}\\src")
    dir_tmpl      = upl.get("dir_tmpl",f"{dir_user}\\template")

    #---------------------------------------------------------------------
    # ファイルリストパス関係
    #---------------------------------------------------------------------
    dir_tmp_filelist = upl.get("dir_tmp_filelist",f"{dir_tmp}\\filelist")
    dir_out_filelist = upl.get("dir_out_filelist",f"{dir_out}\\filelist")

    #---------------------------------------------------------------------
    # makefileパス関係
    #---------------------------------------------------------------------
    dir_tmp_mk  = upl.get("dir_tmp_mk",  f"{dir_tmp}\\mk")
    dir_out_mk  = upl.get("dir_out_mk",  f"{dir_out}\\mk")
    dir_tmpl_mk = upl.get("dir_tmpl_mk", f"{dir_tmpl}\\mk")

    #---------------------------------------------------------------------
    # doxygenのoutput関係パス設定
    #---------------------------------------------------------------------
    dir_tmpl_dxy     = upl.get("dir_tmpl_dxy",    f"{dir_tmpl}\\doxygen")
    file_tmpl_dxy    = upl.get("file_tmpl_dxy",   f"{dir_tmpl_dxy}\\Doxyfile")
    file_tmpl_dxy_mk = upl.get("file_tmpl_dxy_mk",f"{dir_tmpl_mk}\\doxygen.mk")

    dir_tmp_dxy     = upl.get("dir_tmp_dxy",       f"{dir_tmp}\\doxygen")
    dir_tmp_dxy_mk  = upl.get("dir_tmp_dxy_mk",    f"{dir_tmp_dxy}\\mk")
    dir_tmp_dxy_res = upl.get("dir_tmp_dxy_res",   f"{dir_tmp_dxy}\\result")
    dir_tmp_dxy_xml = upl.get("dir_tmp_dxy_xml",   f"{dir_tmp_dxy}\\xml")
    dir_tmp_dxy_yml = upl.get("dir_tmp_dxy_yml",   f"{dir_tmp_dxy}\\yml")
    dir_tmp_dxy_html = upl.get("dir_tmp_dxy_html", f"{dir_tmp_dxy}\\html")

    dir_out_dxy     = upl.get("dir_out_dxy",       f"{dir_out}\\doxygen")
    dir_out_dxy_mk  = upl.get("dir_out_dxy_mk",    f"{dir_out_dxy}\\mk")
    dir_out_dxy_res = upl.get("dir_out_dxy_res",   f"{dir_out_dxy}\\result")
    dir_out_dxy_xml = upl.get("dir_out_dxy_xml",   f"{dir_out_dxy}\\xml")
    dir_out_dxy_yml = upl.get("dir_out_dxy_yml",   f"{dir_out_dxy}\\yml")
    dir_out_dxy_html = upl.get("dir_out_dxy_html", f"{dir_out_dxy}\\html")

    mask_tmp_dxy_xml_files  = upl.get("mask_tmp_dxy_xml_files",f"{dir_tmp_dxy_xml}\\**\\*_8c.xml")
    mask_out_dxy_xml_files  = upl.get("mask_out_dxy_xml_files",f"{dir_out_dxy_xml}\\**\\*_8c.xml")

    file_cfg_doxygen  = upl.get("file_cfg_doxygen",  f"{dir_cfg}\\doxygen.yml")

    file_tmp_doxyfile = upl.get("file_tmp_doxyfile", f"{dir_tmp_dxy}\\Doxyfile")
    file_out_doxyfile = upl.get("file_out_doxyfile", f"{dir_out_dxy}\\Doxyfile")

    file_tmp_dxy_mk   = upl.get("file_tmp_dxy_mk",   f"{dir_tmp_mk}\\doxygen.mk")
    file_out_dxy_mk   = upl.get("file_out_dxy_mk",   f"{dir_out_mk}\\doxygen.mk")

    file_tmp_dxy_log  = upl.get("file_tmp_dxy_log",   f"{dir_tmp_dxy}\\doxygen.log")
    file_out_dxy_log  = upl.get("file_out_dxy_log",   f"{dir_out_dxy}\\doxygen.log")

    file_tmp_dxy_rpt  = upl.get("file_tmp_dxy_rpt",   f"{dir_tmp_dxy}\\doxygen_rpt.yml")
    file_out_dxy_rpt  = upl.get("file_out_dxy_rpt",   f"{dir_out_dxy}\\doxygen_rpt.yml")

    #---------------------------------------------------------------------
    # notes関係パス設定
    #---------------------------------------------------------------------

    dir_notes     = upl.get("dir_notes",     f"{dir_user}\\notes")
    dir_tmpl_note = upl.get("dir_tmpl_note", f"{dir_tmpl}\\notes")    
    dir_tmp_notes = upl.get("dir_tmp_notes", f"{dir_tmp}\\notes")
    dir_out_notes = upl.get("dir_out_notes", f"{dir_out}\\notes")

    mask_notes     = upl.get("mask_notes",     f"{dir_notes}\\**\\*.md")
    file_note_cfg  = upl.get("file_note_cfg",  f"{dir_cfg}\\note_common.yml")
    file_note_tmpl = upl.get("file_note_tmpl", f"{dir_tmpl_note}\\note.html")
    file_note_css  = upl.get("file_note_css",  f"{dir_tmpl_note}\\markdown.css")

    # makefile
    file_note_mk     = upl.get("file_note_mk",     f"{dir_tmpl_mk}\\note.mk")
    file_tmp_note_mk = upl.get("file_tmp_note_mk", f"{dir_tmp_mk}\\note.mk")
    file_out_note_mk = upl.get("file_out_note_mk", f"{dir_out_mk}\\note.mk")

    #---------------------------------------------------------------------
    # dir_ file_ mask_ の接頭辞のローカル変数をuplに格納
    #---------------------------------------------------------------------
    for k, v in locals().items():
        if k.find("file_") == 0:
            upl[k]=v
        elif k.find("dir_") == 0:
            upl[k]=v
        elif k.find("mask_") == 0:
            upl[k]=v

    #---------------------------------------------------------------------
    # アプリケーションパス自動設定
    #---------------------------------------------------------------------
    # 初期値はデフォルトインストールパス
    # デフォルト以外は特に検索して設定するつもりはない。
    # スタートメニューのショートカット抜き出せばうまくいくかも？
    # (レジストリは構造複雑すぎて当てにしてない)
    add_application("exe_doxygen", r"C:\Program Files\doxygen\bin\doxygen.exe" ,upl)
    add_application("exe_dot",     r"C:\Program Files\Git\bin\git.exe" ,upl)
    add_application("exe_git",     r"C:\Program Files\Graphviz\bin\dot.exe" ,upl)
    add_application("exe_java",    r"C:\Program Files (x86)\Java\jre-1.8\bin\java.exe" ,upl)
    add_application("exe_sakura",  r"C:\Program Files (x86)\sakura\sakura.exe" ,upl)
    add_application("exe_ea",      r"C:\Program Files (x86)\SparxSystems Japan\EA\EA.exe" ,upl)
    add_application("exe_make",    r"C:\Program Files (x86)\GnuWin32\bin\make.exe" ,upl)
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
