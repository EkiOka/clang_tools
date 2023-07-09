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

### ファイルリスト

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
| cpp_files     | masks_target_pp                | ターゲット内の拡張子.cppのファイル検索マスク                           |
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

> { ファイル名(行番号 [,列番号]) | ツール名 } : [ 任意のテキスト ] {error | warning} コード タイプと数値:ローカライズ可能文字列 [ 任意のテキスト ]

と思ったが残念ながら情報が不完全。
というのも最初のファイル名はフルパス出力されているため`{ ファイル名(行番号 [,列番号]) | ツール名 } :`で検出される`:`はファイル名内で出力されるため判別が難しい。

また行番号の書式に使用される`(,)`もファイル名内に組み込める文字列のため絶対的な判別は不可能と判断する。
ただし、ファイルパス内で`(数値,数値)`の記載を入れる、更にVisual Studioのソース管理先のパスにそれを使うケースはレアケース過ぎるので、こちらは実施条件から除く。

プロジェクトファイルからの相対パスで出力する方法はありそうな気がするため調査必要。
もしくはドライブレターは文字数固定なため解析時にスキップさせれば問題ない？

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
