
# 
# out_filelist
# 
# 

##########################################################################
# 共通変数
##########################################################################

# カレントディレクトリ
CURRENT_DIR         := $(CURDIR)
# Makefileのパス
MAKEFILE_PATH       := $(abspath $(lastword $(MAKEFILE_LIST)))
# Makefileのあるディレクトリ
MAKEFILE_DIR        := $(dir $(MAKEFILE_PATH))
# Makefile名
MAKEFILE_FILE_NAME  := $(notdir   $(MAKEFILE_PATH))
MAKEFILE_BASE_NAME  := $(basename $(MAKEFILE_FILE_NAME))

##########################################################################
# makefile固有変数
##########################################################################

yml_files       := {% for item in files -%}{{ item.yml }} {% endfor %}

##########################################################################
# make内容定義
##########################################################################

.PHONY: all

all: $(out_doxygen_report_file)
	@echo $(MAKEFILE_FILE_NAME) ^> target_file = $@
	@echo $(MAKEFILE_FILE_NAME) ^> input file  = $<
	@echo $(MAKEFILE_FILE_NAME) ^> new file    = $?

$(out_doxygen_report_file): $(out_doxygen_result_file)
	@echo $(MAKEFILE_FILE_NAME) ^> target_file = $@
	@echo $(MAKEFILE_FILE_NAME) ^> new file    = $?
	py "$(gen_doxygen_rpt)" "-src_path:$(out_doxygen_result_file)" "-dest_path:$(out_doxygen_report_file)"

$(out_doxygen_result_file) : $(yml_files)
	@echo $(MAKEFILE_FILE_NAME) ^> target_file = $@
	@echo $(MAKEFILE_FILE_NAME) ^> new file    = $?
	py "$(marge_doxygen_yml)" "-src_mask:$(out_doxygen_yml)\*.yml" "-dest_path:$(out_doxygen_result_file)"

# TODO doxygen毎回上書きなので毎回実行される改善必要

{% for item in files %}
{{ item.yml }} : {{ item.xml }}
	@echo $(MAKEFILE_FILE_NAME) ^> target_file = $@
	@echo $(MAKEFILE_FILE_NAME) ^> input file  = $<
	@echo $(MAKEFILE_FILE_NAME) ^> new file    = $?
	py "$(gen_doxygen_yml)" "-src_path:{{ item.xml }}" "-dest_path:{{ item.yml }}"

{{ item.xml }}:
	@echo $(MAKEFILE_FILE_NAME) ^> target_file = $@

{% endfor -%}

