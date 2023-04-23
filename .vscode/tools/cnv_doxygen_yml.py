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

__key_name_cnv_table={
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
    "version":"version",
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
    doxygen = []
    res["doxygen"] = doxygen

    for xml_v in src.values():
        xml_children = xml_v.get("children",[])
        for dg_child in xml_children: # dg = doxygen
            element=__cnv_element(dg_child)
            doxygen.append(element)
            pass

    return res    

def __pre_prpc(src:dict):

    name = src.get("tag","")

    match(name):
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

    res_name = __key_name_cnv_table[name]

    return res_name

def __post_prpc(src:dict, dest:dict, name:str):
    match(name):
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


def __cnv_element(src:dict):

    res = {}
    dest=dict()
    name = __pre_prpc(src)

    src_attrs = src.get("attrib",{})
    src_children = src.get("children",[])

    for attrib_key, attrib_value in src_attrs.items():
        dest[attrib_key]=attrib_value
    
    if len(src_children)>0:
        children = []
        for child in src_children:
            dest_child = __cnv_element(child)
            if len(dest_child.keys())>0:
                children.append(dest_child)
        if len(children)>0:
            for d in children:
                for k,v in d.items():
                    dest_target = dest.get(k,[])
                    dest_target.append(v)
                    dest[k]=dest_target
            res[name]=dest

    elif len(src_attrs)>0:
        res[name]=dest
        text = src.get("text","")
        if text == None:
            pass
        elif text.isspace():
            pass
        else:
            res["text"]=text
    else:
        text = src.get("text","")
        if text == None:
            pass
        elif text.isspace():
            pass
        else:
            res[name]=text

    __post_prpc( src, res, name )

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
        [".vscode\\tools\\cnv_doxygen_yml.py", '-src_path:C:\\_data\\text\\dev\\clang_tools\\Z01_out\\doxygen\\yml\\marge.yml', '-dest_path:C:\\_data\\text\\dev\\clang_tools\\Z01_out\\doxygen\\yml\\normalization.yml']
        )
