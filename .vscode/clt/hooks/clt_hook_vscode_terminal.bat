@echo off

chcp 65001 > nul 2>&1

set "cur_exe_name=%~nx0"

echo %cur_exe_name% ^> =========================================================
echo %cur_exe_name% ^>  clt(clang_tools) configration
echo %cur_exe_name% ^> =========================================================

set "clt_env_id=2edd8282662e4ceaa09f3e7284fd9521"

pushd %~dp0..\..\..
set "clt_dir=%cd%"
if "%clt_dir:~-1%"=="\" set "clt_dir=%clt_dir:~0,-1%"
popd
set "clt_hooks_dir=%~dp0"
set "clt_hooks_dir=%clt_hooks_dir:~0,-1%"

echo %cur_exe_name% ^> clt_env_id    : %clt_env_id%
echo %cur_exe_name% ^> clt_dir       : %clt_dir%
echo %cur_exe_name% ^> clt_hooks_dir : %clt_hooks_dir%

call :run_bat "%clt_hooks_dir%\clt_config_path.bat" ""
call :run_bat "%clt_term_cfg_path%" "If you use a path other than the default, please create the this file."
call :run_bat "%clt_hooks_dir%\clt_config_path_post.bat" ""
call :run_bat "%clt_term_cfg_path_post%" "If you use a path other than the default, please create the this file."

call :disp_and_run "set clt_"

echo ---------------------------------------------------------------------
echo.
echo %path:;=&echo.%
echo.
echo %pathext:;=&echo.%
echo.
echo ---------------------------------------------------------------------

goto :end_proc
rem ----------------------------------------------------------------------
:run_bat
rem ----------------------------------------------------------------------
if exist "%~1" (
    call %~1
) else (
    echo %cur_exe_name% ^> %~1 is not fonund.
    echo %cur_exe_name% ^> %~2
    echo %cur_exe_name% ^> 
)
exit /b 0

rem ----------------------------------------------------------------------
:disp_and_run
rem ----------------------------------------------------------------------
echo %cur_exe_name% ^> %~1
echo ---------------------------------------------------------------------
echo.
%~1
echo.
echo ---------------------------------------------------------------------
exit /b 0

rem ----------------------------------------------------------------------
:end_proc
rem ----------------------------------------------------------------------

cmd /k
