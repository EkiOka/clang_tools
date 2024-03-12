rem ================================================================================================
rem post configration path
rem ================================================================================================

rem ------------------------------------------------------------------------------------------------
rem system path configration
rem ------------------------------------------------------------------------------------------------

rem path
set "path=%clt_def_cmd_dir%;%path%"
set "path=%clt_cmd_dir%;%path%"

rem pythonpath
if "%pythonpath%"=="" (
    set "pythonpath=%clt_def_py_lib_dir%"
) else (
    set "pythonpath=%clt_def_py_lib_dir%;%pythonpath%"
)
set "pythonpath=%clt_py_lib_dir%;%pythonpath%"

rem ------------------------------------------------------------------------------------------------
rem default applocation configration
rem ------------------------------------------------------------------------------------------------
set "clt_text_editor_exe=%clt_sakura_exe%"
set "clt_make_exe=%clt_gnuwin32_make_exe%"
set "clt_grep_exe=%clt_grep_exe_for_git%"
set "clt_diff_exe=%clt_diff_exe_for_git%"
set "clt_diff3_exe=%clt_diff3_exe_for_git%"
set "clt_msbuild_exe=%clt_msbuild_exe_v4_0_64%"
rem ------------------------------------------------------------------------------------------------
rem make directory
rem ------------------------------------------------------------------------------------------------

rem output
md "%clt_out_dir%" > nul
md "%clt_tmp_dir%" > nul
md "%clt_doxygen_out_dir%" > nul

rem user directory
md "%clt_py_lib_dir%" > nul
md "%clt_cmd_dir%" > nul
md "%clt_term_cfg_dir%" > nul

exit /b 0
