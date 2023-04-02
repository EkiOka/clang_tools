"""doxygenのmarge ymlファイルを解析しやすい形式に変換
"""

#####################################################################
# import
#####################################################################

from lib import lib

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
    """YAML->整理されたYAML変換処理

    Parameters
    ----------
    src : dict
        XMLを単純に変換したYAMLデータ

    Returns
    -------
    dict
        無駄なフィールドを極力削除して整理したYAMLデータ
    """
    res = {}
    for xml_file_name in src:
        xml_file_value = src[xml_file_name]
        version = __get_attribute(xml_file_value,"version")
        compounddefs = []
        res["version"] = version
        res["compounddefs"]=compounddefs
        for compounddef in __get_children(xml_file_value,"compounddef"):
                compounddefs.append(__cnv_compounddef(compounddef))
    return res


def __cnv_compounddef(compounddef:dict):
    """compounddefの変換処理

    Parameters
    ----------
    compounddef : dict
        変換するcompounddef

    Returns
    -------
    dict
        変換されたcompounddef
    """
    res = {}
    __add_attributes(compounddef,res,["kind","language"])
    __add_single_text(compounddef,res,"compoundname")

    #includes
    for include in __get_children( compounddef, "includes" ):
        __add_includes(include,res)
    #incdepgraph

    #sectiondef
    for sectiondef in __get_children( compounddef, "sectiondef" ):
        __add_sectiondef(sectiondef,res)


    return res

def __add_includes(src:dict,dest:dict):
    """srcのincludeを変換してdestに追加する。
    """
    includes = dest.get("includes",[])
    dest["includes"]=includes

    include = dict()
    includes.append(include)
    __add_attributes(src,include,["local"])
    include["label"]=src["text"]

def __add_sectiondef(src:dict,dest:dict):
    sectiondef = dest.get("sectiondef",dict())
    dest["sectiondef"]=sectiondef

    __add_attributes(src,sectiondef,["kind"])
    for memberdef in __get_children( src, "memberdef"):
        __add_memberdef(memberdef,sectiondef)
        pass

def __add_memberdef(src:dict,dest:dict):
    memberdefs = dest.get("memberdef",[])
    dest["memberdef"]=memberdefs
    memberdef= dict()
    memberdefs.append(memberdef)
    __add_attributes(src,memberdef,["kind","id","prot","static","const","explicit","inline","virt"])
    __add_single_text(src,memberdef,"type")
    __add_single_text(src,memberdef,"definition")
    __add_single_text(src,memberdef,"argsstring")
    __add_single_text(src,memberdef,"name")

    #param
    for param in __get_children( src, "param"):
        param_list = memberdef.get("param",[])
        memberdef["param"]=param_list
        param_dest =dict()
        param_list.append(param_dest)
        __add_single_text(param,param_dest,"type")
        __add_single_text(param,param_dest,"declname")
        pass
    __add_single_text(src,memberdef,"briefdescription")
    __add_single_text(src,memberdef,"detaileddescription")
    __add_single_text(src,memberdef,"inbodydescription")
    #location
    location_dest = dict()
    memberdef["location"]=location_dest
    location_src = __get_children( src, "location")[0]
    __add_attributes(location_src,location_dest,["file","line","column","bodyfile","bodystart","bodyend"])


#--------------------------------------------------------------------
# 単純なXMLデータ操作関数
#--------------------------------------------------------------------

def __get_children(src:dict,name:str)->list:
    """指定されたsrcからnameの要素をリストとして取得する
    """
    children = src.get("children",[])
    res = [c for c in children if c["tag"] == name]
    return res

def __get_attribute(src:dict,name:str,default_value:str="")->str:
    """指定されたsrcから属性要素であるnameのtextを取得する。ない場合はdefault_valueを返す。
    """
    attrib = src.get("attrib",{})
    res = attrib.get(name,default_value)
    return res

def __add_attributes(src:dict,dest:dict,attributes:list):
    """attributesで指定された属性要素をsrcから抜き出してdestに追加する
    """
    for a in attributes:
        dest[a] = __get_attribute(src,a)

def __add_single_text(src:dict,dest:dict,name:str):
    """srcに指定された要素がひとつしかないものとしてnameに指定された要素のtextを抜き出しdestに設定する。
    """
    cs = __get_children(src,name)
    if len(cs)>0:
        c = cs[0]
        text = c["text"]
        if text.isspace():
            dest[name]=""
        else:
            dest[name]=text
    else:
        dest[name]=""

#####################################################################
# シェル起動
#####################################################################

__args_cfg={
    "script":{"type":"text"},
    "src_path":{"type":"text"},
    "dest_path":{"type":"text"}
}

# デバッグ用の値
__debug_args = ['C:\\_data\\text\\dev\\clang_tools\\.vscode\\tools\\cnv_doxygen_yml.py', '-src_path:C:\\_data\\text\\dev\\clang_tools\\Z01_out\\doxygen\\yml\\marge.yml', '-dest_path:C:\\_data\\text\\dev\\clang_tools\\Z01_out\\doxygen\\yml\\normalization.yml']

lib.cmd_app.start(
    __name__,
    __func,
    __args_cfg,
    __debug_args
    )
