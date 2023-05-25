@echo off
setlocal
set "cur_bat_dir=%~dp0"
set "cur_bat_dir=%cur_bat_dir:~,-1%"

py %cur_bat_dir%\py_cmd.py %*

endlocal
exit /b 0

setlocal
set "py_cmd_name=%~nx0"
set "py_cmd=%1"
echo %py_cmd_name% ^> py_cmd : %py_cmd%

shift
:param_set_loop
if not "%~1"=="" (
    set "py_cmd_params=%py_cmd_params% %~1"
    shift
    goto :param_set_loop
)

echo %py_cmd_name% ^> py_cmd_params : %py_cmd_params%

call :run_cmd "%clt_tools_dir%\%py_cmd%" "%py_cmd_params%"
if errorlevel 1 goto end_py_cmd

call :run_cmd "%clt_user_tools_dir%\%py_cmd%" "%py_cmd_params%"
if errorlevel 1 goto end_py_cmd

call :run_cmd "%clt_base_tools_dir%\%py_cmd%" "%py_cmd_params%"
if errorlevel 1 goto end_py_cmd

goto :not_exist_py_cmd


:run_cmd
echo %py_cmd_name% ^> %*
if not exist "%1" exit /b 0
py %*
exit /b 1



:not_exist_py_cmd
echo %py_cmd_name% ^> %py_cmd% not found
endlocal
exit /b 1



:end_py_cmd
endlocal
exit /b 0
