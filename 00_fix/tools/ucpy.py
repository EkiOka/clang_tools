from lib import lib

def __is_exist(path):
    """ファイルの有無確認
    """
    return os.path.exists(path)
def __get_file_size(path:str):
    """ファイルサイズ取得
    """
    return os.path.getsize(path)
def __get_file_sha256(path:str):
    """SHA256取得
    """
    res = ""
    with open(path,"rb") as file:
        fileData = file.read()
        res = hashlib.sha256(fileData).hexdigest()
    return res

class update_copy:

    def __init__(self) -> None:
        lib.log.enable()
        pass

    def out(self, msg:str):
        print(msg)

    def debug(self, msg:str):
        lib.log.debug(msg)

    def copy(self,src_masks:list[str], dest_path:str):
        return


    def __copy_file(src,dest):
        """ファイルの内容に変化がある場合は更新のため上書きコピーします
        日付の変更のみの場合はコピーしません。
        ファイルパスの指定にはマスクは使えません。
        """
        if not(__is_exist(src)):
            raise FileNotFoundError(f'ファイル"{src}"がありません')

        run = False
        if not(__is_exist(dest)):
            print(f'"コピー先にファイルがありません。{src}"を"{dest}"にコピーしました。')
            shutil.copy2(src,dest)
            run = True
        else:
            src_size = __get_file_size(src)
            dst_size = __get_file_size(dest)

            if not(src_size==dst_size):
                print(f'"ファイルサイズが違います。{src}"を"{dest}"にコピーしました。({src_size},{dst_size})')
                shutil.copy2(src,dest)
                run = True
            else:
                src_sha  = __get_file_sha256(src)   
                dst_sha  = __get_file_sha256(dest)   
                if not(src_sha==dst_sha):
                    print(f'"SHA256が違います。{src}"を"{dest}"にコピーしました。({src_sha},{dst_sha})')
                    shutil.copy2(src,dest)
                    run = True
                else:
                    print(f'"{src}"をコピーしませんでした。')
                    # コピーしない(日付の変更は考慮外)
                    pass



#####################################################################
# シェル起動
#####################################################################

def __main(params:dict):
    """本スクリプトがシェルから呼び出された際のファイル処理を記載
    """
    src_mask = params["src_mask"].split(";")
    dest_path = params["dest_path"]
    uc = update_copy
    uc.copy(src_mask,dest_path)
    return

__args_cfg={
    "script":{"type":"text"},
    "src_mask":{"type":"text"},
    "dest_path":{"type":"text"}
}


lib.cmd_app.start(
    __name__,
    __main,
    __args_cfg
    )