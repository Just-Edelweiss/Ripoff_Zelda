import pygame as pyg
from parametre import *
from tile import *
from personnage import *



class Niveau:
    def __init__(self):
        self.affiche_surface = pyg.display.get_surface()

        # groupe de sprite visible et les barriere pour la map
        self.sprites_visible = pyg.sprite.Group()
        self.sprites_barriere = pyg.sprite.Group()
        self.create_map()

    def create_map(self):
        for index_ligne, ligne in enumerate(map):
            for index_colonne, colonne in enumerate(ligne):
                x = index_colonne * tilesize
                y = index_ligne * tilesize
                if colonne == 'x':
                    Tiles((x, y), [self.sprites_visible, self.sprites_barriere])
                if colonne == 'p':
                    Perso((x, y), [self.sprites_visible])

    def run(self):
        self.sprites_visible.draw(self.affiche_surface)

