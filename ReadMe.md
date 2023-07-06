# C言語開発ツール群

個人で利用するC言語の開発ツール群です。
主な目的はvscodeでの開発支援となります。

## 対応機能

対応する機能は以下の通りとなります。

* 仕事上で行う以下の作業の実施結果を利用しやすいYAMLに変換
    * diff結果
    * コードセルフチェック・クロスチェック
    * コーディング規約チェック結果
    * ドキュメント生成結果(doxygenのXML出力など)
    * 静的解析ツール実行結果(指摘・メトリクス)
    * コンパイラ実行結果(エラー、警告)
    * リンカ実行結果(エラー、警告)
    * ソフトウェアテスト実行結果
* YAMLはまとめとしてのレポートファイルに変換して実施毎に問題かどうかを確認結果作成(基準はコーディング規約など現場の基準を用いる)
* 保存次回は同一個所の確認を省略できるようにする
* レポート確認結果は別形式(Excel/Word/pdfファイルなど)にて出力できるようにしてレポート作成工数を軽減する。

## 方針

てきとーに作っててきとーに入れます。
てきとーにご利用ください。
ライセンスはMITになってますが、まあその辺もてきとーで。

## 方針(ファイル構成について)

**パスの一元管理について**

パスを指定するのが面倒なので環境変数`path_list_path`でJSONファイルを指定し、
その中で一元管理することにしました。

指定されていない場合は`path_list.json`がカレントディレクトリに生成されます。

**make用のテンポラリフォルダについて**

Doxygenなどの生成・変換を行うツールは原則ファイルは上書きする形になります。
よって、実行のたびに内容が変わらなくてもタイムスタンプが更新されてしまい、
その結果としてmakeの更新確認が正常に動作しません。

なので結果を一時的に保存するテンポラリフォルダを作成し、
そこからファイル内容の比較で変化したファイルのみコピーすることによりファイルの更新を正常に検出させるようにします。

ただし、これでもログ内のタイムスタンプのみの変更、配置場所のデイレクトリパスの変更による検出がされる可能性があるので
これらがあることを前提としたコピー処理を追加する必要があります。

## 機能

現在の機能は下記の通り。
機能はターミナルからバッチファイルコマンドとして起動させます。
(タスクなどのvscodeの機能は起動するまでの作業が増えがちなので利用していない。)

| コマンド   | 概要                                                                       |
| ---------- | -------------------------------------------------------------------------- |
| nt         | 20_user\notes内にるmdをhtmlに変換して60_out\notesに出力します。            |
| tgt        | doxygenなどの解析対象のパスを設定します。(※1)                             |
| user_init  | ユーザパスを設定します。(※2)                                              |
| dxy        | tgtで設定した対象に対してdoxygenを実行します。出力先は60_out\doxygen(※3)  |

(※1)設定内容は20_user\tools\target_path.pyを参照
(※2)ツールのパスやユーザー拡張機能に関するパスの設定。20_user\tools\user_path.pyを参照。
(※3)現在は解析結果をyml形式に変換するまでしか対応していません。

## データフロー

### ターゲットファイルリスト

