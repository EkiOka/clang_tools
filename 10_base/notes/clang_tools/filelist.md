# ファイルリスト

ファイルリストは動的に生成されるjsonファイルを指します。
jsonファイルの内容はpythonのglobで検索をかけた結果となります。
主にmakefileなどでターゲットの数が決まっていないときに使用します。

makefileでパターンによる指定も可能ですが、
makefileにはパターンによる検索結果の確定した状態のmakefileを中間生成する機能ないので
問題が発生した際の分析に向きません。
（単に探し方が悪いだけの可能性もありますが)

そのためmakefileはpython+jinja2による生成、実行というプロセスを経るため、
入力データとして本ファイルが必要となります。

ただし、複数の処理を経てターゲットを生成する場合、中間生成物が必要になる場合もあるため、
jinja2によるglobの実行を行うフィルタが追加されたため事前準備が必要なもののみが対象となります。

## データフロー

```mermaid
flowchart TB

    clang_tools -- ref -.->path_list


    subgraph clang_tools
        direction LR

        subgraph target
            direction LR

            c_files
            h_files
            cpp_files
        end

        gen_filelist_c(["gen_filelist.py"]):::process
        gen_filelist_h(["gen_filelist.py"]):::process
        gen_filelist_cpp(["gen_filelist.py"]):::process
        gen_filelist_src(["gen_filelist.py"]):::process
        gen_inc_dirs(["gen_inc_dirs.py"]):::process

        subgraph tmp
            direction LR

            tmp_c_list
            tmp_h_list
            tmp_cpp_list
            tmp_src_list
            tmp_inc_list
        end

        tmp2out1(["tmp2out.bat"]):::process
        tmp2out2(["tmp2out.bat"]):::process

        subgraph out
            direction LR

            out_c_list
            out_h_list
            out_cpp_list
            out_src_list
            out_inc_list
        end
    end
    
    c_files   -- src_ena_masks --> gen_filelist_c   -- dest_name --> tmp_c_list
    h_files   -- src_ena_masks --> gen_filelist_h   -- dest_name --> tmp_h_list
    cpp_files -- src_ena_masks --> gen_filelist_cpp -- dest_name --> tmp_cpp_list

    c_files          -- src_ena_masks --> gen_filelist_src
    h_files          -- src_ena_masks --> gen_filelist_src
    cpp_files        -- src_ena_masks --> gen_filelist_src
    gen_filelist_src -- dest_name     --> tmp_src_list

    out_src_list --> gen_inc_dirs --> tmp_inc_list

    tmp_c_list   --> tmp2out1 --> out_c_list
    tmp_h_list   --> tmp2out1 --> out_h_list
    tmp_cpp_list --> tmp2out1 --> out_cpp_list
    tmp_src_list --> tmp2out1 --> out_src_list
    tmp_inc_list --> tmp2out2 --> out_inc_list

    classDef process fill:red,fill-opacity:0.1
    classDef user_path fill:yellow,fill-opacity:0.1
    classDef env_path fill:green,fill-opacity:0.1
```

| 図内識別子    | ユーザーパス名                 | 説明                                                                   |
| ------------- | ------------------------------ | ---------------------------------------------------------------------- |
| c_files       | masks_target_c                 | ターゲット内の拡張子.cのファイル検索マスク                             |
| h_files       | masks_target_h                 | ターゲット内の拡張子.hのファイル検索マスク                             |
| cpp_files     | masks_target_cpp               | ターゲット内の拡張子.cppのファイル検索マスク                           |
|               | masks_target_src               | ターゲット内の拡張子.c;.h;.cppのファイル検索マスク                     |
||||
| tmp_c_list    | file_tmp_file_list_target_c    | ターゲット内の拡張子.cの一時ファイルリスト保存先ファイル(JSON)         |
| tmp_h_list    | file_tmp_file_list_target_h    | ターゲット内の拡張子.hの一時ファイルリスト保存先ファイル(JSON)         |
| tmp_cpp_list  | file_tmp_file_list_target_cpp  | ターゲット内の拡張子.cpp一時ファイルリスト保存先ファイル(JSON)         |
| tmp_src_list  | file_tmp_file_list_target_src  | ターゲット内の拡張子.c;.h;.cppの一時ファイルリスト保存先ファイル(JSON) |
||||
| out_c_list    | file_out_file_list_target_c    | ターゲット内の拡張子.cの更新ファイルリスト保存先ファイル(JSON)         |
| out_h_list    | file_out_file_list_target_h    | ターゲット内の拡張子.hの更新ファイルリスト保存先ファイル(JSON)         |
| out_cpp_list  | file_out_file_list_target_cpp  | ターゲット内の拡張子.cpp更新ファイルリスト保存先ファイル(JSON)         |
| out_src_list  | file_out_file_list_target_src  | ターゲット内の拡張子.c;.h;.cppの更新ファイルリスト保存先ファイル(JSON) |
||||
| tmp_inc_list    | file_tmp_file_list_target_c   | includeパスリストの一時ファイルリスト保存先ファイル(JSON)             |
| out_inc_list    | file_out_file_list_target_inc | includeパスリストの拡張子.c一更新ファイルリスト保存先ファイル(JSON)   |
||||

※includeパスはソースファイル(.c、および.h)からの相対パスか外部のパスから構成されているため、前者の検索を行うためのパスリストを生成するため.cと.hのパスリストを入力としている。

