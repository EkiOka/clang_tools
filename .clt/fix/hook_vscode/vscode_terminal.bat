@echo off

chcp 65001 > nul

set "bat_name=%~nx0"

echo %bat_name% ^> =========================================================
echo %bat_name% ^>  clt(clang_tools) configration
echo %bat_name% ^> =========================================================

set "cur_bat_dir=%~dp0"
set "cur_bat_dir=%cur_bat_dir:~,-1%"
set "env_id=07ef773770c9448785a425e3ad32f298"

echo %bat_name% ^> cur_bat_dir : %cur_bat_dir%
echo %bat_name% ^> env_id      : %env_id%
echo %bat_name% ^> ---------------------------------------------------------
echo %bat_name% ^>  configration / standard environment variable
echo %bat_name% ^> ---------------------------------------------------------

set "clt_root_dir=%cd%"

set "clt_tools_dir=%clt_root_dir%\.clt\fix\py_tools"
set "clt_usr_dir=%clt_root_dir%\usr\%username%"
set "clt_cfg_dir=%clt_root_dir%\usr\%username%\050_cfg"
set "clt_out_dir=%clt_root_dir%\usr\%username%\010_out"
set "clt_tmp_dir=%clt_root_dir%\usr\%username%\010_out\tmp"

echo %bat_name% ^> clt_root_dir  : %clt_root_dir%
echo %bat_name% ^> clt_tools_dir : %clt_tools_dir%
echo %bat_name% ^> clt_usr_dir   : %clt_usr_dir%
echo %bat_name% ^> clt_cfg_dir   : %clt_cfg_dir%
echo %bat_name% ^> clt_out_dir   : %clt_out_dir%
echo %bat_name% ^> clt_tmp_dir   : %clt_tmp_dir%

echo %bat_name% ^> ---------------------------------------------------------
echo %bat_name% ^>  configration / make user directory
echo %bat_name% ^> ---------------------------------------------------------

md %clt_usr_dir% 2> nul
md %clt_cfg_dir% 2> nul
md %clt_out_dir% 2> nul
md %clt_tmp_dir% 2> nul

echo %bat_name% ^> ---------------------------------------------------------
echo %bat_name% ^>  configration / user
echo %bat_name% ^> ---------------------------------------------------------

call :cfg_path %clt_root_dir%\usr\_default\050_cfg\vscode_env_vars.yml %clt_tmp_dir%\cfg_33881d18deb24675ad5b4e6e65cee7a1.bat
call :cfg_path %clt_cfg_dir%\vscode_env_vars.yml %clt_tmp_dir%\cfg_33881d18deb24675ad5b4e6e65cee7a1.bat

goto :end_proc

rem ----------------------------------------------------------------------
:cfg_path
rem ----------------------------------------------------------------------
setlocal
set "src_path=%1"
set "dst_path=%2"

echo %bat_name%:cfg_path ^> src_path : %src_path%
echo %bat_name%:cfg_path ^> dst_path : %dst_path%

if not exist "%src_path%" (
    echo %bat_name%:cfg_path ^> config file not found.(%src_path%)
    exit /b 1
)

md "%~dp2" 2> nul

py "%clt_tools_dir%\cfg_env.py" "-src_path:%src_path%" "-dest_path:%dst_path%"
endlocal

if exist "%2" (
    call "%2"
    del %2 2> nul
)
exit /b 0

rem ----------------------------------------------------------------------
:end_proc
rem ----------------------------------------------------------------------

cmd /k
