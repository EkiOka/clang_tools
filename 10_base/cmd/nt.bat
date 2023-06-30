@echo off
setlocal

call py_cmd user_make "-src_name:file_note_mk" "-dest_name:file_tmp_note_mk" "-target:all"

endlocal
exit /b 0
