{%- set env_path  = data_e39fc4e85e8040d29e215197b26d300a -%}
{%- set user_path = data_fb6f549ef7e44a5693e319ea6bea81e9 -%}
{%- set env_vars  = data_4d22a990e03e4ff0b66061daa1674a0d -%}
{%- set tmpl_inf  = data_095064f18e894dcfaa3f8d12b1d0b9ca -%}
{%- set data_root = data_d74c99efdbb745129d4e98d2194bc941 -%}

{%- set src_files = user_path.file_out_file_list_target_src | load_json -%}

{%- set dir_tmp_dxy      = user_path.dir_tmp_dxy      -%}
{%- set file_tmpl_dxy    = user_path.file_tmpl_dxy    -%}
{%- set file_tmp_dxy_log = user_path.file_tmp_dxy_log -%}
{%- set file_out_dxy_log = user_path.file_out_dxy_log -%}

##########################################################################
# VARIABLES
##########################################################################
# MF  = make file
# DXY = doxygen

MF_NAME=$(notdir $(MAKEFILE_LIST))
MF_DIR=$(dir $(MAKEFILE_LIST))

SRC_FILES={% for src in src_files %}{{ src }} {% endfor %}

##########################################################################
# ALL
##########################################################################

.PHONY : all

all: {{file_out_dxy_log}} {{file_tmp_dxy_log}}
	@echo $(MF_NAME) ^>
	@echo $(MF_NAME) ^> target : $@
	@echo $(MF_NAME) ^> depend : $<
	@echo $(MF_NAME) ^> new    : $?
	tmp2out.bat

##########################################################################
# DOXYGEN LOG OUT
##########################################################################

{{ file_out_dxy_log }} : {{file_tmp_dxy_log}}
	@echo $(MF_NAME) ^>
	@echo $(MF_NAME) ^> target : $@
	@echo $(MF_NAME) ^> depend : $<
	@echo $(MF_NAME) ^> new    : $?
	@if exist "$<" echo $(MF_NAME) ^> exist  : $<
	tmp2out.bat

##########################################################################
# DOXYGEN RUN
##########################################################################

{{file_tmp_dxy_log}}: {{ file_tmpl_dxy }} $(SRC_FILES)
	@echo $(MF_NAME) ^>
	@echo $(MF_NAME) ^> target : $@
	@echo $(MF_NAME) ^> depend : $<
	@echo $(MF_NAME) ^> new    : $?
	@if exist "$<" echo $(MF_NAME) ^> exist  : $<
	md "{{dir_tmp_dxy}}"
	py_cmd.bat doxygen "-doxyfile_name:file_tmpl_dxy" > "{{file_tmp_dxy_log}}"

##########################################################################
# USER EDIT FILES
##########################################################################

{{ file_tmpl_dxy }}:

$(SRC_FILES):
