from PIL import Image
import os

"""création de l'ensemble des dossiers contenant nos données d'intérêt"""
path = "/Users/baudouinfauchier-magnan/Documents/Centrale_3A/Deep_Learning/FlickrLogos_47"
folder1 = path + "/train/000000/"
folder2 = path + "/train/000001/"
folder3 = path + "/train/000002/"
folder4 = path + "/test/000000/"
folder5 = path + "/test/000001/"
folder6 = path + "/test/000002/"
folders = [folder1, folder2, folder3, folder4, folder5, folder6]

"""on met par défaut à 200 la largeur des images resizées"""
basewidth = 200


def parser():
    """méthode permettant de ne garder que les images qui nous intéressent, de les resizer et de créer le doc.txt qui les concerne"""
    with open("train.txt", 'w') as train:
        for folder in folders:
            for doc in os.listdir(folder):
                if doc.endswith(".png"):
                    if "mask" not in doc:
                        #on n'a plus que les photos
                        img_infos_path = folder.replace("FlickrLogos_47", "FlickrLogos_47_copie") + doc.replace(".png", "") + ".gt_data.txt"
                        #il s'agit du path du fichier .txt original qui contient les infos de l'image, et qu'il va falloir retraiter
                        new_img_infos_path = folder + doc.replace(".png", ".txt")
                        #path du futur fichier .txt
                        img = Image.open(folder + doc)
                        old_img = Image.open(folder.replace("FlickrLogos_47", "FlickrLogos_47_copie") + doc)
                        #j'ai créé une copie de FlickrLogos_47 afin de ne pas perdre les images et infos originales
                        wpercent = (basewidth/float(old_img.size[0]))
                        #taux de resizing
                        hsize = int((float(old_img.size[1])*float(wpercent)))
                        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                        #on resize l'image
                        img.convert("RGB")
                        img.save(folder + doc.replace(".png", ".jpg"))
                        #on la convertit en JPEG
                        with open(new_img_infos_path, 'w') as annotations:
                            with open(img_infos_path, "r") as img_infos:
                                for line in img_infos:
                                    data = line.split() 
                                    if data[7] == '0' and (data[4] == '7' or data[4] == '21'):
                                        #on ne garde que les BMW (classe 7) et les Ferrari (classe 21)
                                        if data[4] == '7':
                                            data[4] = '0'
                                        if data[4] == '21':
                                            data[4] = '1'
                                        train.writelines(folder + doc.replace(".png", ".jpg") + "\n")
                                        annotations.write(data[4] + " " 
                                        + str(((int(data[0]) + int(data[2]))/2)*wpercent/basewidth) + " " 
                                        + str(((int(data[1]) + int(data[3]))/2)*wpercent/hsize) + " " 
                                        + str((int(data[2]) - int(data[0]))*wpercent/basewidth) + " " 
                                        + str((int(data[3]) - int(data[1]))*wpercent/hsize) + "\n")



parser()