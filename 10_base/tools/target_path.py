"""ターゲットパス初期化

doxygenなどで解析する対象のユーザーパスを変更します。
基本的に上書き・追加動作となります。

アクション：
    既存のパス　　　　　　　　　　：上書きされます
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
    try:
        #---------------------------------------------------------------------
        # 環境パス取得
        #---------------------------------------------------------------------

        dir_base          = upl["dir_base"]
        dir_user          = upl["dir_user"]
        dir_tmp           = upl["dir_tmp"]
        dir_out           = upl["dir_out"]
        dir_tmpl          = upl["dir_tmpl"]
        dir_tmpl_mk       = upl["dir_tmpl_mk"]
        dir_tmp_mk        = upl["dir_tmp_mk"]
        dir_cfg           = upl["dir_cfg"]
        dir_tmp_filelist  = upl["dir_tmp_filelist"]
        dir_out_filelist  = upl["dir_out_filelist"]

        dis_vars = [ k for k in locals().keys() ]

        #---------------------------------------------------------------------
        # ターゲットルートパス
        #---------------------------------------------------------------------

        # 解析対象のターゲットソフトのパス設定
        dir_target = f"{dir_user}\\src"

        #---------------------------------------------------------------------
        # マスク
        #---------------------------------------------------------------------

        # ファイルリスト生成用のマスク設定
        c_masks   = f"{dir_target}\\**\\*.c"
        h_masks   = f"{dir_target}\\**\\*.h"
        cpp_masks = f"{dir_target}\\**\\*.cpp"

        masks_target_src = [c_masks,h_masks,cpp_masks]
        masks_target_c   = c_masks
        masks_target_h   = h_masks
        masks_target_cpp = cpp_masks

        #---------------------------------------------------------------------
        # ファイルリスト
        #---------------------------------------------------------------------

        # ファイルリストの生成先設定
        file_tmp_file_list_target_src = f"{dir_tmp_filelist}\\target_src.json"
        file_tmp_file_list_target_c   = f"{dir_tmp_filelist}\\target_c.json"
        file_tmp_file_list_target_h   = f"{dir_tmp_filelist}\\target_h.json"
        file_tmp_file_list_target_cpp = f"{dir_tmp_filelist}\\target_cpp.json"
        file_tmp_file_list_target_inc = f"{dir_tmp_filelist}\\target_inc.json"

        # 更新チェック可能なファイルリストの生成先設定
        file_out_file_list_target_src = f"{dir_out_filelist}\\target_src.json"
        file_out_file_list_target_c   = f"{dir_out_filelist}\\target_c.json"
        file_out_file_list_target_h   = f"{dir_out_filelist}\\target_h.json"
        file_out_file_list_target_cpp = f"{dir_out_filelist}\\target_cpp.json"
        file_out_file_list_target_inc = f"{dir_out_filelist}\\target_inc.json"

        #---------------------------------------------------------------------
        # makefile
        #---------------------------------------------------------------------

        # ファイルリストのmakefile
        file_tmpl_target_mk = f"{dir_tmpl_mk}\\target.mk"
        file_tmp_target_mk  = f"{dir_tmp_mk}\\target.mk"

        # doxygenのmakefile
        file_tmpl_doxygen_mk    = f"{dir_tmpl_mk}\\doxygen.mk"
        file_tmp_doxygen_mk     = f"{dir_tmp_mk}\\doxygen.mk"
        file_tmpl_doxygen_p1_mk = f"{dir_tmpl_mk}\\doxygen_phase1.mk"
        file_tmp_doxygen_p1_mk  = f"{dir_tmp_mk}\\doxygen_phase1.mk"
        file_tmpl_doxygen_p2_mk = f"{dir_tmpl_mk}\\doxygen_phase2.mk"
        file_tmp_doxygen_p2_mk  = f"{dir_tmp_mk}\\doxygen_phase2.mk"
        #---------------------------------------------------------------------
        # report
        #---------------------------------------------------------------------
        file_report = f"{dir_cfg}\\report.yml"

        #---------------------------------------------------------------------
        # dir_ file_ mask_ の接頭辞のローカル変数をuplに格納
        #---------------------------------------------------------------------
        for k, v in locals().items():
            if k in dis_vars:
                pass
            else:
                if k.find("file_") == 0:
                    upl[k]=v
                elif k.find("dir_") == 0:
                    upl[k]=v
                elif k.find("mask_") == 0:
                    upl[k]=v
                elif k.find("masks_") == 0:
                    upl[k]=v

        #---------------------------------------------------------------------
        # リスト更新
        #---------------------------------------------------------------------
        pl.update_user_path(upl)
    except KeyError as e:
        a.log_error("以下のキーが見つかりませんでした。")
        for k in e.args:
            a.log_error(k)
        pass
    except Exception as e:
        a.log_error(e)
        pass

    return

app = cmd("8ed072c7d5644e609538a725280da9ec")
app.reg_main(__main)
app.start()
