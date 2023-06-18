{%- set env_path  = data_e39fc4e85e8040d29e215197b26d300a -%}
{%- set user_path = data_fb6f549ef7e44a5693e319ea6bea81e9 -%}
{%- set env_vars  = data_4d22a990e03e4ff0b66061daa1674a0d -%}
{%- set tmpl_inf  = data_095064f18e894dcfaa3f8d12b1d0b9ca -%}
{%- set data_root = data_d74c99efdbb745129d4e98d2194bc941 -%}

{%- set md_mask   = user_path.mask_user_notes -%}
{%- set md_files  = md_mask | file_list(True) -%}
{%- set css_file  = user_path.file_user_note_css -%}
{%- set cfg_file  = user_path.file_user_note_cfg -%}
{%- set tmpl_file = user_path.file_user_note_tmpl -%}
{%- set base      = env_path.dir_user_notes -%}
{%- set tmp_dir   = env_path.dir_tmp_notes  -%}
{%- set out_dir   = env_path.dir_out_notes  -%}

##########################################################################
# VARIABLES
##########################################################################
# MF  = make file
MF_NAME=$(notdir $(MAKEFILE_LIST))
MF_DIR=$(dir $(MAKEFILE_LIST))

DEST_FILES = {% for md_file in md_files %}{{out_dir}}\{{md_file | rel_names(base) | replace(".md",".html")}} {% endfor %}

##########################################################################
# ALL
##########################################################################

.PHONY : all

all: $(DEST_FILES)
	@echo $(MF_NAME) ^> 
	@echo $(MF_NAME) ^> target    : $@
	@echo $(MF_NAME) ^> depend    : $<
	@echo $(MF_NAME) ^> new       : $?
	@echo $(MF_NAME) ^> md_files  : {{md_files}}
	@echo $(MF_NAME) ^> css_file  : {{css_file}}
	@echo $(MF_NAME) ^> cfg_file  : {{cfg_file}}
	@echo $(MF_NAME) ^> tmpl_file : {{tmpl_file}}
	@echo $(MF_NAME) ^> base      : {{base}}
	@echo $(MF_NAME) ^> tmp_dir   : {{tmp_dir}}
	@echo $(MF_NAME) ^> out_dir   : {{out_dir}}

##########################################################################
# OUT
##########################################################################

{% for md_file in md_files %}
{{out_dir}}\{{md_file | rel_names(base) | replace(".md",".html")}}: {{tmp_dir}}\{{md_file | rel_names(base) | replace(".md",".html")}}
	@echo $(MF_NAME) ^> 
	@echo $(MF_NAME) ^> target  : $@
	@echo $(MF_NAME) ^> depend  : $<
	@echo $(MF_NAME) ^> new     : $?
	@tmp2out.bat
{% endfor %}


##########################################################################
# TMP
##########################################################################

{% for md_file in md_files %}
{{tmp_dir}}\{{md_file | rel_names(base) | replace(".md",".html")}}: {{md_file}}
	@echo $(MF_NAME) ^> 
	@echo $(MF_NAME) ^> target : $@
	@echo $(MF_NAME) ^> depend : $<
	@echo $(MF_NAME) ^> new    : $?
	py_cmd.bat md2html "-src_md_path:$<" "-src_cfg_name:file_user_note_cfg" "-src_tmpl_name:file_user_note_tmpl" "-dest_html_path:$@"
{% endfor %}

##########################################################################
# USER EDIT FILES
##########################################################################

# md files
{% for md_file in md_files %}
{{md_file}}:
{% endfor %}

# css file
{{css_file}}:

# template file
{{tmpl_file}}:

# config file
{{cfg_file}}:
