import os
import shutil

path = "D:/ETUDES/3A/OSY/Deep_learning/projet/FlickrLogos_47"
folder1 = path + "/train/000000/"
folder2 = path + "/train/000001/"
folder3 = path + "/train/000002/"
folders = [folder1, folder2, folder3]


def parser():
    new_folder_path = path + "/classes_non_dedoublees"
    try:
        os.mkdir(new_folder_path)
    except:
        pass
    for i in range(47):
        try:
            os.mkdir(new_folder_path + "/" + str(i))
        except:
            pass
    for folder in folders:
        for doc in os.listdir(folder):
            if doc.endswith(".png"):
                if "mask" not in doc:
                    img_infos_path = folder + doc.replace(".png", "") + ".gt_data.txt"
                    with open(img_infos_path, "r") as img_infos:
                        for line in img_infos:
                            data = line.split()
                            if data[7] == '0':
                                img_path = new_folder_path + "/" + data[4]
                                shutil.copy(folder + doc, img_path)


parser()