パッケージメモ

同時にimportしていい単位でファイル(モジュール)を構成(import時間短縮のため)

from パッケージ名.モジュール名 import 識別子名
でimport。(パッケージ名はPYTHONPATHなどを基点としたサブディレクトリ名)
モジュール内の全識別子をimportする場合は識別子名を*と記載する。

全モジュールをインポートする場合は
from パッケージ名 import *

単一のモジュールで構成されたパッケージなら

import パッケージ名

でimport可能とおもわれる

通常のパッケージの書き方はこれ。
どういう構造になっている？

jinja2で確認。

jinja2ディレクトリ内にある
__init__.py
に下記が記載されている
from .loaders import FileSystemLoader as FileSystemLoader
使用側はimport jinja2でjinja2.FileSystemLoaderを使用できている。

FileSystemLoaderは__init__.py内の同一ディレクトリ
loaders.py
に記載されている。

このことから
__init__.pyで記載されればパッケージ名のimportで識別子が使えると想定できるが、
この場合、__init__.pyで記載された識別子がすべてimportされてしまうため
パフォーマンスのためにモジュールを分ける意味がなくなってしまう。

そのため下記の書式はあきらめるしかない
import パッケージ名

ただし、サブパッケージによる管理で上記の__init__.pyを使用するなら
import パッケージ名.サブパッケージ名
で、記載できるはず。
from pkg in idの書き方が直感的ではないのでこの構成がベストと思われる。