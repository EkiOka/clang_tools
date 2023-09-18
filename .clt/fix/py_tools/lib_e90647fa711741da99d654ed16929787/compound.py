from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Type


class DoxAccessor(Enum):
    RETAIN = "retain"
    COPY = "copy"
    ASSIGN = "assign"
    WEAK = "weak"
    STRONG = "strong"
    UNRETAINED = "unretained"


class DoxAlign(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"


class DoxBool(Enum):
    YES = "yes"
    NO = "no"


class DoxCompoundKind(Enum):
    CLASS = "class"
    STRUCT = "struct"
    UNION = "union"
    INTERFACE = "interface"
    PROTOCOL = "protocol"
    CATEGORY = "category"
    EXCEPTION = "exception"
    SERVICE = "service"
    SINGLETON = "singleton"
    MODULE = "module"
    TYPE = "type"
    FILE = "file"
    NAMESPACE = "namespace"
    GROUP = "group"
    PAGE = "page"
    EXAMPLE = "example"
    DIR = "dir"
    CONCEPT = "concept"


class DoxGraphRelation(Enum):
    INCLUDE = "include"
    USAGE = "usage"
    TEMPLATE_INSTANCE = "template-instance"
    PUBLIC_INHERITANCE = "public-inheritance"
    PROTECTED_INHERITANCE = "protected-inheritance"
    PRIVATE_INHERITANCE = "private-inheritance"
    TYPE_CONSTRAINT = "type-constraint"


class DoxHighlightClass(Enum):
    COMMENT = "comment"
    NORMAL = "normal"
    PREPROCESSOR = "preprocessor"
    KEYWORD = "keyword"
    KEYWORDTYPE = "keywordtype"
    KEYWORDFLOW = "keywordflow"
    STRINGLITERAL = "stringliteral"
    CHARLITERAL = "charliteral"
    VHDLKEYWORD = "vhdlkeyword"
    VHDLLOGIC = "vhdllogic"
    VHDLCHAR = "vhdlchar"
    VHDLDIGIT = "vhdldigit"


class DoxImageKind(Enum):
    HTML = "html"
    LATEX = "latex"
    DOCBOOK = "docbook"
    RTF = "rtf"
    XML = "xml"


class DoxLanguage(Enum):
    UNKNOWN = "Unknown"
    IDL = "IDL"
    JAVA = "Java"
    C = "C#"
    D = "D"
    PHP = "PHP"
    OBJECTIVE_C = "Objective-C"
    C_1 = "C++"
    JAVA_SCRIPT = "JavaScript"
    PYTHON = "Python"
    FORTRAN = "Fortran"
    VHDL = "VHDL"
    XML = "XML"
    SQL = "SQL"
    MARKDOWN = "Markdown"
    SLICE = "Slice"
    LEX = "Lex"


class DoxMemberKind(Enum):
    DEFINE = "define"
    PROPERTY = "property"
    EVENT = "event"
    VARIABLE = "variable"
    TYPEDEF = "typedef"
    ENUM = "enum"
    FUNCTION = "function"
    SIGNAL = "signal"
    PROTOTYPE = "prototype"
    FRIEND = "friend"
    DCOP = "dcop"
    SLOT = "slot"
    INTERFACE = "interface"
    SERVICE = "service"


class DoxOlType(Enum):
    VALUE_1 = "1"
    A = "a"
    A_1 = "A"
    I = "i"
    I_1 = "I"


class DoxParamDir(Enum):
    IN = "in"
    OUT = "out"
    INOUT = "inout"


class DoxParamListKind(Enum):
    PARAM = "param"
    RETVAL = "retval"
    EXCEPTION = "exception"
    TEMPLATEPARAM = "templateparam"


class DoxPlantumlEngine(Enum):
    UML = "uml"
    BPM = "bpm"
    WIRE = "wire"
    DOT = "dot"
    DITAA = "ditaa"
    SALT = "salt"
    MATH = "math"
    LATEX = "latex"
    GANTT = "gantt"
    MINDMAP = "mindmap"
    WBS = "wbs"
    YAML = "yaml"
    CREOLE = "creole"
    JSON = "json"
    FLOW = "flow"
    BOARD = "board"
    GIT = "git"


class DoxProtectionKind(Enum):
    PUBLIC = "public"
    PROTECTED = "protected"
    PRIVATE = "private"
    PACKAGE = "package"


class DoxRefKind(Enum):
    COMPOUND = "compound"
    MEMBER = "member"


class DoxRefQualifierKind(Enum):
    LVALUE = "lvalue"
    RVALUE = "rvalue"


class DoxSectionKind(Enum):
    USER_DEFINED = "user-defined"
    PUBLIC_TYPE = "public-type"
    PUBLIC_FUNC = "public-func"
    PUBLIC_ATTRIB = "public-attrib"
    PUBLIC_SLOT = "public-slot"
    SIGNAL = "signal"
    DCOP_FUNC = "dcop-func"
    PROPERTY = "property"
    EVENT = "event"
    PUBLIC_STATIC_FUNC = "public-static-func"
    PUBLIC_STATIC_ATTRIB = "public-static-attrib"
    PROTECTED_TYPE = "protected-type"
    PROTECTED_FUNC = "protected-func"
    PROTECTED_ATTRIB = "protected-attrib"
    PROTECTED_SLOT = "protected-slot"
    PROTECTED_STATIC_FUNC = "protected-static-func"
    PROTECTED_STATIC_ATTRIB = "protected-static-attrib"
    PACKAGE_TYPE = "package-type"
    PACKAGE_FUNC = "package-func"
    PACKAGE_ATTRIB = "package-attrib"
    PACKAGE_STATIC_FUNC = "package-static-func"
    PACKAGE_STATIC_ATTRIB = "package-static-attrib"
    PRIVATE_TYPE = "private-type"
    PRIVATE_FUNC = "private-func"
    PRIVATE_ATTRIB = "private-attrib"
    PRIVATE_SLOT = "private-slot"
    PRIVATE_STATIC_FUNC = "private-static-func"
    PRIVATE_STATIC_ATTRIB = "private-static-attrib"
    FRIEND = "friend"
    RELATED = "related"
    DEFINE = "define"
    PROTOTYPE = "prototype"
    TYPEDEF = "typedef"
    ENUM = "enum"
    FUNC = "func"
    VAR = "var"


class DoxSimpleSectKind(Enum):
    SEE = "see"
    RETURN = "return"
    AUTHOR = "author"
    AUTHORS = "authors"
    VERSION = "version"
    SINCE = "since"
    DATE = "date"
    NOTE = "note"
    WARNING = "warning"
    PRE = "pre"
    POST = "post"
    COPYRIGHT = "copyright"
    INVARIANT = "invariant"
    REMARK = "remark"
    ATTENTION = "attention"
    PAR = "par"
    RCS = "rcs"


class DoxVerticalAlign(Enum):
    BOTTOM = "bottom"
    TOP = "top"
    MIDDLE = "middle"


class DoxVirtualKind(Enum):
    NON_VIRTUAL = "non-virtual"
    VIRTUAL = "virtual"
    PURE_VIRTUAL = "pure-virtual"


@dataclass
class DocAnchorType:
    class Meta:
        name = "docAnchorType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class DocBlockQuoteType:
    class Meta:
        name = "docBlockQuoteType"

    para: List["DocParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DocEmojiType:
    class Meta:
        name = "docEmojiType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    unicode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocEmptyType:
    class Meta:
        name = "docEmptyType"


@dataclass
class DocFormulaType:
    class Meta:
        name = "docFormulaType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class DocHtmlOnlyType:
    class Meta:
        name = "docHtmlOnlyType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    block: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocIndexEntryType:
    class Meta:
        name = "docIndexEntryType"

    primaryie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    secondaryie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class DocInternalS4Type:
    class Meta:
        name = "docInternalS4Type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["DocParaType"],
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocLanguageType:
    class Meta:
        name = "docLanguageType"

    para: List["DocParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    langid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocListItemType:
    class Meta:
        name = "docListItemType"

    para: List["DocParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocParBlockType:
    class Meta:
        name = "docParBlockType"

    para: List["DocParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DocXrefSectType:
    class Meta:
        name = "docXRefSectType"

    xreftitle: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    xrefdescription: Optional["DescriptionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LinkType:
    class Meta:
        name = "linkType"

    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LocationType:
    class Meta:
        name = "locationType"

    file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    line: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    column: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    declfile: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    declline: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    declcolumn: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bodyfile: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bodystart: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bodyend: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ReferenceType:
    class Meta:
        name = "referenceType"

    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    compoundref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    startline: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    endline: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class ReimplementType:
    class Meta:
        name = "reimplementType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SpType:
    class Meta:
        name = "spType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class TableofcontentsKindType:
    class Meta:
        name = "tableofcontentsKindType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tableofcontents: List["TableofcontentsType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ChildnodeType:
    class Meta:
        name = "childnodeType"

    edgelabel: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    relation: Optional[DoxGraphRelation] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CompoundRefType:
    class Meta:
        name = "compoundRefType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    virt: Optional[DoxVirtualKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocEntryType:
    class Meta:
        name = "docEntryType"

    para: List["DocParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    thead: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    colspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[DoxAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[DoxVerticalAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class DocListType:
    class Meta:
        name = "docListType"

    listitem: List[DocListItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    type: Optional[DoxOlType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocRefTextType:
    class Meta:
        name = "docRefTextType"

    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    kindref: Optional[DoxRefKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": Type["DocImageType"],
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": Type["DocDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": Type["DocDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": Type["DocPlantumlType"],
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": Type["DocRefTextType"],
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocSect4Type:
    class Meta:
        name = "docSect4Type"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": Type["DocParaType"],
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": DocInternalS4Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class IncType:
    class Meta:
        name = "incType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    local: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MemberRefType:
    class Meta:
        name = "memberRefType"

    scope: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    virt: Optional[DoxVirtualKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ambiguityscope: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RefTextType:
    class Meta:
        name = "refTextType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    kindref: Optional[DoxRefKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    tooltip: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RefType:
    class Meta:
        name = "refType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    inline: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TableofcontentsType:
    class Meta:
        name = "tableofcontentsType"

    tocsect: List[TableofcontentsKindType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class DocInternalS3Type:
    class Meta:
        name = "docInternalS3Type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["DocParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect3",
                    "type": DocSect4Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocParamName:
    class Meta:
        name = "docParamName"

    direction: Optional[DoxParamDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ref",
                    "type": RefTextType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocParamType:
    class Meta:
        name = "docParamType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ref",
                    "type": RefTextType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocPlantumlType:
    class Meta:
        name = "docPlantumlType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    caption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    engine: Optional[DoxPlantumlEngine] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": Type["DocImageType"],
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": Type["DocDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": Type["DocDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": Type["DocPlantumlType"],
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocRowType:
    class Meta:
        name = "docRowType"

    entry: List[DocEntryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class HighlightType:
    class Meta:
        name = "highlightType"

    class_value: Optional[DoxHighlightClass] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sp",
                    "type": SpType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": RefTextType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class LinkedTextType:
    class Meta:
        name = "linkedTextType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ref",
                    "type": RefTextType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class ListofallmembersType:
    class Meta:
        name = "listofallmembersType"

    member: List[MemberRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class NodeType:
    class Meta:
        name = "nodeType"

    label: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    link: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    childnode: List[ChildnodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CodelineType:
    class Meta:
        name = "codelineType"

    highlight: List[HighlightType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    lineno: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    refkind: Optional[DoxRefKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    external: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocDotMscType:
    class Meta:
        name = "docDotMscType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    caption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": Type["DocImageType"],
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": Type["DocDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": Type["DocDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocParamNameList:
    class Meta:
        name = "docParamNameList"

    parametertype: List[DocParamType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    parametername: List[DocParamName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DocSect3Type:
    class Meta:
        name = "docSect3Type"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": Type["DocParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect4",
                    "type": DocSect4Type,
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": DocInternalS3Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class GraphType:
    class Meta:
        name = "graphType"

    node: List[NodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class DocImageType:
    class Meta:
        name = "docImageType"

    type: Optional[DoxImageKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    inline: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    caption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": Type["DocImageType"],
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocInternalS2Type:
    class Meta:
        name = "docInternalS2Type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["DocParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect3",
                    "type": DocSect3Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocParamListItem:
    class Meta:
        name = "docParamListItem"

    parameternamelist: List[DocParamNameList] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    parameterdescription: Optional["DescriptionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ListingType:
    class Meta:
        name = "listingType"

    codeline: List[CodelineType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocCaptionType:
    class Meta:
        name = "docCaptionType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": DocImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocHeadingType:
    class Meta:
        name = "docHeadingType"

    level: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": DocImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocImageFileType:
    """
    :ivar name: The mentioned file will be located in the directory as
        specified by XML_OUTPUT
    :ivar width:
    :ivar height:
    :ivar content:
    """
    class Meta:
        name = "docImageFileType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": DocImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocParamListType:
    class Meta:
        name = "docParamListType"

    parameteritem: List[DocParamListItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    kind: Optional[DoxParamListKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocSect2Type:
    class Meta:
        name = "docSect2Type"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": Type["DocParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect3",
                    "type": DocSect3Type,
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": DocInternalS2Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocSummaryType:
    class Meta:
        name = "docSummaryType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": DocImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocTitleType:
    class Meta:
        name = "docTitleType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": DocImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocTocItemType:
    class Meta:
        name = "docTocItemType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": DocImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocDetailsType:
    class Meta:
        name = "docDetailsType"

    summary: Optional[DocSummaryType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    para: List["DocParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DocInternalS1Type:
    class Meta:
        name = "docInternalS1Type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["DocParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect2",
                    "type": DocSect2Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocSimpleSectType:
    class Meta:
        name = "docSimpleSectType"

    title: Optional[DocTitleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    para: List["DocParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    kind: Optional[DoxSimpleSectKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocTableType:
    class Meta:
        name = "docTableType"

    caption: Optional[DocCaptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    row: List[DocRowType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    rows: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cols: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocTocListType:
    class Meta:
        name = "docTocListType"

    tocitem: List[DocTocItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DocVarListEntryType:
    class Meta:
        name = "docVarListEntryType"

    term: Optional[DocTitleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class DocSect1Type:
    class Meta:
        name = "docSect1Type"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": Type["DocParaType"],
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": DocInternalS1Type,
                    "namespace": "",
                },
                {
                    "name": "sect2",
                    "type": DocSect2Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocVariableListType:
    class Meta:
        name = "docVariableListType"

    varlistentry: List[DocVarListEntryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    listitem: List[DocListItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequential": True,
        }
    )


@dataclass
class DocInternalType:
    class Meta:
        name = "docInternalType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["DocParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect1",
                    "type": DocSect1Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocCopyType:
    class Meta:
        name = "docCopyType"

    para: List["DocParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    sect1: List[DocSect1Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    internal: Optional[DocInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DocMarkupType:
    class Meta:
        name = "docMarkupType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": DocImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hruler",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "preformatted",
                    "type": Type["DocMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "programlisting",
                    "type": ListingType,
                    "namespace": "",
                },
                {
                    "name": "verbatim",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "javadocliteral",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "javadoccode",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "indexentry",
                    "type": DocIndexEntryType,
                    "namespace": "",
                },
                {
                    "name": "orderedlist",
                    "type": DocListType,
                    "namespace": "",
                },
                {
                    "name": "itemizedlist",
                    "type": DocListType,
                    "namespace": "",
                },
                {
                    "name": "simplesect",
                    "type": DocSimpleSectType,
                    "namespace": "",
                },
                {
                    "name": "title",
                    "type": DocTitleType,
                    "namespace": "",
                },
                {
                    "name": "variablelist",
                    "type": DocVariableListType,
                    "namespace": "",
                },
                {
                    "name": "table",
                    "type": DocTableType,
                    "namespace": "",
                },
                {
                    "name": "heading",
                    "type": DocHeadingType,
                    "namespace": "",
                },
                {
                    "name": "dotfile",
                    "type": DocImageFileType,
                    "namespace": "",
                },
                {
                    "name": "mscfile",
                    "type": DocImageFileType,
                    "namespace": "",
                },
                {
                    "name": "diafile",
                    "type": DocImageFileType,
                    "namespace": "",
                },
                {
                    "name": "toclist",
                    "type": DocTocListType,
                    "namespace": "",
                },
                {
                    "name": "language",
                    "type": DocLanguageType,
                    "namespace": "",
                },
                {
                    "name": "parameterlist",
                    "type": DocParamListType,
                    "namespace": "",
                },
                {
                    "name": "xrefsect",
                    "type": DocXrefSectType,
                    "namespace": "",
                },
                {
                    "name": "copydoc",
                    "type": DocCopyType,
                    "namespace": "",
                },
                {
                    "name": "details",
                    "type": DocDetailsType,
                    "namespace": "",
                },
                {
                    "name": "blockquote",
                    "type": DocBlockQuoteType,
                    "namespace": "",
                },
                {
                    "name": "parblock",
                    "type": DocParBlockType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocUrllink:
    class Meta:
        name = "docURLLink"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["DocUrllink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": DocImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DocParaType:
    class Meta:
        name = "docParaType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": DocUrllink,
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": DocHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": DocImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": DocDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": DocPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": DocAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": DocFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": DocRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": DocEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hruler",
                    "type": DocEmptyType,
                    "namespace": "",
                },
                {
                    "name": "preformatted",
                    "type": DocMarkupType,
                    "namespace": "",
                },
                {
                    "name": "programlisting",
                    "type": ListingType,
                    "namespace": "",
                },
                {
                    "name": "verbatim",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "javadocliteral",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "javadoccode",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "indexentry",
                    "type": DocIndexEntryType,
                    "namespace": "",
                },
                {
                    "name": "orderedlist",
                    "type": DocListType,
                    "namespace": "",
                },
                {
                    "name": "itemizedlist",
                    "type": DocListType,
                    "namespace": "",
                },
                {
                    "name": "simplesect",
                    "type": DocSimpleSectType,
                    "namespace": "",
                },
                {
                    "name": "title",
                    "type": DocTitleType,
                    "namespace": "",
                },
                {
                    "name": "variablelist",
                    "type": DocVariableListType,
                    "namespace": "",
                },
                {
                    "name": "table",
                    "type": DocTableType,
                    "namespace": "",
                },
                {
                    "name": "heading",
                    "type": DocHeadingType,
                    "namespace": "",
                },
                {
                    "name": "dotfile",
                    "type": DocImageFileType,
                    "namespace": "",
                },
                {
                    "name": "mscfile",
                    "type": DocImageFileType,
                    "namespace": "",
                },
                {
                    "name": "diafile",
                    "type": DocImageFileType,
                    "namespace": "",
                },
                {
                    "name": "toclist",
                    "type": DocTocListType,
                    "namespace": "",
                },
                {
                    "name": "language",
                    "type": DocLanguageType,
                    "namespace": "",
                },
                {
                    "name": "parameterlist",
                    "type": DocParamListType,
                    "namespace": "",
                },
                {
                    "name": "xrefsect",
                    "type": DocXrefSectType,
                    "namespace": "",
                },
                {
                    "name": "copydoc",
                    "type": DocCopyType,
                    "namespace": "",
                },
                {
                    "name": "details",
                    "type": DocDetailsType,
                    "namespace": "",
                },
                {
                    "name": "blockquote",
                    "type": DocBlockQuoteType,
                    "namespace": "",
                },
                {
                    "name": "parblock",
                    "type": DocParBlockType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class DescriptionType:
    class Meta:
        name = "descriptionType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": DocParaType,
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": DocInternalType,
                    "namespace": "",
                },
                {
                    "name": "sect1",
                    "type": DocSect1Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class EnumvalueType:
    class Meta:
        name = "enumvalueType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "name",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "initializer",
                    "type": LinkedTextType,
                    "namespace": "",
                },
                {
                    "name": "briefdescription",
                    "type": DescriptionType,
                    "namespace": "",
                },
                {
                    "name": "detaileddescription",
                    "type": DescriptionType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class ParamType:
    class Meta:
        name = "paramType"

    attributes: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    type: Optional[LinkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    declname: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    defname: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    array: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    defval: Optional[LinkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    typeconstraint: Optional[LinkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    briefdescription: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TemplateparamlistType:
    class Meta:
        name = "templateparamlistType"

    param: List[ParamType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class MemberdefType:
    class Meta:
        name = "memberdefType"

    templateparamlist: Optional[TemplateparamlistType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    type: Optional[LinkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    definition: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    argsstring: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    qualifiedname: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    read: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    write: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    bitfield: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    reimplements: List[ReimplementType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    reimplementedby: List[ReimplementType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    qualifier: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    param: List[ParamType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    enumvalue: List[EnumvalueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    requiresclause: Optional[LinkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    initializer: Optional[LinkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    exceptions: Optional[LinkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    briefdescription: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detaileddescription: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    inbodydescription: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    location: Optional[LocationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    references: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    referencedby: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    kind: Optional[DoxMemberKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    static: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    strong: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    const: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    explicit: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    inline: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    refqual: Optional[DoxRefQualifierKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    virt: Optional[DoxVirtualKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    volatile: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mutable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    noexcept: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    constexpr: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    readable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    writable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    initonly: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    settable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    privatesettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    protectedsettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    gettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    privategettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    protectedgettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    final: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sealed: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    new: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    add: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    remove: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    raise_value: Optional[DoxBool] = field(
        default=None,
        metadata={
            "name": "raise",
            "type": "Attribute",
        }
    )
    optional: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    required: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    accessor: Optional[DoxAccessor] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    attribute: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    property: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    readonly: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bound: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    removable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    constrained: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transient: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maybevoid: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maybedefault: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maybeambiguous: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SectiondefType:
    class Meta:
        name = "sectiondefType"

    header: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    description: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    memberdef: List[MemberdefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    kind: Optional[DoxSectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CompounddefType:
    class Meta:
        name = "compounddefType"

    compoundname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    basecompoundref: List[CompoundRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    derivedcompoundref: List[CompoundRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    includes: List[IncType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    includedby: List[IncType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    incdepgraph: Optional[GraphType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    invincdepgraph: Optional[GraphType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innerdir: List[RefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innerfile: List[RefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innerclass: List[RefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innerconcept: List[RefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innernamespace: List[RefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innerpage: List[RefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innergroup: List[RefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    qualifier: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    templateparamlist: Optional[TemplateparamlistType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    sectiondef: List[SectiondefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    tableofcontents: Optional[TableofcontentsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    requiresclause: Optional[LinkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    initializer: Optional[LinkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    briefdescription: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detaileddescription: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    inheritancegraph: Optional[GraphType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    collaborationgraph: Optional[GraphType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    programlisting: Optional[ListingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    location: Optional[LocationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    listofallmembers: Optional[ListofallmembersType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    kind: Optional[DoxCompoundKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[DoxLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    final: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    inline: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sealed: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    abstract: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DoxygenType:
    compounddef: List[CompounddefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\d+\.\d+.*",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )


@dataclass
class Doxygen(DoxygenType):
    class Meta:
        name = "doxygen"
