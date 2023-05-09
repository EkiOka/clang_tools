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

ツール内におけるファイルパスについては
ツールを拡張する場合を含めて、`vscode_terminal.bat`内の環境変数で行ってください。
動的に生成されるファイル一覧についても環境変数を元に生成してください。

doxygenの設定ファイルなどの外部から情報を含めることのできない場合を除きます。
ただし、このような場合でもテンプレートからの設定ファイルの生成などを行い、
極力動的に環境変数を元に動くようにしてください。

目的としてはファイルパスの管理個所の局所化です。
なんだかんだとシステム関係で一番ネックになるのはファイルパスなどの
どこに情報があるかを示す情報の管理になるので。

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
