rem ----------------------------------------------------------------------
rem automation
rem ----------------------------------------------------------------------
set "path_doxygen_file=%workspace_folder%\B01_prj_doxygen\Doxyfile"
set "path_doxygen_xml=%workspace_folder%\Z01_out\doxygen\xml"
set "path_doxygen_yml=%workspace_folder%\Z01_out\doxygen\yml"

doxygen.exe %path_doxygen_file%
py %tools_folder%\doxygen_xml2yml.py "-src_masks:%path_doxygen_xml%\*_8c.xml" "-dis_masks:" "-dest_path:%path_doxygen_yml%\marge.yml"
