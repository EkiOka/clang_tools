import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

markdown = None
my_ext = None
markdown_include = None
# リリース時にはコメントアウトしてください
#import markdown
#import markdown_include.include as markdown_include  # pip install markdown-include
#import lib_40d60c18793c4117a0e52c0fdadfd4fc.ext.md as my_ext

def __import():
    global markdown
    global markdown_include
    global my_ext
    if markdown == None:
        markdown = pkgs.imp("markdown")
        markdown_include = pkgs.imp("markdown_include.include")
        my_ext = pkgs.imp("lib_40d60c18793c4117a0e52c0fdadfd4fc.ext.md")

def convert(
        md_text:str,
        extensions:list=None,
        extension_configs:dict=None,
        include_base_path:str="."):
    __import()
    if extensions == None:
        extensions = [
            "admonition",
            "tables",
            "toc",
            "nl2br",
            "codehilite",
            "fenced_code",
            my_ext.md_extension(),
            markdown_include.MarkdownInclude(configs={'base_path':include_base_path}),
        ]
    if extension_configs == None:
        extension_configs = {
            "toc": { "toc_depth": "2-3" }
        }
    md = markdown.Markdown(
        extensions=extensions,
        extension_configs=extension_configs
    )
    res = md.convert(md_text)
    return res

