from typing import List, Optional
import pygame as pyg
from parametre import *
from tile import *
from personnage import *
from support import *
from random import choice

class Niveau:
    def __init__(self):
        
        # groupe de sprite visible et les barriere pour la map
        self.sprites_visible = YSortCameraGroup()
        self.sprites_barriere = pyg.sprite.Group()
        self.create_map()

    def create_map(self):
        layouts = {
            'barrier_limite': import_csv_layout('assets/map/Zeldouille_map_barrier.csv'),
            'cassable' : import_csv_layout('assets/map/Zeldouille_map_cassable.csv'),
            'objet' : import_csv_layout('assets/map/Zeldouille_map_objet.csv'),
        }
        graphics = {
            'herbe' : import_fichier('assets/herbe'),
            'objets' : import_fichier('assets/objet')
        }

        for style, layout in layouts.items():    
            for index_ligne, ligne in enumerate(layout):
                for index_colonne, colonne in enumerate(ligne):
                    if colonne != '-1':
                        x = index_colonne * tilesize
                        y = index_ligne * tilesize
                        if style == 'barrier_limite':
                            Tile((x, y), [self.sprites_barriere], 'invisible')
                        if style == 'cassable':
                            random_grass_image = choice(graphics['herbe'])
                            Tile((x, y), [self.sprites_visible, self.sprites_barriere], 'grass', random_grass_image)

                            # module pour faire apparitre les arbre
                        """if style == 'objet':
                            surf = graphics['objets'][int(colonne)]
                            Tile((x, y), [self.sprites_visible, self.sprites_barriere], 'objet', surf)"""
                                    
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
        

