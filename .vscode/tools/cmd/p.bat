@echo off

set "txt2yml_src=%workspace_folder%\C01_src"
set "txt2yml_dst=%workspace_folder%\Z01_out\parse\00_txt2yml"
set "txt2yml_exe=%tools_folder%\txt2yml.py"
set "paese_basic_txt_src=%txt2yml_dst%"
set "paese_basic_txt_dst=%workspace_folder%\Z01_out\parse\10_basic"
set "paese_basic_txt_exe=%tools_folder%\paese_basic_txt.py"


call :XML2YML main.c
call :PARSE_BASIC_TXT main.c


goto :EOF

:XML2YML
py %txt2yml_exe% %txt2yml_src%\%1 %txt2yml_dst%\%1.yml
exit /b 0

:PARSE_BASIC_TXT
py %paese_basic_txt_exe% %paese_basic_txt_src%\%1.yml %paese_basic_txt_dst%\%1.yml
exit /b 0
