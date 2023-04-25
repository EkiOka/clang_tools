"""doxygenのmarge ymlファイルを解析しやすい形式に変換
"""

#####################################################################
# import
#####################################################################

import sys
from lib import lib

#####################################################################
# variables
#####################################################################

# 削除するキー名
delete_name = "_"

# 置換キー名テーブル
# 「○○の下の××だけ△△に置換したい」とか器用なことはできませんので注意
__key_name_cnv_table={
    "@version"                       : "version",
    "@xml:lang"                      : "language",
    "@language"                      : "language",
    "@kind"                          : "kind",
    "@xsi:noNamespaceSchemaLocation" : delete_name,
    "@xmlns:xsi"                     : delete_name,
    "@id"                            : "id",
    "@file"                          : "file",
    "@refid"                         : "reference_id",
    "@relation"                      : "relation",
    "@local"                         : "local",
    "#text"                          : "value",
    "@mutable"                         : "mutable",
    "@prot"                         : "protect",
    "@static"                         : "static",
    "@bodyend"                         : "body_end",
    "@bodyfile"                         : "body_file",
    "@bodystart"                         : "body_start",
    "@column"                         : "column",
    "@file"                         : "file",
    "@line"                         : "line",
    "@const"                         : "const",
    "@explicit"                         : "explicit",
    "@inline"                         : "inline",
    "@virt"                         : "virtual",
    "@declcolumn"                         : "prototype_declaration_column",
    "@declfile"                         : "prototype_declaration_file",
    "@declline"                         : "prototype_declaration_line",
    "@direction"                         : "direction",

    "compounddef"  : "src_file",

    "compoundname" : "src_name",
    "kind"         : "type",
    "language"     : "lang",

    "includes"     : "includes",
    "label"        : "header_name",
    "local"        : "find_local",

    "sectiondef"   : "section",
    "memberdef"    : "member",

    "argsstring"          : "args",
    "briefdescription"    : "brief",
    "const"               : "const",
    "definition"          : "definition",
    "detaileddescription" : "details",
    "explicit"            : "explicit",
    "id"                  : "id",
    "inbodydescription"   : "in_body",
    "initializer"         : "init_value",
    "inline"              : "inline",
    "location"            : "location",
    "bodyend"            : "body_end",
    "bodyfile"            : "body_file",
    "bodystart"            : "body_start",
    "column"            : "column",
    "file"            : "file",
    "line"            : "line",
    "name"            : "name",
    "prot"            : "protect",
    "static"            : "static",
    "type"            : "type",
    "virt"            : "virtual",
    "param"            : "param",
    "declname"            : "param_name",
    "incdepgraph": "dependency_graph",
    "node":"node",
    "link":"link",
    "childnode":"child_node",
    "para":"paragraph",
    "simplesect":"simple_section",
    "parameterlist":"params",
    "parameteritem":"param",
    "parameternamelist":"names",
    "parametername":"name",
    "parameterdescription":"details"
}



#####################################################################
# 内部関数定義
#####################################################################


def __func(params:dict):
    """シェル起動基点

    Parameters
    ----------
    params : dict
        起動引数
    """
    src_path = params["src_path"]
    dest_path = params["dest_path"]
    src = lib.yaml.load(src_path)
    dest = __cnv(src)
    lib.yaml.save(dest_path,dest)

#--------------------------------------------------------------------
# 各要素の変換関数
#--------------------------------------------------------------------

def __cnv(src:dict)->dict:
    res = {}
    dest_doxygen = []
    res["doxygen"] = dest_doxygen

    for src_xml_file in src.values():
        for src_doxygen in src_xml_file.values():
            element=__cnv_element(src_doxygen)
            dest_doxygen.append(element)
            pass

    return res    

def __pre_prpc(key,value):

    match(key):
        case "includes":
            pass
        case "para":
            pass
        case "briefdescription":
            pass
        case "detaileddescription":
            pass
        case "inbodydescription":
            pass
        case _:
            pass

    res_key_name = __key_name_cnv_table[key]
    res_key_value = value

    return res_key_name, res_key_value

def __post_prpc(key,value):
    match(key):
        case "para":
            pass
        case "briefdescription":
            pass
        case "detaileddescription":
            pass
        case "inbodydescription":
            pass
        case _:
            pass
    return


def __cnv_element(src):

    res  = None
 
    if isinstance(src, dict):
        # 辞書型
        res = dict()
        for src_key, src_value in src.items():
            dest_key,dest_value = __pre_prpc(src_key,src_value)
            if dest_key == delete_name:
                # 処理しないで削除する
                pass
            else:
                dest_value = __cnv_element( dest_value )
                if dest_value == None:
                    # 追加しない
                    pass
                else:
                    res[dest_key]=dest_value
    elif isinstance(src, list):
        # リスト型
        res = list()
        for src_item in src:
            dest_item = __cnv_element( src_item )
            res.append(dest_item)
    else:
        # 単純型
        res = src

    return res


#####################################################################
# シェル起動
#####################################################################

__args_cfg={
    "script":{"type":"text"},
    "src_path":{"type":"text"},
    "dest_path":{"type":"text"}
}

if "debugpy" not in sys.modules:
    lib.cmd_app.start(
        __name__,
        __func,
        __args_cfg
        )
else:
    lib.cmd_app.start(
        __name__,
        __func,
        __args_cfg,
        [".vscode\\tools\\cnv_doxygen_yml.py", '-src_path:Z01_out\\doxygen\\yml\\marge.yml', '-dest_path:Z01_out\\doxygen\\yml\\normalization.yml']
        )
