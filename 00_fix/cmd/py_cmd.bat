@echo off
setlocal
set "cur_bat_dir=%~dp0"
set "cur_bat_dir=%cur_bat_dir:~,-1%"

py %cur_bat_dir%\py_cmd.py %*

endlocal
exit /b 0
