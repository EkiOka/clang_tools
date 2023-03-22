rem ----------------------------------------------------------------------
rem automation
rem ----------------------------------------------------------------------
set "path_doxygen_file=%workspace_folder%\B01_prj_doxygen\Doxyfile"
set "path_doxygen_xml=%workspace_folder%\Z01_out\doxygen\xml"

doxygen.exe %path_doxygen_file%
powershell %tools_folder%\doxygenxml_combine.ps1 %path_doxygen_xml%
