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

set "clt_base_lib_dir=%clt_root_dir%\10_base\lib"
set "clt_base_cmd_dir=%clt_root_dir%\10_base\cmd"

set "clt_user_lib_dir=%clt_root_dir%\20_user\lib"
set "clt_user_cmd_dir=%clt_root_dir%\20_user\cmd"

set "path=%clt_cmd_dir%;%clt_user_cmd_dir%;%clt_base_cmd_dir%;%path%"
set "pythonpath=%clt_lib_dir%;%clt_user_lib_dir%;%clt_base_lib_dir%;%pythonpath%"

echo %proc_name% ^> clt_root_dir  : %clt_root_dir%
echo %proc_name% ^> clt_tools_dir : %clt_tools_dir%

echo %proc_name% ^> ---------------------------------------------------------

if not exist "%clt_user_cmd_dir%" call :initialize

cmd /k

rem ----------------------------------------------------------------------
:initialize
rem ----------------------------------------------------------------------
call py_cmd init.py
