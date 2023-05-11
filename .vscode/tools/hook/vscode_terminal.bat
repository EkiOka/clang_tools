@echo off
rem --------------------------------------------------------------------------
rem configration
rem --------------------------------------------------------------------------
chcp 65001

rem directory

set "cur_bat_dir=%~dp0"
set "PYTHONPATH=%cur_bat_dir%..\lib"
set "workspace_folder=%CD%"
set "tools_folder=%workspace_folder%\.vscode\tools"

set "path_cmd=%CD%\.vscode\tools\cmd"
set "path_doxygen=C:\Program Files\doxygen\bin"

set "path=%path_cmd%;%path%"
set "path=%path_doxygen%;%path%"

set "out_root=%workspace_folder%\Z01_out"

set "out_doxygen_root=%out_root%\doxygen"
set "out_doxygen_xml=%out_doxygen_root%\xml"
set "out_doxygen_yml=%out_doxygen_root%\yml"
set "out_doxygen_mk=%out_doxygen_root%\mk"
set "out_doxygen_result=%out_doxygen_root%\result"

set "out_filelist=%out_root%\filelist"

set "tmp_root=%workspace_folder%\O10_template"
set "tmp_doxygen_root=%tmp_root%\doxygen"

rem tools

set "gen_files_tool=%tools_folder%\filelist.py"
set "gen_doxygen_yml=%tools_folder%\gen_doxygen_yml.py"
set "gen_doxygen_rpt=%tools_folder%\gen_doxygen_rpt.py"
set "gen_doxygen_mk=%tools_folder%\gen_doxygen_mk.py"
set "marge_doxygen_yml=%tools_folder%\marge_doxygen_yml.py"

rem files

set "path_doxygen_file=%workspace_folder%\B01_prj_doxygen\Doxyfile"
set "path_doxygen_xml_files=%out_filelist%\doxygen_xml_files.yml"
set "tmp_doxygen_mk=%tmp_root%\doxygen\doxygen.mk"
set "out_doxygen_makefile=%out_doxygen_mk%\doxygen.mk"
set "out_doxygen_result_file=%out_doxygen_result%\result.yml"
set "out_doxygen_report_file=%out_doxygen_result%\report.yml"
set "out_doxygen_warning_txt=%out_doxygen_result%\warning.txt"

rem --------------------------------------------------------------------------
rem remake directory
rem --------------------------------------------------------------------------


rd /s /q "%out_doxygen_root%"
rd /s /q "%out_doxygen_mk%"
rd /s /q "%out_doxygen_result%"
rd /s /q "%out_doxygen_xml%"
rd /s /q "%out_doxygen_yml%"
rd /s /q "%out_filelist%"

md "%out_doxygen_root%"
md "%out_doxygen_mk%"
md "%out_doxygen_result%"
md "%out_doxygen_xml%"
md "%out_doxygen_yml%"
md "%out_filelist%"

rem --------------------------------------------------------------------------
rem start terminal
rem --------------------------------------------------------------------------
cmd /k
