"""doxygenのmarge ymlファイルを解析しやすい形式に変換
"""

#####################################################################
# import
#####################################################################

import sys
from lib import lib
import doxygen_compound as doxygen
from xsdata.formats.dataclass.parsers import XmlParser


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
    src_txt = lib.text.load(src_path)
    parser = XmlParser()
    xml_data = parser.from_string(src_txt, doxygen.DoxygenType)
    dest = __cnv(xml_data)
    lib.yaml.save(dest_path,dest)

#--------------------------------------------------------------------
# 各要素の変換関数
#--------------------------------------------------------------------

def __cnv(src:doxygen.DoxygenType)->dict:
    res = dict()

    for src_comp in src.compounddef:
        file = dict()
        res[src_comp.compoundname] = file

        file["includes"                ] = __includes(src_comp.includes )
        file["include_dependency_graph"] = __incdepgraph(src_comp.incdepgraph)
        file["functions"] = __sectiondef_functions(src_comp.sectiondef)
        file["variables"] = __sectiondef_variables(src_comp.sectiondef)

    return res

def __includes(src:list[doxygen.IncType]):
    res = list()

    for src_inc in src:
        dest_inc = dict()
        dest_inc["local"]=__bool(src_inc.local)
        dest_inc["name"] = src_inc.value
        dest_inc["ref"] = __id(src_inc.refid)
        res.append(dest_inc)

    return res

def __incdepgraph(src:doxygen.GraphType):
    res = list()
    if not( src == None ):
        node_labels = dict()
        for src_node in src.node:
            node_labels[src_node.id]=src_node.label
        for src_node in src.node:
            for child in src_node.childnode:
                dest = dict()
                dest["relation"] = child.relation.value
                dest["src"]      = node_labels[src_node.id]
                dest["dest"]     = node_labels[child.refid]
                res.append(dest)
            if src_node.link != None:
                dest = dict()
                dest["relation"] = "link"
                dest["src"]      = node_labels[src_node.id]
                dest["dest"]     = __id(src_node.link.refid)
                res.append(dest)
    return res

def __sectiondef_functions(src:list[doxygen.SectiondefType]):

    res = list()

    src_funcs = [ item for item in src if item.kind == doxygen.DoxSectionKind.FUNC]

    for src_func in src_funcs:
        for member in src_func.memberdef:
            if member.kind == doxygen.DoxMemberKind.FUNCTION:
                dest_func = dict()
                res.append(dest_func)

                dest_func["name"       ] = member.name
                dest_func["return_type"] = __type(member.type.content)
                dest_func["const"      ] = __bool(member.const)
                dest_func["inline"     ] = __bool(member.inline)
                dest_func["static"     ] = __bool(member.static)

                dest_func["references"] = __member_relation(
                        member.references,
                        member.referencedby)

                # params
                dest_params=list()
                dest_func["params"]=dest_params

                for src_param in member.param:
                    dest_param = dict()
                    dest_params.append(dest_param)

                    dest_declaration_name = ""
                    dest_define_name      = ""
                    dest_type             = __type(src_param.type.content)
                    if src_param.declname != None:
                        dest_declaration_name = src_param.declname
                        if src_param.defname != None:
                            dest_define_name = src_param.defname
                        else:
                            dest_define_name = src_param.declname
                    elif src_param.defname != None:
                        dest_define_name      = src_param.defname

                    dest_param["declaration_name"] = dest_declaration_name
                    dest_param["define_name"]      = dest_define_name
                    dest_param["type"]             = dest_type
                
                # location
                dest_location             = dict()
                dest_location_declaration = dict()
                dest_location_body        = dict()

                dest_func["location"]       =dest_location
                dest_location["declaration"]=dest_location_declaration
                dest_location["body"]       =dest_location_body

                dest_location_declaration["file"] = member.location.declfile
                dest_location_declaration["column"] = member.location.declcolumn
                dest_location_declaration["line"] = member.location.declline

                dest_location_body["start"] = member.location.bodystart
                dest_location_body["end"]   = member.location.bodyend
                dest_location_body["file"]  = member.location.bodyfile

                # comment
                dest_func["brief"]   = __contents(member.briefdescription.content)
                dest_func["details"] = __contents(member.detaileddescription.content, dest_params )

    return res

