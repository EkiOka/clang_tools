import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

glob = None
# リリース時にはコメントアウトしてください
#import glob

def __import():
    global glob
    if glob == None:
        glob = pkgs.imp("glob")
    
def glb(masks:str,recursive=True)->str:
    __import()
    res = glob.glob(masks,recursive = recursive)
    return res
