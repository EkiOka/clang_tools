@echo off
rem --------------------------------------------------------------------------
rem configration
rem --------------------------------------------------------------------------
chcp 65001
set "cur_bat_dir=%~dp0"
set "PYTHONPATH=%cur_bat_dir%..\lib"
set "workspace_folder=%CD%"
set "tools_folder=%workspace_folder%\.vscode\tools"

set "path_cmd=%CD%\.vscode\tools\cmd"
set "path_doxygen=C:\Program Files\doxygen\bin"

set "path=%path_cmd%;%path%"
set "path=%path_doxygen%;%path%"
rem --------------------------------------------------------------------------
rem start terminal
rem --------------------------------------------------------------------------
cmd /k
