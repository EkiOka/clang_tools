import os
import re
import string
import markdown
import markdown.inlinepatterns as ilp
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a

class md_preprocessor(markdown.preprocessors.Preprocessor):

    has_mermaid = False

    def run_lines(self, lines):
        # ca = code area
        pat_ca_start = re.compile(
            r"^(?P<code_area_sign>[\~\`]{3})[\ \t]*(?P<code_area_name>[a-zA-Z_]*)[\ \t]*$")
        pat_ca_end = re.compile(
            r"^(?P<code_area_sign>[\~\`]{3})[\ \t]*$")

        result_lines = []
        code_area_sign = ""
        code_area_name = ""
        for line in lines:
            code_changed = False
            src_line = line
            print_line = ''.join(filter(lambda x: x in string.printable, line))

            match code_area_name:
                case "":
                    mat = pat_ca_start.match(print_line)
                    if mat:
                        code_area_sign = mat.group("code_area_sign")
                        code_area_name = mat.group("code_area_name")
                        if code_area_name == "mermaid":
                            result_lines.append('<div class="mermaid">')
                            self.has_mermaid = True
                            code_changed = True
                        else:
                            code_area_name = "-"

                case "mermaid":
                    mat = pat_ca_end.match(print_line)
                    if mat:
                        if mat.group("code_area_sign") == code_area_sign:
                            result_lines.append("</div>")
                            result_lines.append("")
                            code_area_name = "" # area end
                            code_changed = True
                    if not code_changed:
                        result_lines.append(src_line.strip())
                        code_changed = True

                case "-": # not supported area
                    mat = pat_ca_end.match(print_line)
                    if mat:
                        if mat.group("code_area_sign") == code_area_sign:
                            code_area_name = "" # area end
                    pass

            if not code_changed:
                result_lines.append(src_line)

        return result_lines

    def run(self, lines):
        result_lines = self.run_lines(lines)
        return result_lines


class md_inline_processor(ilp.LinkInlineProcessor):
    
    def getLink(self, *args, **kwargs):
        
        href, title, index, handled = super().getLink(*args, **kwargs)

        dest_href = ""

        url = a.url_values(href)
        if url.is_rel:
            dest_path = self.replace_ext(url.path,".md",".html")
            url.path = dest_path
            dest_href = url.to_str()
        else:
            dest_href = href

        return (dest_href, title, index, handled)
    def replace_ext(s,path:str,src_dot_ext:str=".md", dest_dot_ext=".html"):
        dest_path = path
        if path[-len(src_dot_ext):]==src_dot_ext:
            dest_path = path[0:len(path)-len(src_dot_ext)]
            dest_path = dest_path + dest_dot_ext
        return dest_path

    
  

class md_extension(markdown.Extension):
    def extendMarkdown(self, md:markdown.core.Markdown, md_globals=None):
        """ add extension instance. """

        # https://github.com/Python-Markdown/markdown/blob/master/markdown/inlinepatterns.py#L73

        # プリプロセッサを登録
        pp =md_preprocessor(md)
        md.preprocessors.register(pp, 'my_pre_proc', 35)
        md.registerExtension(self)

        # 既存のリンク生成を置き換える
        # inlinePatterns.register(LinkInlineProcessor(LINK_RE, md), 'link', 160)
        priority = 160
        md.inlinePatterns.deregister("link")
        pattern = md_inline_processor(ilp.LINK_RE, md)
        md.inlinePatterns.register(pattern, "link", priority)

    def makeExtension(**kwargs):
        return md_extension(**kwargs)


