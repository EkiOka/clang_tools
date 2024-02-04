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

set "clt_doxygen_tmp_dir=%clt_tmp_dir%\doxygen"
set "clt_doxygen_xml_dir=%clt_tmp_dir%\doxygen\xml"
set "clt_doxygen_yml_dir=%clt_tmp_dir%\doxygen\yml"

md %clt_doxygen_tmp_dir% 2> nul
md %clt_doxygen_xml_dir% 2> nul
md %clt_doxygen_yml_dir% 2> nul

echo %bat_name% ^> clt_doxygen_tmp_dir : %clt_doxygen_tmp_dir%
echo %bat_name% ^> clt_doxygen_xml_dir : %clt_doxygen_xml_dir%
echo %bat_name% ^> clt_doxygen_yml_dir : %clt_doxygen_yml_dir%

call :cfg_env_doxygen

goto :end_proc
rem ----------------------------------------------------------------------
:cfg_env_doxygen
rem ----------------------------------------------------------------------
set "clt_doxygen_cfg_yml=%clt_cfg_dir%\doxygen\default_env_vars.yml"
set "clt_doxygen_cfg_bat=%clt_tmp_dir%\doxygen.bat"

md "%clt_cfg_dir%\doxygen" 2> nul

echo %bat_name% ^> clt_doxygen_cfg_yml : %clt_doxygen_cfg_yml%
echo %bat_name% ^> clt_doxygen_cfg_bat : %clt_doxygen_cfg_bat%

py "%clt_tools_dir%\cfg_env.py" "-src_path:%clt_doxygen_cfg_yml%" "-dest_path:%clt_doxygen_cfg_bat%"
if exist "%clt_doxygen_cfg_bat%" (
    call %clt_doxygen_cfg_bat%
    del %clt_doxygen_cfg_bat% 2> nul
)
exit /b 0

rem ----------------------------------------------------------------------
:end_proc
rem ----------------------------------------------------------------------

cmd /k
