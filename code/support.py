import pygame as pyg
from csv import reader
from os import walk

def import_csv_layout(chemin):
    terrain = []
    with open(chemin) as map_level:
        layout = reader(map_level, delimiter = ',')
        for ligne in layout:
            terrain.append(list(ligne))
    return terrain

def import_fichier(chemin):
    list_surf = []
    for _,__,img_files in walk(chemin):
        for image in img_files:
            chemin_complet = chemin + '/' + image
            image_surf = pyg.image.load(chemin_complet).convert_alpha()
            list_surf.append(image_surf)
        return list_surf

