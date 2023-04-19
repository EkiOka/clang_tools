@echo off
rem ----------------------------------------------------------------------
rem automation
rem ----------------------------------------------------------------------
set "path_doxygen_file=%workspace_folder%\B01_prj_doxygen\Doxyfile"
set "path_doxygen_xml=%workspace_folder%\Z01_out\doxygen\xml"
set "path_doxygen_yml=%workspace_folder%\Z01_out\doxygen\yml"

set "path_rule_file=%workspace_folder%\D50_coding_check\rule.yml"

set "xml2yml=%tools_folder%\xml2yml.py"
set "path_marge_yml=%path_doxygen_yml%\marge.yml"

set "cnvyml=%tools_folder%\cnv_doxygen_yml.py"
set "path_nrm_yml=%path_doxygen_yml%\normalization.yml"

set "chkyml=%tools_folder%\chk_doxygen_yml.py"
set "path_rpt_yml=%path_doxygen_yml%\report.yml"

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

rem check yml file
py %chkyml% "-src_path:%path_nrm_yml%" "-cfg_path:%path_rule_file%" "-dest_path:%path_rpt_yml%"
