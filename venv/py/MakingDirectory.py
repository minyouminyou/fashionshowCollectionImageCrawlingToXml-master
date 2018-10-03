import os

class MakeDirectory:
    def __init__(self):
        pass

    def makeDir(self,dir_path,dir_name):
        try:
            if not(os.path.isdir(dir_path+"/"+dir_name+"/")):
                os.mkdir(dir_path + "/" + dir_name + "/")
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("failed to create directory!!")
                raise