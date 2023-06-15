import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl

class cmd(cab.cmd_app):
    pass

def __main(s:cmd):
    # リストの読み出し
    upl = pl.user_path_list()
    epl = pl.env_path_list()

    # ワークスペース内の基本となるディレクトリ
    # ユーザー固有の入出力を設定する場合に使用してください。
    dir_base = epl["dir_base"]
    dir_user = epl["dir_user"]
    dir_tmp  = epl["dir_tmp"]
    dir_out  = epl["dir_out"]

    # ファイルリストの出力先
    dir_tmp_filelist = epl["dir_tmp_filelist"]
    dir_out_filelist = epl["dir_out_filelist"]

    # アプリケーションパス設定(初期値はデフォルトインストールパス)
    doxygen_exe = r"C:\Program Files\doxygen\bin\doxygen.exe"
    if a.is_exist(doxygen_exe):
        upl["doxygen_exe"] = doxygen_exe
    git_exe = r"C:\Program Files\Git\bin\git.exe"
    if a.is_exist(git_exe):
        upl["git_exe"] = git_exe
    dot_exe = r"C:\Program Files\Graphviz\bin\dot.exe"
    if a.is_exist(dot_exe):
        upl["dot_exe"] = dot_exe
    java_exe_for_jre_18 = r"C:\Program Files (x86)\Java\jre-1.8\bin\java.exe"
    if a.is_exist(java_exe_for_jre_18):
        upl["java_exe"] = java_exe_for_jre_18
    sakura_exe = r"C:\Program Files (x86)\sakura\sakura.exe"
    if a.is_exist(sakura_exe):
        upl["sakura_exe"] = sakura_exe
    ea_exe = r"C:\Program Files (x86)\SparxSystems Japan\EA\EA.exe"
    if a.is_exist(ea_exe):
        upl["ea_exe"] = ea_exe
    make_exe = r"C:\Program Files (x86)\GnuWin32\bin\make.exe"
    if a.is_exist(make_exe):
        upl["make_exe"] = make_exe

    # リストの更新
    pl.update_user_path(upl)
    return

app = cmd("2990fc3bc3304ab68c0af04edf7e6fdb")
app.reg_main(__main)
app.start()
