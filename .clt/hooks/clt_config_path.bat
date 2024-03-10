rem ------------------------------------------------------------------------------------------------
rem パス設定
rem ------------------------------------------------------------------------------------------------

rem =============================================
rem CLT標準設定
rem =============================================

rem 設定ファイル格納先ディレクトリ
set "clt_def_cfg_dir=%clt_dir%\.clt\term_cfg"

rem コマンド格納先ディレクトリ
set "clt_def_cmd_dir=%clt_dir%\.clt\term_cmd"

rem pythonライブラリ格納先ディレクトリ
set "clt_def_py_lib_dir=%clt_dir%\.clt\py_lib"

rem =============================================
rem ユーザー別設定
rem =============================================
rem ユーザーが変更できる設定となります。clt_term_cfg_dirで指定されたファイルで環境変数を上書きしてください

rem ユーザー別ディレクトリ
set "clt_usr_dir=%clt_dir%\20_usr"

rem 設定ファイル格納先ディレクトリ
set "clt_cfg_dir=%clt_usr_dir%\cfg"

rem vscodeのTerminal設定ファイル格納先ディレクトリ
set "clt_term_cfg_dir=%clt_usr_dir%\cfg\term"

rem vscodeのTerminal設定ファイル
set "clt_term_cfg_path=%clt_term_cfg_dir%\clt_config_path.bat"

rem vscodeのTerminal設定ファイル実行後バッチファイル
set "clt_term_cfg_path_post=%clt_term_cfg_dir%\clt_config_path_post.bat"

rem コマンド格納先ディレクトリ
set "clt_cmd_dir=%clt_usr_dir%\cmd"

rem pythonライブラリ格納先ディレクトリ
set "clt_py_lib_dir=%clt_usr_dir%\py_lib"

rem =============================================
rem 共通設定
rem =============================================

rem 出力ルートディレクトリ
set "clt_out_dir=%clt_dir%\10_out\out"

rem 一時出力ルートディレクトリ
set "clt_tmp_dir=%clt_dir%\10_out\tmp"

rem Doxygen出力ファイル格納ルートディレクトリ
set "clt_doxygen_out_dir=%clt_tmp_dir%\Doxygen"

rem ------------------------------------------------------------------------------------------------
rem application path
rem ------------------------------------------------------------------------------------------------
rem 使用するアプリケーションパスを設定します。基本的にインストーラーを使用した場合のデフォルト設定となっているため
rem インストール時に変更している場合はclt_term_cfg_dirで指定されているファイルで環境変数を上書きしてください

rem =============================================
rem Doxygen
rem =============================================

rem Doxygenインストール先ディレクトリ
set "clt_doxygen_install=%ProgramFiles%\doxygen"

rem Doxygenの実行ファイルパス
set "clt_doxygen_exe=%clt_doxygen_install%\bin\doxygen.exe"

rem DoxyWizardの実行ファイルパス
set "clt_doxywizard_exe=%clt_doxygen_install%\bin\doxywizard.exe"

rem =============================================
rem GnuWin32
rem =============================================

rem GnuWin32インストール先ディレクトリ
set "clt_gnuwin32_install_dir=%ProgramFiles(x86)%\GnuWin32"

rem make(GnuWin32)の実行ファイルパス
set "clt_gnuwin32_make_exe=%clt_gnuwin32_install_dir%\bin\make.exe"

rem =============================================
rem Git
rem =============================================

rem Gitインストールディレクトリ
set "clt_git_install=%ProgramFiles%\Git"

rem Gitの実行ファイルパス
set "clt_git_exe=%clt_git_install%\bin\git.exe"

rem Grepの実行ファイルパス(Git添付のもの)
set "clt_grep_exe_for_git=%clt_git_install%\usr\bin\grep.exe"

rem diffの実行ファイルパス(Git添付のもの)
set "clt_diff_exe_for_git=%clt_git_install%\usr\bin\diff.exe"

rem diff3の実行ファイルパス(Git添付のもの)
set "clt_diff3_exe_for_git=%clt_git_install%\usr\bin\diff3.exe"

rem =============================================
rem Graphviz
rem =============================================

rem Graphvizインストールディレクトリ
set "clt_graphviz_install=%ProgramFiles%\Graphviz"

rem Graphvizの実行ファイルパス(dox.exe)
set "clt_dot_exe=%clt_graphviz_install%\bin\dot.exe"

rem =============================================
rem LLVM
rem =============================================

rem LLVMインストールディレクトリ
set "clt_llvm_install=%ProgramFiles%\LLVM"

rem LLVMの実行ファイルパス(clang.exe)
set "clt_clang_exe=%clt_llvm_install%\clang.exe"

rem LLVMの実行ファイルパス(clang++.exe)
set "clt_clangpp_exe=%clt_llvm_install%\clang++.exe"

rem WinMargeインストールディレクトリ
set "clt_winmarge_install=%ProgramFiles%\WinMerge"

rem =============================================
rem WinMarge
rem =============================================

rem WinMarge実行パス
set "clt_winmarge_exe=%clt_winmarge_install%\WinMergeU.exe"

rem =============================================
rem MsBuild
rem =============================================

rem MsBuildの実行ファイルパス
set "clt_msbuild_exe_v2_0=%SystemRoot%Microsoft.NET\Framework\v2.0.50727\MSBuild.exe"

rem MsBuildの実行ファイルパス
set "clt_msbuild_exe_v3_5=%SystemRoot%Microsoft.NET\Framework\v3.5\MSBuild.exe"

rem MsBuildの実行ファイルパス
set "clt_msbuild_exe_v4_0=%SystemRoot%Microsoft.NET\Framework\v4.0.30319\MSBuild.exe"

rem MsBuildの実行ファイルパス
set "clt_msbuild_exe_v2_0_64=%SystemRoot%Microsoft.NET\Framework64\v2.0.50727\MSBuild.exe"

rem MsBuildの実行ファイルパス
set "clt_msbuild_exe_v3_5_64=%SystemRoot%Microsoft.NET\Framework64\v3.5\MSBuild.exe"

rem MsBuildの実行ファイルパス
set "clt_msbuild_exe_v4_0_64=%SystemRoot%Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe"

rem =============================================
rem Text Editor
rem =============================================

rem メモ帳の実行ファイルパス
set "clt_notepad_exe=%SystemRoot%\system32\notepad.exe"

rem サクラエディタインストールパス
set "clt_sakura_install=%ProgramFiles(x86)%\sakura"

rem サクラエディタ実行パス
set "clt_sakura_exe=%clt_sakura_install%sakura.exe"

rem ------------------------------------------------------------------------------------------------
exit /b 0
