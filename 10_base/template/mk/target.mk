{%- set env_path  = data_e39fc4e85e8040d29e215197b26d300a -%}
{%- set user_path = data_fb6f549ef7e44a5693e319ea6bea81e9 -%}
{%- set env_vars  = data_4d22a990e03e4ff0b66061daa1674a0d -%}
{%- set tmpl_inf  = data_095064f18e894dcfaa3f8d12b1d0b9ca -%}
{%- set data_root = data_d74c99efdbb745129d4e98d2194bc941 -%}

.PHONY : all

all: {{ user_path.file_tmp_file_list_target_src }} \
 {{ user_path.file_out_file_list_target_h }}       \
 {{ user_path.file_out_file_list_target_c }}       \
 {{ user_path.file_out_file_list_target_cpp }}     \
 {{ user_path.file_out_file_list_target_inc }}     \


##########################################################################
# inc out
##########################################################################

{{ user_path.file_out_file_list_target_inc }}: {{ user_path.file_tmp_file_list_target_inc }}
	tmp2out.bat

##########################################################################
# inc tmp
##########################################################################

{{ user_path.file_tmp_file_list_target_inc }}: {{ user_path.file_out_file_list_target_src }}
	py_cmd.bat gen_inc_dirs

##########################################################################
# out
##########################################################################

{{ user_path.file_out_file_list_target_src }}: {{ user_path.file_tmp_file_list_target_src }}
	tmp2out.bat

{{ user_path.file_out_file_list_target_c }}: {{ user_path.file_tmp_file_list_target_c }}
	tmp2out.bat

{{ user_path.file_out_file_list_target_h }}: {{ file_tmp_file_list_target_h }}
	tmp2out.bat

{{ user_path.file_out_file_list_target_cpp }}: {{ user_path.file_tmp_file_list_target_cpp }}
	tmp2out.bat


##########################################################################
# tmp
##########################################################################

{{ user_path.file_tmp_file_list_target_src }}:
	py_cmd.bat gen_filelist "-src_ena_masks:{{env_vars.username}}/masks_target_src" "-src_dis_masks:" "-dest_name:{{env_vars.username}}/file_tmp_file_list_target_src"

{{ user_path.file_tmp_file_list_target_c }}:
	py_cmd.bat gen_filelist "-src_ena_masks:{{env_vars.username}}/masks_target_c"   "-src_dis_masks:" "-dest_name:{{env_vars.username}}/file_tmp_file_list_target_c"

{{ user_path.file_tmp_file_list_target_h }}:
	py_cmd.bat gen_filelist "-src_ena_masks:{{env_vars.username}}/masks_target_h"   "-src_dis_masks:" "-dest_name:{{env_vars.username}}/file_tmp_file_list_target_h"

{{ user_path.file_tmp_file_list_target_cpp }}:
	py_cmd.bat gen_filelist "-src_ena_masks:{{env_vars.username}}/masks_target_cpp" "-src_dis_masks:" "-dest_name:{{env_vars.username}}/file_tmp_file_list_target_cpp"