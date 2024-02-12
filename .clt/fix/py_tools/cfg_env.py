""" コンフィグファイルから環境変数設定用のバッチファイルを生成する
"""

import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_base as cab

class application(cab.cmd_app):
    def main(s):
        a.log_setup("d8658ed222954badbfba1295d1a6eb9d",level="DEBUG")
        src_path = s.cfg["src_path"]
        dest_path = s.cfg["dest_path"]
        yml_data = a.load_yaml(src_path)
        dst = list()
        for item in yml_data:
            match(item.get("type","set")):
                case "add":
                    dst.append(f"set \"{item['name']}={item['value']};%{item['name']}%\"")
                case _:
                    dst.append(f"set \"{item['name']}={item['value']}\"")
            if item.get("make_dir",False) == True:
                dst.append(f"md \"{item['value']}\"2>nul")

        dst.append(f"exit /b 0")
        a.save_text(dest_path,dst)

app = application("4b399ded59144cad95ec678d4ea5f4c5")
app.start()

