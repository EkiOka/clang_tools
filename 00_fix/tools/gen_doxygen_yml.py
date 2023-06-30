"""doxygenのmarge ymlファイルを解析しやすい形式に変換
"""

#####################################################################
# import
#####################################################################
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import doxygen_compound as doxygen
from xsdata.formats.dataclass.parsers import XmlParser
#####################################################################
# 内部関数定義
#####################################################################

def __main(s, src_path:str, dest_path:str):
    """シェル起動基点

    Parameters
    ----------
    params : dict
        起動引数
    """
    if not a.is_exist(src_path):
        a.log_error(f"src_pathで指定したファイル({src_path})が存在しません。")
        a.sys.exit(1)


    src_txt = a.load_text(src_path)
    parser = XmlParser()
    xml_data = parser.from_string(src_txt, doxygen.DoxygenType)
    dest = __cnv(xml_data)
    a.save_yaml(dest_path,dest)

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
    a.set_log_id("323b761b93b9400c9a1525e70420af11")

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
            if src_item.kind.value == doxygen.DoxParamListKind.PARAM.value:
                res_params = __contents_params(src_item,dest_params)
                res.extend(res_params)
            elif src_item.kind.value == doxygen.DoxParamListKind.RETVAL.value:
                res_params = __contents_retval(src_item,dest_params)
                res.extend(res_params)
            else:
                raise Exception(f"未サポートの種別です({src_item.kind.value})")
        elif isinstance(src_item,doxygen.DocEmptyType):
            pass
        else:
            a.log_warning(f"未対応の型を検出しました(type={type(src_item)},value={src_item})")

    a.set_log_id()

    return res

def __contents_retval(src_item:list[object],dest_params:list=[]):
    res = list()
    dest_item = dict()
    res.append(dest_item)
    dest_item["type"]="retval"

    vals = list()
    dest_item["value"]=vals
    
    for item in src_item.parameteritem:
        if isinstance(item, doxygen.DocParamListItem):
            for name_list in item.parameternamelist:
                for name in name_list.parametername:
                    content = __contents(name.content)
                    val = dict()
                    for c in content:
                        val["value"]= val.get("value","") + c["value"]
                    descript = __contents(item.parameterdescription.content)
                    for d in descript:
                        val["descript"]= val.get("descript","") + d["value"]
                    vals.append(val)
                    pass
        else:
            raise Exception(f"未対応の型です。({type(item)})")
    return res

def __contents_params(src_item:list[object],dest_params:list=[]):
    res = list()
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
        res = a.cnv_text_to_sha256(src)
    return res

def __type(src)->str:
    res = ""
    if isinstance(src,doxygen.DoxRefKind):
        res = src.value
    elif isinstance(src,list):
        for item in src:
            item_res = __type(item)
            res = res + item_res + " "
        if len(res)>0:
            res = res[0:len(res)-1]
    elif isinstance(src,str):
        res = src
    elif isinstance(src,doxygen.RefTextType):
        res = src.value
    else:
        raise Exception(f"{type(src)}型は未サポートです。")
    return res

#####################################################################
# シェル起動
#####################################################################

app = cab.cmd_app("1f46f8135a9046d881b7849a66ecc91c")
app.add_param_cfg_text("src_path")
app.add_param_cfg_text("dest_path")
app.reg_main(__main)
app.start()
