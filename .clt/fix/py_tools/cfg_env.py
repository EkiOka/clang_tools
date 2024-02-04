""" コンフィグファイルから環境変数設定用のバッチファイルを生成する
"""

import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_base as cab

class application(cab.cmd_app):
    def main(s):
        a.log_setup("d8658ed222954badbfba1295d1a6eb9d",level="DEBUG")
        for k,v in s.cfg.items():
            a.log_info(f"{k}:{v}")
        a.log_info("！！！作成中！！！")



app = application("4b399ded59144cad95ec678d4ea5f4c5")
app.start()

