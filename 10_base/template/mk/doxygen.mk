{%- set env_path  = data_e39fc4e85e8040d29e215197b26d300a -%}
{%- set user_path = data_fb6f549ef7e44a5693e319ea6bea81e9 -%}
{%- set env_vars  = data_4d22a990e03e4ff0b66061daa1674a0d -%}
{%- set tmpl_inf  = data_095064f18e894dcfaa3f8d12b1d0b9ca -%}
{%- set data_root = data_d74c99efdbb745129d4e98d2194bc941 -%}

{%- set dir_out_dxy = user_path.dir_out_dxy -%}
{%- set file_out_dxy_log = user_path.file_out_dxy_log -%}

##########################################################################
# VARIABLES
##########################################################################
# MF  = make file
# DXY = doxygen

MF_NAME=$(notdir $(MAKEFILE_LIST))
MF_DIR=$(dir $(MAKEFILE_LIST))

##########################################################################
# ALL
##########################################################################

.PHONY : all

all: {{file_out_dxy_log}}
	@echo $(MF_NAME) ^>
	@echo $(MF_NAME) ^> target : $@
	@echo $(MF_NAME) ^> depend : $<
	@echo $(MF_NAME) ^> new    : $?
	py_cmd user_make "-src_name:file_tmpl_doxygen_p2_mk" "-dest_name:file_tmp_doxygen_p2_mk" "-target:all"


##########################################################################
# PHASE1
##########################################################################

{{file_out_dxy_log}}:
	@echo $(MF_NAME) ^>
	@echo $(MF_NAME) ^> target : $@
	@echo $(MF_NAME) ^> depend : $<
	@echo $(MF_NAME) ^> new    : $?
	tmp2out.bat
	py_cmd user_make "-src_name:file_tmpl_doxygen_p1_mk" "-dest_name:file_tmp_doxygen_p1_mk" "-target:all"
