{%- set env_path  = data_e39fc4e85e8040d29e215197b26d300a -%}
{%- set user_path = data_fb6f549ef7e44a5693e319ea6bea81e9 -%}
{%- set env_vars  = data_4d22a990e03e4ff0b66061daa1674a0d -%}
{%- set tmpl_inf  = data_095064f18e894dcfaa3f8d12b1d0b9ca -%}
{%- set data_root = data_d74c99efdbb745129d4e98d2194bc941 -%}

{%- set xml_files = user_path.mask_out_dxy_xml_files | file_list(True)  -%}


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

all: {% for xml_file in xml_files %}{{ xml_file | replace(".xml",".yml") | replace("\\xml\\","\\yml\\")  }} {% endfor %}
	@echo $(MF_NAME) ^> target                 : $@
	@echo $(MF_NAME) ^> depend                 : $<
	@echo $(MF_NAME) ^> new                    : $?
	@echo $(MF_NAME) ^> mask_out_dox_xml_files : {{mask_out_dxy_xml_files}}
	@echo $(MF_NAME) ^> xml_files              : {% for xml_file in xml_files %}{{ xml_file }} {% endfor %}
	tmp2out.bat

##########################################################################
# DOXYGEN RUN
##########################################################################
{% for xml_file in xml_files %}
{{ xml_file | replace(".xml",".yml") | replace("\\xml\\","\\yml\\") }}: {{ xml_file }}
	@echo $(MF_NAME) ^> target : $@
	@echo $(MF_NAME) ^> depend : $<
	@echo $(MF_NAME) ^> new    : $?
	py_cmd gen_doxygen_yml "-src_path:$<" "-dest_path:$@"
{% endfor %}
##########################################################################
# USER EDIT FILES
##########################################################################
{% for xml_file in xml_files %}
{{ xml_file }}:
{% endfor %}
