@echo off

rem =========================================================================
rem environment
rem =========================================================================

set bat_name=%~n0
set "gen_files_tool=%tools_folder%\filelist.py"

echo %bat_name% ^> %%tools_folder%%=%tools_folder%
echo %bat_name% ^> %%out_filelist%%=%out_filelist%

rem =========================================================================
rem generate Doxygen xml file list
rem =========================================================================

set "ena_masks=%out_doxygen_xml%\**\*_8c.xml"
set "dis_masks="
set "tmp_out=%tmp_filelist%\doxygen_xml_files.yml"
set "dest=%out_filelist%\doxygen_xml_files.yml"

echo %bat_name% ^> 
echo %bat_name% ^> -----------------------------------------
echo %bat_name% ^> %gen_files_tool%
echo %bat_name% ^> -----------------------------------------
echo %bat_name% ^> Params
echo %bat_name% ^> %%ena_masks%%=%ena_masks%
echo %bat_name% ^> %%dis_masks%%=%dis_masks%
echo %bat_name% ^> %%tmp_out%%=%tmp_out%
echo %bat_name% ^> -----------------------------------------
echo %bat_name% ^> 

py "%gen_files_tool%" "-enable_masks:%ena_masks%" "-disable_masks:%dis_masks%" "-dest:%dest%"

