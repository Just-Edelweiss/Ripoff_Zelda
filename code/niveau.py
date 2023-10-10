from typing import List, Optional
import pygame as pyg
from pygame.rect import Rect
from pygame.surface import Surface
from parametre import *
from tile import *
from personnage import *



class Niveau:
    def __init__(self):
        
        # groupe de sprite visible et les barriere pour la map
        self.sprites_visible = YSortCameraGroup()
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
                    self.perso = Perso((x, y), [self.sprites_visible], self.sprites_barriere)

    def run(self):
        self.sprites_visible.draw_custom()
        self.sprites_visible.update()


class YSortCameraGroup(pyg.sprite.Group):
    def __init__(self):

        super().__init__()
        self.affiche_surface = pyg.display.get_surface()

    def draw_custom(self):
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
            self.affiche_surface.blit(sprite.image, sprite.rect)
        

