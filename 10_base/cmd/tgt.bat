@echo off
setlocal
rem TODO : bat to makefile
call py_cmd.bat target_path
call py_cmd.bat gen_filelist "-src_ena_masks:%username%/masks_target_src" "-src_dis_masks:" "-dest_name:%username%/file_tmp_file_list_target_src"
call py_cmd.bat gen_filelist "-src_ena_masks:%username%/masks_target_c"   "-src_dis_masks:" "-dest_name:%username%/file_tmp_file_list_target_c"
call py_cmd.bat gen_filelist "-src_ena_masks:%username%/masks_target_h"   "-src_dis_masks:" "-dest_name:%username%/file_tmp_file_list_target_h"
call py_cmd.bat gen_filelist "-src_ena_masks:%username%/masks_target_cpp" "-src_dis_masks:" "-dest_name:%username%/file_tmp_file_list_target_cpp"
call tmp2out.bat
call py_cmd.bat gen_inc_dirs
call tmp2out.bat

endlocal
exit /b 0
