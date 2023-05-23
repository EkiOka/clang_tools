@echo off

chcp 65001 > nul

set "proc_name=%~nx0"

echo %proc_name% ^> =========================================================
echo %proc_name% ^>  clt(clang_tools) configration
echo %proc_name% ^> =========================================================

set "cur_bat_dir=%~dp0"
set "cur_bat_dir=%cur_bat_dir:~,-1%"
set "env_id=07ef773770c9448785a425e3ad32f298"

echo %proc_name% ^> cur_bat_dir : %cur_bat_dir%
echo %proc_name% ^> env_id      : %env_id%
echo %proc_name% ^> ---------------------------------------------------------
echo %proc_name% ^>  configration / clt_basic
echo %proc_name% ^> ---------------------------------------------------------

set "clt_root_dir=%cd%"
set "clt_tools_dir=%clt_root_dir%\00_fix\tools"
set "clt_lib_dir=%clt_root_dir%\00_fix\lib"
set "clt_cmd_dir=%clt_root_dir%\00_fix\cmd"

set "path=%clt_cmd_dir%;%path%"
set "pythonpath=%clt_lib_dir%"

echo %proc_name% ^> clt_root_dir  : %clt_root_dir%
echo %proc_name% ^> clt_tools_dir : %clt_tools_dir%
echo %proc_name% ^> clt_lib_dir   : %clt_lib_dir%
echo %proc_name% ^> clt_cmd_dir   : %clt_cmd_dir%
echo %proc_name% ^> pythonpath    : %pythonpath%
echo %proc_name% ^> ---------------------------------------------------------

py "%clt_tools_dir%\init.py"

cmd /k


set "clt_base_dir=%clt_root_dir%\10_base"
set "clt_user_dir=%clt_root_dir%\20_user"
set "clt_out_tmp=%clt_root_dir%\50_out_tmp"
set "clt_out_dir=%clt_root_dir%\60_out_tmp"


set "clt_base_cfg_dir=%clt_base_dir%\cfg"
set "clt_base_cfg_path_file=%clt_base_cfg_dir%\set_path.bat"

set "clt_user_cfg_dir=%clt_user_dir%\cfg"
set "clt_user_cfg_path_file=%clt_user_cfg_dir%\set_path.bat"

echo %proc_name% ^> 
echo %proc_name% ^> clt_root_dir : %clt_root_dir%
echo %proc_name% ^> clt_fix_dir  : %clt_fix_dir%
echo %proc_name% ^> clt_base_dir : %clt_base_dir%
echo %proc_name% ^> clt_user_dir : %clt_user_dir%
echo %proc_name% ^> clt_out_tmp  : %clt_out_tmp%
echo %proc_name% ^> clt_out_dir  : %clt_out_dir%
echo %proc_name% ^> 
echo %proc_name% ^> clt_tools    : %clt_tools%
echo %proc_name% ^> clt_lib      : %clt_lib%
echo %proc_name% ^> clt_cmd      : %clt_cmd%
echo %proc_name% ^>
echo %proc_name% ^> clt_cmd_init : %clt_cmd_init%
echo %proc_name% ^>
echo %proc_name% ^> clt_base_cfg_dir          : %clt_base_cfg_dir%
echo %proc_name% ^> clt_base_cfg_path_file    : %clt_base_cfg_path_file%
echo %proc_name% ^>
echo %proc_name% ^> clt_user_cfg_dir          : %clt_user_cfg_dir%
echo %proc_name% ^> clt_user_cfg_path_file    : %clt_user_cfg_path_file%
echo %proc_name% ^> 



echo %proc_name% ^> ---------------------------------------------------------
echo %proc_name% ^>  configration / tools
echo %proc_name% ^> ---------------------------------------------------------

set "clt_doxygen_bin_dir=C:\Program Files\doxygen\bin"
set "clt_doxygen_bin_file=%clt_doxygen_bin_dir%\doxygen.exe"

set "clt_tools_gen_txt=%clt_tools%\gen_txt.py"
set "clt_tools_gen_files=%clt_tools%\filelist.py"
set "clt_tools_dox_gen_prj=%clt_tools%\gen_doxygen_prj.py"
set "clt_tools_dox_gen_yml=%clt_tools%\gen_doxygen_yml.py"
set "clt_tools_dox_gen_rpt=%clt_tools%\gen_doxygen_rpt.py"
set "clt_tools_dox_gen_mk=%clt_tools%\gen_doxygen_mk.py"
set "clt_tools_dox_marge_yml=%clt_tools%\marge_doxygen_yml.py"

echo %proc_name% ^> 
echo %proc_name% ^> clt_doxygen_bin_dir  : %clt_doxygen_bin_dir%
echo %proc_name% ^> clt_doxygen_bin_file : %clt_doxygen_bin_file%
echo %proc_name% ^> 
echo %proc_name% ^> clt_tools_gen_txt    : %clt_tools_gen_txt%
echo %proc_name% ^> clt_tools_gen_files  : %clt_tools_gen_files%
echo %proc_name% ^> 
echo %proc_name% ^> clt_tools_dox_gen_prj    : %clt_tools_dox_gen_prj%
echo %proc_name% ^> clt_tools_dox_gen_yml    : %clt_tools_dox_gen_yml%
echo %proc_name% ^> clt_tools_dox_gen_rpt    : %clt_tools_dox_gen_rpt%
echo %proc_name% ^> clt_tools_dox_gen_mk     : %clt_tools_dox_gen_mk%
echo %proc_name% ^> clt_tools_dox_marge_yml  : %clt_tools_dox_marge_yml%
echo %proc_name% ^> 



echo %proc_name% ^> ---------------------------------------------------------
echo %proc_name% ^>  configration / environment
echo %proc_name% ^> ---------------------------------------------------------

set "pythonpath=%cur_bat_dir%\..\lib"
set "path=%clt_cmd%;%path%"
set "path=%clt_doxygen_bin%;%path%"

echo %proc_name% ^> 
echo %proc_name% ^> pythonpath : %pythonpath%
echo %proc_name% ^> 



echo %proc_name% ^> ---------------------------------------------------------
echo %proc_name% ^>  configration / base / path
echo %proc_name% ^> ---------------------------------------------------------
echo %proc_name% ^> 

if exist "%clt_base_cfg_path_file%" call "%clt_base_cfg_path_file%"



if not exist "%clt_user_cfg_path_file%" call "%clt_cmd_init%"

echo %proc_name% ^> 
echo %proc_name% ^> ---------------------------------------------------------
echo %proc_name% ^>  configration / user / path
echo %proc_name% ^> ---------------------------------------------------------
echo %proc_name% ^> 

if exist "%clt_user_cfg_path_file%" call "%clt_user_cfg_path_file%"

:start_term
echo %proc_name% ^> 
echo %proc_name% ^> =========================================================
echo %proc_name% ^>  start terminal
echo %proc_name% ^> =========================================================
echo %proc_name% ^> 
cmd /k
