
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
# Makefileのあるディレクトリのひとつ上のディレクトリ
MAKEFILE_PARENT_DIR := $(shell dirname $(MAKEFILE_PATH))
# Makefile名
MAKEFILE_FILE_NAME  := $(notdir   $(MAKEFILE_PATH))
MAKEFILE_BASE_NAME  := $(basename $(MAKEFILE_PATH))

##########################################################################
# makefile固有変数
##########################################################################

yml_files       := {% for item in files -%}{{ item.yml }} {% endfor %}

##########################################################################
# make内容定義
##########################################################################

.PHONY: all

all: $(out_doxygen_result_file)

$(out_doxygen_result_file) : $(yml_files)
	py "$(marge_doxygen_yml)" "-src_mask:$(out_doxygen_yml)\*.yml" "-dest_path:$(out_doxygen_result_file)"

{% for item in files %}
{{ item.yml }} : {{ item.xml }}
	py "$(gen_doxygen_yml)" "-src_path:{{ item.xml }}" "-dest_path:{{ item.yml }}"

{{ item.xml }}:

{% endfor -%}

