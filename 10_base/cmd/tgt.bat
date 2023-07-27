@echo off
setlocal
call py_cmd.bat target_path
call py_cmd.bat user_make "-src_name:file_tmpl_target_mk" -"dest_name:file_tmp_target_mk" "-target:tmps"
call py_cmd.bat user_make "-src_name:file_tmpl_target_mk" -"dest_name:file_tmp_target_mk" "-target:all"

endlocal
exit /b 0
