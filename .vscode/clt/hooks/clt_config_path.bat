rem ================================================================================================
rem configration path
rem ================================================================================================
rem If necessary, overwrite the file specified in clt_term_cfg_dir.

rem ------------------------------------------------------------------------------------------------
rem CLT standard path
rem ------------------------------------------------------------------------------------------------
set "clt_def_cfg_dir=%clt_dir%\.vscode\clt\term_cfg"
set "clt_def_cmd_dir=%clt_dir%\.vscode\clt\term_cmd"
set "clt_codes_dir=%clt_dir%\.vscode\clt\dev\codes"
set "clt_out_dir=%clt_dir%\10_out\out"
set "clt_tmp_dir=%clt_dir%\10_out\tmp"
set "clt_doxygen_out_dir=%clt_tmp_dir%\Doxygen"

rem ------------------------------------------------------------------------------------------------
rem user configration path
rem ------------------------------------------------------------------------------------------------
set "clt_usr_dir=%clt_dir%\20_usr"
set "clt_cfg_dir=%clt_usr_dir%\cfg"
set "clt_term_cfg_dir=%clt_usr_dir%\cfg\term"
set "clt_term_cfg_path=%clt_term_cfg_dir%\clt_config_path.bat"
set "clt_term_cfg_path_post=%clt_term_cfg_dir%\clt_config_path_post.bat"
set "clt_cmd_dir=%clt_usr_dir%\cmd"

rem ------------------------------------------------------------------------------------------------
rem application path
rem ------------------------------------------------------------------------------------------------

rem Doxygen
set "clt_doxygen_install=%ProgramFiles%\doxygen"
set "clt_doxygen_exe=%clt_doxygen_install%\bin\doxygen.exe"
set "clt_doxywizard_exe=%clt_doxygen_install%\bin\doxywizard.exe"

rem GnuWin32
set "clt_gnuwin32_install_dir=%ProgramFiles(x86)%\GnuWin32"
set "clt_gnuwin32_make_exe=%clt_gnuwin32_install_dir%\bin\make.exe"

rem Git
set "clt_git_install=%ProgramFiles%\Git"
set "clt_git_exe=%clt_git_install%\bin\git.exe"
set "clt_grep_exe_for_git=%clt_git_install%\usr\bin\grep.exe"
set "clt_diff_exe_for_git=%clt_git_install%\usr\bin\diff.exe"
set "clt_diff3_exe_for_git=%clt_git_install%\usr\bin\diff3.exe"

rem Graphviz
set "clt_graphviz_install=%ProgramFiles%\Graphviz"
set "clt_dot_exe=%clt_graphviz_install%\bin\dot.exe"

rem LLVM
set "clt_llvm_install=%ProgramFiles%\LLVM"
set "clt_clang_exe=%clt_llvm_install%\clang.exe"
set "clt_clangpp_exe=%clt_llvm_install%\clang++.exe"
set "clt_winmarge_install=%ProgramFiles%\WinMerge"

rem WinMarge
set "clt_winmarge_exe=%clt_winmarge_install%\WinMergeU.exe"

rem MsBuild
set "clt_msbuild_exe_v2_0=%SystemRoot%Microsoft.NET\Framework\v2.0.50727\MSBuild.exe"
set "clt_msbuild_exe_v3_5=%SystemRoot%Microsoft.NET\Framework\v3.5\MSBuild.exe"
set "clt_msbuild_exe_v4_0=%SystemRoot%Microsoft.NET\Framework\v4.0.30319\MSBuild.exe"
set "clt_msbuild_exe_v2_0_64=%SystemRoot%Microsoft.NET\Framework64\v2.0.50727\MSBuild.exe"
set "clt_msbuild_exe_v3_5_64=%SystemRoot%Microsoft.NET\Framework64\v3.5\MSBuild.exe"
set "clt_msbuild_exe_v4_0_64=%SystemRoot%Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe"

rem Text Editor
set "clt_notepad_exe=%SystemRoot%\system32\notepad.exe"
set "clt_sakura_install=%ProgramFiles(x86)%\sakura"
set "clt_sakura_exe=%clt_sakura_install%sakura.exe"

rem ------------------------------------------------------------------------------------------------
exit /b 0
