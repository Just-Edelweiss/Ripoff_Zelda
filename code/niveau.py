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
        """        for index_ligne, ligne in enumerate(map):
            for index_colonne, colonne in enumerate(ligne):
                x = index_colonne * tilesize
                y = index_ligne * tilesize
                if colonne == 'x':
                    Tiles((x, y), [self.sprites_visible, self.sprites_barriere])
                if colonne == 'p':
                    self.perso = Perso((x, y), [self.sprites_visible], self.sprites_barriere)"""
        self.perso = Perso((448, 96), [self.sprites_visible], self.sprites_barriere)

    def run(self):
        self.sprites_visible.draw_custom()
        self.sprites_visible.update()


class YSortCameraGroup(pyg.sprite.Group):
    def __init__(self):

        super().__init__()
        self.affiche_surface = pyg.display.get_surface()
        self.offset = pyg.math.Vector2()
        

        self.sol_surf = pyg.image.load('assets/Zeldouille_map.png').convert()
        self.sol_rect = self.sol_surf.get_rect(topleft = (0, 0))

    def draw_custom(self):
        pos_offset_sol = self.sol_rect.topleft
        self.affiche_surface.blit(self.sol_surf, pos_offset_sol)

        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
            self.affiche_surface.blit(sprite.image, sprite.rect)
        

