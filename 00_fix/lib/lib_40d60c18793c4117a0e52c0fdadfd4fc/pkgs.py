from importlib import import_module as im

imported:dict=dict()

def imp(name:str):
    """モジュールを動的にimportします。

    一度、importしたモジュールは辞書型に保存して流用します。
    動的にimportした場合はvscodeなどのコード補完が効かないので注意してください。
    """
    res = imported.get(name, None)
    if res == None:
        res = im(name)
        if res == None:
            raise Exception(f"{name}のインポートに失敗しました。")
        else:
            imported[name]=res
    return res
