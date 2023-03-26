@echo off
rem ----------------------------------------------------------------------
rem automation
rem ----------------------------------------------------------------------
set "path_doxygen_file=%workspace_folder%\B01_prj_doxygen\Doxyfile"
set "path_doxygen_xml=%workspace_folder%\Z01_out\doxygen\xml"
set "path_doxygen_yml=%workspace_folder%\Z01_out\doxygen\yml"

set "xml2yml=%tools_folder%\xml2yml.py"
set "path_marge_yml=%path_doxygen_yml%\marge.yml"

set "cnvyml=%tools_folder%\cnv_doxygen_yml.py"
set "path_nrm_yml=%path_doxygen_yml%\normalization.yml"

set "cdcflt=%tools_folder%\cdc_filter.py"
set "path_flt_yml=%path_doxygen_yml%\flt.yml"


rem ----------------------------------------------------------------------
rem make directory
rem ----------------------------------------------------------------------
md "%path_doxygen_xml%"
md "%path_doxygen_yml%"

rem ----------------------------------------------------------------------
rem doxygen
rem ----------------------------------------------------------------------
doxygen.exe %path_doxygen_file%

rem xml file to yml
py %xml2yml% "-src_masks:%path_doxygen_xml%\*_8c.xml" "-dis_masks:" "-dest_path:%path_marge_yml%"

rem convert yml file
py %cnvyml% "-src_path:%path_marge_yml%" "-dest_path:%path_nrm_yml%"

rem code check items filter
py %cdcflt% "-src_path:%path_nrm_yml%" "-dest_path:%path_flt_yml%"

rem code check
