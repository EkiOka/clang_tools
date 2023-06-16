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
    dir_user_template = epl["dir_user_template"]
    dir_tmp_mk = epl["dir_tmp_mk"]

    # ファイルリストの出力先
    dir_tmp_filelist = epl["dir_tmp_filelist"]
    dir_out_filelist = epl["dir_out_filelist"]

    # 解析対象のターゲットソフトのパス設定
    target = f"{dir_user}\\src"

    # ファイルリスト生成用のマスク設定
    c_masks   = f"{target}\\**\\*.c"
    h_masks   = f"{target}\\**\\*.h"
    cpp_masks = f"{target}\\**\\*.cpp"

    upl["masks_target_src" ] = [c_masks,h_masks,cpp_masks]
    upl["masks_target_c"   ] = c_masks
    upl["masks_target_h"   ] = h_masks
    upl["masks_target_cpp" ] = cpp_masks

    # ファイルリストの生成先設定
    upl["file_tmp_file_list_target_src" ] = f"{dir_tmp_filelist}\\target_src.json"
    upl["file_tmp_file_list_target_c"   ] = f"{dir_tmp_filelist}\\target_c.json"
    upl["file_tmp_file_list_target_h"   ] = f"{dir_tmp_filelist}\\target_h.json"
    upl["file_tmp_file_list_target_cpp" ] = f"{dir_tmp_filelist}\\target_cpp.json"
    upl["file_tmp_file_list_target_inc" ] = f"{dir_tmp_filelist}\\target_inc.json"

    # 更新チェック可能なファイルリストの生成先設定
    upl["file_out_file_list_target_src" ] = f"{dir_out_filelist}\\target_src.json"
    upl["file_out_file_list_target_c"   ] = f"{dir_out_filelist}\\target_c.json"
    upl["file_out_file_list_target_h"   ] = f"{dir_out_filelist}\\target_h.json"
    upl["file_out_file_list_target_cpp" ] = f"{dir_out_filelist}\\target_cpp.json"
    upl["file_out_file_list_target_inc" ] = f"{dir_out_filelist}\\target_inc.json"

    # ファイルリストのmakefile
    upl["file_tmpl_target_mk" ] = f"{dir_user_template}\\mk\\target.mk"
    upl["file_tmp_target_mk"  ] = f"{dir_tmp_mk}\\target.mk"

    # リストの更新
    pl.update_user_path(upl)
    return

app = cmd("8ed072c7d5644e609538a725280da9ec")
app.reg_main(__main)
app.start()
