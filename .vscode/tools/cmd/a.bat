@echo off

rem ----------------------------------------------------------------------
rem doxygen
rem ----------------------------------------------------------------------

rem run doxygen
doxygen.exe "%path_doxygen_file%"

call fl.bat

rem build makefile
py "%gen_doxygen_mk%" "-src_path:%path_doxygen_xml_files%" "-tmp_path:%tmp_doxygen_mk%" "-dest_path:%out_doxygen_makefile%"

rem run makefile
make "--makefile=%out_doxygen_makefile%" "all"
