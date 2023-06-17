@echo off
setlocal

call py_cmd doxygen -doxyfile_name:file_doxyfile_template

endlocal
exit /b 0
