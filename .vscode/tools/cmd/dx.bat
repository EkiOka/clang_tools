rem run doxygen
doxygen.exe "%path_doxygen_file%" 1> nul 2> "%out_doxygen_warning_txt%"

call fl.bat 1> nul

rem build makefile
py "%gen_doxygen_mk%" "-src_path:%path_doxygen_xml_files%" "-tmp_path:%tmp_doxygen_mk%" "-dest_path:%out_doxygen_makefile%" 1> nul

rem run makefile
make "--makefile=%out_doxygen_makefile%"
