import xml.etree.ElementTree as ET
import yaml
import codecs
import json

class lib:
    class json:

        @staticmethod
        def load(path: str) -> dict:
            """json file to object.
            """
            try:
                with open(path, encoding="utf-8_sig") as f:
                    t = f.read()
                return json.loads(t)
            except Exception as e:
                return dict()

        @staticmethod
        def save(path: str,data):
            """ jsonファイルとしてデータを保存する
            """
            enc = "utf-8"
            ensure_ascii=False
            with codecs.open(path , "w", enc) as f:
                json.dump(data, f, ensure_ascii=ensure_ascii,indent=4, sort_keys=True)

    class yaml:

        @staticmethod
        def load(path: str) -> dict:
            """yaml file to object.
            """
            try:
                obj = dict()
                with open(path, encoding="utf-8_sig") as f:
                    obj = yaml.safe_load(f)
                    return obj
            except OSError as e:
                return None
    class xml:
        @staticmethod
        def load(path: str) -> dict:
            """xml file to object.
            """
            try:
                xml_tree = ET.parse(path)
                obj = xml_tree.getroot()
                return obj
            except OSError as e:
                return None
