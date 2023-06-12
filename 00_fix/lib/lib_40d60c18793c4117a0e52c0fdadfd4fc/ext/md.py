import os
import re
import string
import markdown
import markdown.inlinepatterns as ilp

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

        href_split = str(href).split(os.extsep)

        replaced_href = ""
        if len(href_split) < 2:
            replaced_href = href
        else:
            ext     = href_split[-1]
            not_ext = ".".join(href_split[:-1])
            if ext == "md":
                ext = "html"
            replaced_href = f"{not_ext}.{ext}"

        return (replaced_href, title, index, handled)
    
  

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


