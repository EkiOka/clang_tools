@echo off
setlocal

call py_cmd user_make "-src_name:file_tmpl_doxygen_mk" "-dest_name:file_tmp_doxygen_mk" "-target:all"

endlocal
exit /b 0
