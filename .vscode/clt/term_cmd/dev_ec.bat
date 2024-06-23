@echo off

echo extract_code
extract_code "mask:%clt_codes_dir%\**\*.py" "dst:%clt_tmp_dir%\extract_code.yml"
echo remake output directory
rd /s /q "%clt_tmp_dir%\export_code"
md "%clt_tmp_dir%\export_code"
echo export_code
export_code "src_dir:%clt_def_cmd_dir%" "src_mask:**\*.py" "src_codes:%clt_tmp_dir%\extract_code.yml" "dst:%clt_tmp_dir%\export_code"
echo diff and manual marge
start "" "%clt_winmarge_exe%" "%clt_tmp_dir%\export_code" "%clt_def_cmd_dir%" 

