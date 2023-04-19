
class sign:
    txt           = "txt"
    src_path      = "src_path"
    dest_path     = "dest_path"
    cr            = "\r"
    lf            = "\n"
    crlf          = "\r\n"
    begin_column  = "b_col"
    end_column    = "e_col"
    begin_line    = "b_line"
    end_line      = "e_line"
    args_type_txt = {"type":"text"}
    script        = "script"
    file_name     = "file_name"
    type          = "type"

class basic_text_sign:


    """アルファベットの大文字
    """
    alphabet_uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alphabet_uppercase_name = "alphabet_uppercase"

    """アルファベットの小文字
    """
    alphabet_lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabet_lowercase_name = "alphabet_lowercase"

    """数字
    """
    number = ["0","1","2","3","4","5","6","7","8","9"]
    number_name = "number"

    """記号
    """
    mark = [
        "!",        "\"",       "#",        "$",        "%",
        "&",        "'",        "(",        ")",        "=",
        "~",        "|",        "`",        "{",        "+",
        "*",        "}",        "<",        ">",        "?",
        "_",        "-",        "^",        "\\",        "@",
        "[",        ";",        ":",        "]",        ",",
        ".",        "/",        "`"
    ]
    mark_name = "mark"

    """コントロール記号
    """
    control_code = [
        "\0",
        "\a",
        "\b",
        "\f",
        "\n",
        "\r",
        "\t",
        "\v"
    ]
    control_code_name = "control_code"

    """空白
    """
    space = [" "]
    space_name = "space"

    """未定義文字列
    """
    unknown_name = "unknown"

    """改行コード
    """
    new_line = ["\r","\n","\r\n"]
    new_line_name = "new_line"

    """タブ
    """
    tab = ["\t"]
    tab_name = "tab"


class clang:

    """アルファベットの大文字(uppercase letter)
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.1 Character sets
    26個のラテンアルファベットの大文字(uppercase letter)
    """
    uppercase_letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    """アルファベットの小文字(uppercase letter)
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.1 26個のラテンアルファベットの小文字(uppercase letter)
    """
    lowercase_letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    """図形文字(graphic characters)
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.1
    29個の図形文字(graphic characters)
    """
    graphic_characters = [
        "!","\"","#","%","&","'" ,"(" ,")" ,"*" ,"+" ,"," ,"-","." ,"/" ,":",
        ";" ,"<" ,"=",">" ,"?" ,"[" ,"\\","]","ˆ" ,"_" ,"{" ,"|" ,"}","˜",
    ]

    """3文字表記
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.1.1 Trigraph sequences
    """
    trigraph_sequences = [
        "??=",  "??)",  "??!",
        "??(",  "??'",  "??>",
        "??/",  "??<",  "??-"
        ]

    """keyword
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.1) keyword
    """
    keyword = [
        "auto",      "enum",      "restrict",     "unsigned",
        "break",     "extern",    "return",       "void",
        "case",      "float",     "short",        "volatile",
        "char",      "for",       "signed",       "while",
        "const",     "goto",      "sizeof",       "̲_Bool",
        "continue",  "if",        "static",       "̲_Complex",
        "default",   "inline",    "struct",       "̲_Imaginary",
        "do",        "int",       "switch",
        "double",    "long",      "typedef",
        "else",      "register",  "union"
        ]


    """10進数字(digit)
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.2.1) digit
    5.2.1 10個の10進数字(digit)
    """
    digit = ["0","1","2","3","4","5","6","7","8","9"]

    """nondigit
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.2.1) nondigit
    """
    nondigit=["_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    """hexadecimal-prefix
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.1) hexadecimal-prefix
    """
    hexadecimal_prefix=["0x","0X"]

    """nonzero-digit
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.1) nonzero-digit
    """
    nonzero_digit = ["1","2","3","4","5","6","7","8","9"]

    """octal-digit
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.1) octal-digit
    """
    octal_digit = ["1","2","3","4","5","6","7"]

    """hexadecimal-digit
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.1) 
    """
    hexadecimal_digit = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","A","B","C","D","E","F"]

    """unsigned-suffix
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.1) unsigned-suffix
    """
    unsigned_suffix = ["u","U"]

    """long-suffix
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.1) long-suffix
    """
    long_suffix = ["l","L"]

    """long-long-suffix
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.1) long-long-suffix
    """
    long_long_suffix = ["ll","LL"]

    """sign
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.2) sign
    """
    sign = ["+","-"]

    """floating-suffix
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.2) floating-suffix
    """
    floating_suffix = ["f","l","F","L"]

    """simple-escape-sequence
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.4.4) simple-escape-sequence
    """
    simple_escape_sequence = ["\'","\"","\?","\\","\a","\b","\f","\n","\r","\t","\v"]

    """punctuator
    from X3010:2003(ISO/IEC 9899:1999)
    (6.4.6) punctuator
    """
    punctuator=[
        "[]","]","(",")","{","}",".","->",
        "++","--","&","*","+","-","~","!",
        "/","%","<<",">>","<",">","<=",">=","==","!=","^","|","&&","||",
        "?",":",";","...",
        "=","*=","/=","%=","+=","-=","<<=",">>=","&=","^=","|=",
        ",","#","##",
        "<:",":>","<%","%>","%:","%:%:"]

    """unary-operator
    from X3010:2003(ISO/IEC 9899:1999)
    (6.5.3) unary-operator
    """
    unary_operator = ["&","*","+","-","~","!"]

    """assignment-operator
    from X3010:2003(ISO/IEC 9899:1999)
    (6.5.16) assignment-operator
    """
    assignment_operator = ["=","*=","/=","%=","+=","-=","<<=",">>=","&=","^=","|="]

    """storage-class-specifier
    from X3010:2003(ISO/IEC 9899:1999)
    (6.5.16) storage-class-specifier
    """
    storage_class_specifier = [
        "typedef",
        "extern",
        "static",
        "auto",
        "register"]


    """type-specifier
    from X3010:2003(ISO/IEC 9899:1999)
    (6.7.2) type-specifier
    """
    type_specifier = [
        "void",
        "char",
        "short",
        "int",
        "long",
        "float",
        "double",
        "signed",
        "unsigned",
        "̲_Bool",
        "̲_Complex",
        "̲_Imaginary"
        ]

    """struct-or-union
    from X3010:2003(ISO/IEC 9899:1999)
    (6.7.2.1) struct-or-union
    """
    struct_or_union = [
        "struct",
        "union"
    ]

    """type-qualifier
    from X3010:2003(ISO/IEC 9899:1999)
    (6.7.3) type-qualifier
    """
    type_qualifier = [
        "const",
        "restrict",
        "volatile"
    ]
    """function-qualifier
    from X3010:2003(ISO/IEC 9899:1999)
    (6.7.4) function-qualifier
    """
    function_qualifier = [
        "inline"
    ]

    """alert
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.2 Character display semantics
    """
    alert = "\a"


    """backspace
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.2 Character display semantics
    """
    backspace = "\b"


    """form feed
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.2 Character display semantics
    """
    form_feed = "\f"


    """new line
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.2 Character display semantics
    """
    new_line = "\n"

    
    """carriage return
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.2 Character display semantics
    """
    carriage_return = "\r"


    """horizontal tab
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.2 Character display semantics
    """
    horizontal_tab = "\t"


    """vertical tab
    from X3010:2003(ISO/IEC 9899:1999)
    5.2.2 Character display semantics
    """
    vertical_tab = "\v"
