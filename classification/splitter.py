import os
import shutil
from math import *
import random

path = "D:\\ETUDES\\3A\\OSY\\Deep_learning\\projet\\FlickrLogos_47\\classes"
folder0 = path + "\\0\\"
folder1 = path + "\\1\\"
folder2 = path + "\\2\\"
folder3 = path + "\\3\\"
folder4 = path + "\\4\\"
folder5 = path + "\\5\\"
folder6 = path + "\\6\\"
folder7 = path + "\\7\\"
folder8 = path + "\\8\\"
folder9 = path + "\\9\\"
folder10 = path + "\\10\\"
folder11 = path + "\\11\\"
folder12 = path + "\\12\\"
folder13 = path + "\\13\\"
folder14 = path + "\\14\\"
folder15 = path + "\\15\\"
folder16 = path + "\\16\\"
folder17 = path + "\\17\\"
folder18 = path + "\\18\\"
folder19 = path + "\\19\\"
folder20 = path + "\\20\\"
folder21 = path + "\\21\\"
folder22 = path + "\\22\\"
folder23 = path + "\\23\\"
folder24 = path + "\\24\\"
folder25 = path + "\\25\\"
folder26 = path + "\\26\\"
folder27 = path + "\\27\\"
folder28 = path + "\\28\\"
folder29 = path + "\\29\\"
folder30 = path + "\\30\\"
folder31 = path + "\\31\\"
folder32 = path + "\\32\\"
folder33 = path + "\\33\\"
folder34 = path + "\\34\\"
folder35 = path + "\\35\\"
folder36 = path + "\\36\\"
folder37 = path + "\\37\\"
folder38 = path + "\\38\\"
folder39 = path + "\\39\\"
folder40 = path + "\\40\\"
folder41 = path + "\\41\\"
folder42 = path + "\\42\\"
folder43 = path + "\\43\\"
folder44 = path + "\\44\\"
folder45 = path + "\\45\\"
folder46 = path + "\\46\\"
folders = [folder0, folder1, folder2, folder3, folder4, folder5, folder6, folder7,\
              folder8, folder9, folder10, folder11, folder12, folder13, folder14, folder15,\
              folder16, folder17, folder18, folder19, folder20, folder21, folder22, folder23,\
              folder24, folder25, folder26, folder27, folder28, folder29, folder30, folder31, \
              folder32, folder33, folder34, folder35, folder36,folder37, folder38, folder39, \
              folder40, folder41, folder42, folder43, folder44, folder45, folder46]


def get_nb_files(directory):
  """Get number of files by searching directory recursively"""
  return len(os.listdir(directory))

def replace_last(source_string, replace_what, replace_with):
    """Remove \\ from path in order to use os.path.basename"""
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail

global_cache = {}
def cached_listdir(path):
    """Get list of files from folder"""
    res = global_cache.get(path)
    if res is None:
        res = os.listdir(path)
        global_cache[path] = res
    return res

def get_random_file(folder):
    """Get random file from folder"""
    return random.choice(cached_listdir(folder))

def splitter():
    """A partir du dossier classes créé par le parser, splitter train/val (80%-20%)"""
    new_folder_path = "D:\\ETUDES\\3A\\OSY\\Deep_learning\\projet\\FlickrLogos_47\\val"
    try:
        os.mkdir(new_folder_path)
    except:
        pass
    for i in range(47):
        try:
            os.mkdir(new_folder_path + "\\" + str(i))
        except:
            pass

    for folder in folders:
        nb_files = get_nb_files(folder)
        nb_val = floor(0.2 * nb_files)
        files_to_move = []
        folder_name = os.path.split(replace_last(folder, "\\", ""))[1]
        for i in range(nb_val):
            b = get_random_file(folder)
            c = folder + b
            d = str(c)
            files_to_move += [d]
            i += 1
        print(files_to_move)
        for file in files_to_move:
            print(file)
            print(new_folder_path)
            print(folder_name)
            dest =os.path.split(replace_last(file, "\\", ""))[1]
            print(dest)
            img_path = new_folder_path + "\\" + folder_name + "\\" + dest
            print(img_path)
            os.rename(file, img_path)


#splitter()
path_bis = "D:\\ETUDES\\3A\\OSY\\Deep_learning\\projet\\FlickrLogos_47\\classes\\0\\000000280.png"
file_name = os.path.split(replace_last(path_bis, "\\", ""))[1]
file_name =file_name.split(',')
print(file_name)
del file_name[0]
print(file_name)