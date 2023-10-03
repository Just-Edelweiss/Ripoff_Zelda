import pygame as pyg
from parametre import *

class Tiles(pyg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pyg.image.load('assets\Arbre.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)