def __sectiondef_variables(src:list[doxygen.SectiondefType]):

    res = list()
    src_vars = [ item for item in src if item.kind == doxygen.DoxSectionKind.VAR]
    for src_var in src_vars:
        for member in src_var.memberdef:
            if member.kind == doxygen.DoxMemberKind.VARIABLE:
                dest_var = dict()
                res.append(dest_var)
                dest_var["name"  ] = member.name
                dest_var["type"  ] = __type(member.type.content)
                dest_var["static"] = __bool(member.static)
                dest_var["references"] = __member_relation(
                        [],
                        member.referencedby)
                dest_var["init_value"] = __bool(member.initializer)

                # location
                dest_location             = dict()
                dest_location_declaration = dict()
                dest_location_body        = dict()

                dest_var["location"]       =dest_location
                dest_location["declaration"]=dest_location_declaration
                dest_location["body"]       =dest_location_body

                dest_location_declaration["file"] = member.location.declfile
                dest_location_declaration["column"] = member.location.declcolumn
                dest_location_declaration["line"] = member.location.declline

                dest_location_body["start"] = member.location.bodystart
                dest_location_body["end"]   = member.location.bodyend
                dest_location_body["file"]  = member.location.bodyfile

                # comment
                dest_var["brief"] = __contents(member.briefdescription.content)
                dest_var["details"] = __contents(member.detaileddescription.content)


    return res

def __member_relation(references:list[doxygen.ReferenceType],referencedby:list[doxygen.ReferenceType]):
    res = list()

    for ref in references:
        dest_ref = dict()
        res.append(dest_ref)
        dest_ref["name"] = ref.content[0]
        dest_ref["id"]   = __id(ref.refid)
        dest_ref["line_start"] = ref.startline
        dest_ref["line_end"  ] = ref.endline
        dest_ref["relation"    ] = "reference"
    for ref in referencedby:
        dest_ref = dict()
        res.append(dest_ref)
        dest_ref["name"] = ref.content[0]
        dest_ref["id"]   = __id(ref.refid)
        dest_ref["line_start"] = ref.startline
        dest_ref["line_end"  ] = ref.endline
        dest_ref["relation"    ] = "referenced_by"

    return res


#############################################################################
# 定型処理
#############################################################################


def __contents(src:list[object],dest_params:list=[]):
    """descript関係のcontentsを変換します。
    """
    res = list()

    for src_item in src:
        if isinstance(src_item,doxygen.DocParaType):
            dest_content = __contents( src_item.content,dest_params )
            res.extend(dest_content)
        elif isinstance(src_item, str):
            dest_item = dict()
            dest_item["value"]=src_item
            dest_item["type"]=""
            res.append(dest_item)
        elif isinstance(src_item, doxygen.DocSimpleSectType):
            dest_para = __contents( src_item.para, dest_params )
            __replace_contents_type(dest_para, src_item.kind.value)
            res.extend(dest_para)
            pass
        elif isinstance(src_item,doxygen.DocParamListType):
            dest_item = dict()
            params = list()
            res.append(dest_item)
            dest_item["value"]=params
            dest_item["type"]="params"
            
            for param_item in src_item.parameteritem:
                dest_param_direction = ""
                dest_param_name      = ""
                for name in param_item.parameternamelist:
                    for n in name.parametername:
                        if n.direction != None:
                            if n.direction.value != None:
                                dest_param_direction = n.direction.value
                        dest_param_name      = n.content
                dest_description = __contents(param_item.parameterdescription.content, dest_params)
                dest_param = dict()
                if len(dest_param_name)>0:
                    dest_param_name = dest_param_name[0]
                    dest_param["name"       ] = dest_param_name
                else:
                    dest_param["name"       ] = ""
                    dest_param_name = ""

                dest_param["direction"  ] = dest_param_direction
                if len(dest_description)>0:
                    dest_param["description"] = dest_description[0].get("value","")
                else:
                    dest_param["description"] = ""
                params.append(dest_param)

                # 引数情報にコメントを追加
                for dp in dest_params:
                    if dp.get("define_name","#") == dest_param_name:
                        dp["doxygen_comment_name"       ]=dest_param_name
                        dp["doxygen_comment_direction"  ]=dest_param_direction
                        if len(dest_description)>0:
                            dp["doxygen_comment_description"]=dest_description[0].get("value","")
                        else:
                            dp["doxygen_comment_description"]=""
        elif isinstance(src_item,doxygen.DocEmptyType):
            pass
        else:
            raise Exception(f"未対応の型を検出しました({type(src_item)})")

    return res

def __replace_contents_type(src:list, type_name:str):
    """contentのtypeを置換します。
    """
    for item in src:
        item["type"]=type_name

def __bool(src:doxygen.DoxBool):
    """bool形式を変換します
    """
    res = False
    if src == doxygen.DoxBool.YES:
        res = True
    return res

def __id(src:str):
    """id形式を変換します
    
    ID内にソース名が残っているとデータ解析時に視線が流れやすいため、
    内容を読むことを前提としないSHA形式に変換します。
    """
    res = ""
    if src != None:
        res = lib.hashlib.cnv_str_to_sha256(src)
    return res

def __type(src)->str:
    res = ""

    content = src[0]
    if isinstance(content,doxygen.DoxRefKind):
        res = content.value
    else:
        res = content
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
        [".vscode\\tools\\cnv_doxygen_yml.py", '-src_path:Z01_out\\doxygen\\xml\\main_8c.xml', '-dest_path:Z01_out\\doxygen\\yml\\main_8c.yml']
        )
