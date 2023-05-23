@echo off


rd /s /q "%out_doxygen_root%"
rd /s /q "%out_doxygen_mk%"
rd /s /q "%out_doxygen_result%"
rd /s /q "%out_doxygen_xml%"
rd /s /q "%out_doxygen_yml%"
rd /s /q "%out_filelist%"



md "%out_doxygen_root%"
md "%out_doxygen_mk%"
md "%out_doxygen_result%"
md "%out_doxygen_xml%"
md "%out_doxygen_yml%"
md "%out_filelist%"