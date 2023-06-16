import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

jinja2 = None
# リリース時にはコメントアウトしてください
#import jinja2

class jinja2_environment:
    loader = None
    env = None
    tmp = None
    def __init__(s,loader):
        s.env = jinja2.Environment(loader=loader)

    def add_filter(s,name,function):
        s.env.filters[name]=function

    def get_template(s,name:str):
        s.tmp = jinja2_template(s.env.get_template(name))
        return s.tmp

class jinja2_template:
    template = None
    def __init__(s,tmp):
        s.template = tmp
    def render(s,data)->str:
        return s.template.render(data)

def __import():
    global jinja2
    if jinja2 == None:
        jinja2 = pkgs.imp("jinja2")

def file_system_loader(searchpath:str,encoding="utf8"):
    __import()
    return jinja2.FileSystemLoader( searchpath=searchpath, encoding=encoding)

def environment(loader)->jinja2_environment:
    __import()
    return jinja2_environment(loader=loader)

