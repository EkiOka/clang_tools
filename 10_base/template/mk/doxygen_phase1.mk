{%- set env_path  = data_e39fc4e85e8040d29e215197b26d300a -%}
{%- set user_path = data_fb6f549ef7e44a5693e319ea6bea81e9 -%}
{%- set env_vars  = data_4d22a990e03e4ff0b66061daa1674a0d -%}
{%- set tmpl_inf  = data_095064f18e894dcfaa3f8d12b1d0b9ca -%}
{%- set data_root = data_d74c99efdbb745129d4e98d2194bc941 -%}

{%- set src_files = user_path.file_out_file_list_target_src | load_json -%}

{%- set dir_tmp_dxy = user_path.dir_tmp_dox -%}
{%- set dir_tmp_dxy = user_path.dir_tmp_dox -%}
{%- set dir_tmp_dxy = user_path.file_tmpl_dxy -%}


##########################################################################
# VARIABLES
##########################################################################
# MF  = make file
# DXY = doxygen

MF_NAME=$(notdir $(MAKEFILE_LIST))
MF_DIR=$(dir $(MAKEFILE_LIST))

SRC_FILES={% for src in src_files %}{{ src }} {% endfor %}
DXY_LOG={{dir_tmp_dxy}}\doxygen.log


##########################################################################
# ALL
##########################################################################

.PHONY : all

all: $(DXY_LOG)
	@echo $(MF_NAME) ^> target : $@
	@echo $(MF_NAME) ^> depend : $<
	@echo $(MF_NAME) ^> new    : $?
	@tmp2out.bat

##########################################################################
# DOXYGEN RUN
##########################################################################

$(DXY_LOG): $(SRC_FILES) {{ file_tmpl_dxy }}
	@py_cmd.bat doxygen "-doxyfile_name:file_tmpl_dxy" > {{dir_tmp_dxy}}\doxygen.log 2>&1

##########################################################################
# USER EDIT FILES
##########################################################################

{{ file_tmpl_dxy }}:

$(SRC_FILES):
