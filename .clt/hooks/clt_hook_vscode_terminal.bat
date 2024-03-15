@echo off

chcp 65001 > nul

set "cur_exe_name=%~nx0"

echo %cur_exe_name% ^> =========================================================
echo %cur_exe_name% ^>  clt(clang_tools) configration
echo %cur_exe_name% ^> =========================================================

set "clt_env_id=2edd8282662e4ceaa09f3e7284fd9521"

pushd %~dp0..\..\
set "clt_dir=%cd%"
if "%clt_dir:~-1%"=="\" set "clt_dir=%clt_dir:~0,-1%"
popd
set "clt_hooks_dir=%~dp0"
set "clt_hooks_dir=%clt_hooks_dir:~0,-1%"

echo %cur_exe_name% ^> clt_env_id    : %clt_env_id%
echo %cur_exe_name% ^> clt_dir       : %clt_dir%
echo %cur_exe_name% ^> clt_hooks_dir : %clt_hooks_dir%

call %clt_hooks_dir%\clt_config_path.bat
call %clt_term_cfg_path%
call %clt_hooks_dir%\clt_config_path_post.bat
call %clt_term_cfg_path_post%

set clt_

rem ----------------------------------------------------------------------
:end_proc
rem ----------------------------------------------------------------------

cmd /k
