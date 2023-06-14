import lib_40d60c18793c4117a0e52c0fdadfd4fc.apps.cmd_app_basic as cab
import lib_40d60c18793c4117a0e52c0fdadfd4fc.adps.adp as a
import lib_40d60c18793c4117a0e52c0fdadfd4fc.path_list as pl

class cmd_base2user(cab.cmd_app):
    pass

def base2user(s:cmd_base2user):
    dir_base = pl.get_path("dir_base")
    dir_user = pl.get_path("dir_user")
    a.copy_dir_tree(dir_base,dir_user)
    return

app = cmd_base2user("128cd916e257419188c9140d3192f598")
app.reg_main(base2user)
app.start()