```mermaid
flowchart LR

    subgraph パスリスト
        dir_target:::user_path
        dir_tmp:::user_path
        dir_out:::user_path

        subgraph ファイルマスク
            masks_target_src["ソース"]:::user_path
            masks_target_c[".c"]:::user_path
            masks_target_h[".h"]:::user_path
            masks_target_cpp[".cpp"]:::user_path
        end

        subgraph 一時出力ファイルリスト
            file_tmp_file_list_target_src["ソース"]:::user_path
            file_tmp_file_list_target_h[".h"]:::user_path
            file_tmp_file_list_target_c[".c"]:::user_path
            file_tmp_file_list_target_cpp[".cpp"]:::user_path
            file_tmp_file_list_target_inc["includeパス"]:::user_path
        end

        subgraph 更新出力ファイルリスト
            file_out_file_list_target_src["ソース"]:::user_path
            file_out_file_list_target_h[".h"]:::user_path
            file_out_file_list_target_c[".c"]:::user_path
            file_out_file_list_target_cpp[".cpp"]:::user_path
            file_out_file_list_target_inc["includeパス"]:::user_path
        end

        file_tmpl_target_mk["mkテンプレート"]:::user_path
        file_tmp_target_mk["target.mk"]:::user_path
    end

    subgraph vscodeワークスペース

        mk_tmpl["target.mkテンプレート"]

        user_make(["user_make.py"]):::process

        c_files["ターゲット内.cファイルリスト"]
        h_files["ターゲット内.hファイルリスト"]
        cpp_files["ターゲット内.cppファイルリスト"]
        src_files["ターゲット内.srcファイルリスト"]
        inc_dis["ターゲット内includeパスリスト"]
        updated_c_files["更新.cファイルリスト"]
        updated_h_files["更新.hファイルリスト"]
        updated_cpp_files["更新.cppファイルリスト"]
        updated_src_files["更新.srcファイルリスト"]
        updated_inc_dis["更新includeパスリスト"]

        subgraph target_mk["target.mk"]
            gen_filelist_c(["gen_filelist.py"]):::process
            gen_filelist_h(["gen_filelist.py"]):::process
            gen_filelist_cpp(["gen_filelist.py"]):::process
            gen_filelist_src(["gen_filelist.py"]):::process
            ucpy_c(["ucpy.py"]):::process
            ucpy_h(["ucpy.py"]):::process
            ucpy_cpp(["ucpy.py"]):::process
            ucpy_inc(["ucpy.py"]):::process
            ucpy_src(["ucpy.py"]):::process
            gen_inc_dirs(["gen_inc_dirs.py"]):::process
        end
    end

    file_tmpl_target_mk--"param:src_name"-->user_make
    file_tmp_target_mk--"param:dest_name"-->user_make
    mk_tmpl-->user_make
    user_make--makefile生成-->target_mk

    dir_target --> masks_target_c
    dir_target --> masks_target_h
    dir_target --> masks_target_cpp

    masks_target_c--marge-->masks_target_src
    masks_target_h--marge-->masks_target_src
    masks_target_cpp--marge-->masks_target_src

    masks_target_c--"param:src_ena_masks"-->gen_filelist_c
    file_tmp_file_list_target_c--"param:dest_name"-->gen_filelist_c
    gen_filelist_c-->c_files

    masks_target_h--"param:src_ena_masks"-->gen_filelist_h
    file_tmp_file_list_target_h--"param:dest_name"-->gen_filelist_h
    gen_filelist_h-->h_files

    masks_target_cpp--"param:src_ena_masks"-->gen_filelist_cpp
    file_tmp_file_list_target_cpp--"param:dest_name"-->gen_filelist_cpp
    gen_filelist_cpp-->cpp_files

    masks_target_src--"param:src_ena_masks"-->gen_filelist_src
    file_tmp_file_list_target_src--"param:dest_name"-->gen_filelist_src
    gen_filelist_src-->src_files

    updated_src_files-->gen_inc_dirs--"includeパスリスト生成"-->inc_dis
    file_out_file_list_target_inc-->gen_inc_dirs

    dir_tmp-->ucpy_c
    dir_out-->ucpy_c

    dir_tmp-->ucpy_h
    dir_out-->ucpy_h

    dir_tmp-->ucpy_cpp
    dir_out-->ucpy_cpp

    dir_tmp-->ucpy_inc
    dir_out-->ucpy_inc

    c_files-->ucpy_c-->updated_c_files
    h_files-->ucpy_h-->updated_h_files
    cpp_files-->ucpy_cpp-->updated_cpp_files
    src_files-->ucpy_src-->updated_src_files
    inc_dis-->ucpy_inc-->updated_inc_dis


    classDef process fill:red,fill-opacity:0.1
    classDef user_path fill:yellow,fill-opacity:0.1
    classDef env_path fill:green,fill-opacity:0.1
```



## 関連技術情報

### doxygen XMLデータの読み出しについて

doxygenのXMLデータの読み出しは生成されるスキーマ(compound.xsd)と
pythonのxsdataを利用します

まずxsdataを以下のようにインストールします。

~~~shell
pip install xsdata[cli,lxml,soap]
~~~

次にcompound.xsdのあるディレクトリにカレントディレクトリを移動させて以下を実行します。

~~~shell
xsdata compound.xsd --package doxygen_compound
~~~

doxygen_compoundディレクトリ以下にパッケージが生成されるので以下のように使用します。

~~~python
import doxygen_compound as doxygen
from xsdata.formats.dataclass.parsers import XmlParser

xml_string = ""
xml_file_path = "Z01_out/doxygen/xml/main_8c.xml"
parser = XmlParser()

with open(xml_file_path, mode="r", encoding="utf8") as f:
    xml_string = f.read()
root = parser.from_string(xml_string, doxygen.DoxygenType)
print(root)
~~~

### Visual C++のビルドエラー・警告解析

書式は下記にあるので解析して定型化し、チェッカー作れるはず。

https://learn.microsoft.com/ja-jp/cpp/build/formatting-the-output-of-a-custom-build-step-or-build-event?view=msvc-170

### GCCのビルドエラー・警告解析

未調査

### QACのレポート解析

未調査

### Jenkinsでのテスト実行＆レポート解析などの自動化

未調査

### その他ツール対応予定

未調査のツール。コマンド実行できるようならレポートとして取り込む

* CppCheck
* Sphinx
* ReVIEW
* textlint-app
* SourceMonitor
