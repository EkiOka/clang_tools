import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

jinja2 = None
# リリース時にはコメントアウトしてください
import jinja2

def __import():
    global jinja2
    if jinja2 == None:
        jinja2 = pkgs.imp("jinja2")

def file_system_loader(searchpath:str,encoding="utf8"):
    __import()
    return jinja2.FileSystemLoader( searchpath=searchpath, encoding=encoding)

def environment(loader):
    __import()
    return jinja2.Environment(loader=loader)

def add_filter(name,function,environment):
    __import()
    environment.filters[name]=function

def get_template(name:str,environment):
    __import()
    template = environment.get_template(name)
    return template

def render(data, template)->str:
    return template.render(data)
