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
echo %bat_name% ^>  configration / clt_basic
echo %bat_name% ^> ---------------------------------------------------------

set "clt_root_dir=%cd%"

set "clt_tools_dir=%clt_root_dir%\.clt\ver\tools_py"

cmd /k
