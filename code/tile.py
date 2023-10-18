import pygame as pyg
from parametre import *

class Tile(pyg.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pyg.Surface((tilesize, tilesize))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)